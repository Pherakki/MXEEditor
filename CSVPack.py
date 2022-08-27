import os
import csv

from pyValkLib.containers.MXEN.MXEC.MXECInterface import MXECInterface
from pyValkLib.containers.MXEN.MXEC.MXECInterface import ParameterInterface
from pyValkLib.containers.MXEN.MXEC.MXECInterface import EntityInterface
from pyValkLib.containers.MXEN.MXEC.MXECInterface import GraphInterface, SubgraphInterface
from pyValkLib.containers.MXEN.MXEC.MXECInterface import NodeInterface, EdgeInterface
from pyValkLib.containers.MXEN.MXEC.MXECInterface import AssetInterface


if __name__ == "CSVPack":
    from CSVPackFuncs import repack_funcs, ExceptionMessageGenerator
else:
    from .CSVPackFuncs import repack_funcs, ExceptionMessageGenerator

def csvs_to_interface(path):
    mi = MXECInterface()
    
    pack_parameters(path, mi)
    pack_entities(path, mi)
    pack_paths(path, mi)
    pack_assets(path, mi)
    
    return mi



def pack_parameters(path, mi):
    parameters_path = os.path.join(path, "params")
    if not os.path.isdir(parameters_path):
        return
    
    registered_global_ids = {}
    for csv_file in os.listdir(parameters_path):
        if os.path.isfile(os.path.join(parameters_path, csv_file)):
            param_type, ext = os.path.splitext(csv_file)
            with open(os.path.join(parameters_path, csv_file), 'r', newline='', encoding="utf8") as F:
                csvreader = csv.reader(F, delimiter=',', quotechar='"')
                
                # Don't need the header, so skip it
                next(csvreader)
                
                for row in csvreader:
                    pi = ParameterInterface.init_from_type(param_type)
                    
                    # Pack ID and Name
                    try:
                        param_id = int(row[0])
                        pi.ID = param_id
                    except Exception:
                        raise Exception(f"Attempted to pack {param_type} entry {row[0]}; could not convert ID to int.")
                    pi.name = row[1]
                    
                    # Since we currently have global parameter IDs, let's check
                    # that the ID hasn't already been registered
                    if param_id not in registered_global_ids:
                        registered_global_ids[param_id] = param_type
                    else:
                        raise Exception(f"Attempted to pack {param_type} entry {param_id}; ID already used in {registered_global_ids[param_id]}.")
                    
                    # Now pack the parameter data
                    if len(row) - 2 != len(pi.parameters):
                        raise Exception(f"Attempted to pack {param_type} entry {param_id}; number of parameters ({len(row)-2}) does not match definition ({len(pi.parameters)}).")
                    param_def = pi.get_type_def()
                    flat_defs = {k: v[1:] for chunk in param_def.get("struct", []) for k, v in chunk.items()}
                    for key, elem in zip(pi.parameters, row[2:]):
                        try:
                            converted_elem = repack_funcs[flat_defs[key]](elem)
                        except ExceptionMessageGenerator as e:
                            raise Exception(f"Attempted to convert '{key}' entry of {param_type} entry {param_id}; {e.generate_exception_msg()}") from e
                        except Exception as e:
                            raise Exception(f"Attempted to convert '{key}' entry of {param_type} entry {param_id}, but an unknown exception occurred: {e}.")
                        pi.parameters[key] = converted_elem
                        
                    # aaaaaand pack any subparameters
                    param_subparams = param_def.get("subparams", {})
                    if len(param_subparams):
                        subparam_dir = os.path.join(parameters_path, param_type)
                        if not os.path.isdir(subparam_dir):
                            raise Exception(f"Attempted to pack {param_type}.csv, which has subparameters, but the folder 'params/{param_type}' that should contain subparameters is not present.")
                        for subparam_name, subparam_info in param_subparams.items():
                            subparam_csv = os.path.join(subparam_dir, os.path.extsep.join((subparam_name, "csv")))
                            subparam_type = subparam_info["type"]
                            
                            if not os.path.isdir(subparam_dir):
                                raise Exception(f"Attempted to pack {param_type}.csv, which has the subparameter '{subparam_name}', but the csv file 'params/{param_type}/{subparam_csv}' that should contain the subparameter data is not present.")
                            
                            with open(subparam_csv, 'r', newline='', encoding="utf8") as F:
                                csvreader = csv.reader(F, delimiter=',', quotechar='"')
                                
                                # Don't need the header, so skip it
                                next(csvreader)
                                
                                for sprow in csvreader:
                                    if len(sprow) < 1:
                                        continue
                                    
                                    parent_id = sprow[0]
                                    # Pack parent ID
                                    try:
                                        int_parent_id = int(sprow[0])
                                    except Exception:
                                        raise Exception(f"Attempted to read {param_type} subparameters file {subparam_csv}; could not convert parent ID '{parent_id}' to int.")
                                    
                                    if int_parent_id == param_id:
                                        spi = ParameterInterface.init_from_type(subparam_type)
                                        
                                        # Now pack the parameter data
                                        if len(sprow) - 1 != len(spi.parameters):
                                            raise Exception(f"Attempted to pack {param_type} subparameters file {subparam_csv}; number of parameters ({len(row)-1}) does not match definition ({len(spi.parameters)}).")
                                        
                                        subparam_def = spi.get_type_def()
                                        spflat_defs = {k: v[1:] for chunk in subparam_def.get("struct", []) for k, v in chunk.items()}
                                        
                                        for key, elem in zip(spi.parameters, sprow[1:]):
                                            try:
                                                converted_elem = repack_funcs[spflat_defs[key]](elem)
                                            except ExceptionMessageGenerator as e:
                                                raise Exception(f"Attempted to convert '{key}' entry of {subparam_type} subparameter of {param_type} entry {parent_id}; {e.generate_exception_msg()}") from e
                                            except Exception as e:
                                                raise Exception(f"Attempted to convert '{key}' entry of {subparam_type} subparameter of {param_type} entry {parent_id}, but an unknown exception occurred: {e}.")
                                            spi.parameters[key] = converted_elem
                                        
                                        # Now add the subparameter to the parameter
                                        pi.subparameters[subparam_name].append(spi)
                    
                    # Now add the parameter to the interface
                    mi.param_sets.append(pi)
                
    # Check that the global IDs are contiguous
    missing_ids = []
    sorted_ids = sorted(registered_global_ids.keys())
    missing_ids.extend(range(0, sorted_ids[0]))
    for id_1, id_2 in zip(sorted_ids, sorted_ids[1:]):
        if id_2 != id_1 + 1:
            missing_ids.extend(range(id_1+1, id_2))
    if len(missing_ids):
        raise Exception(f"Parameter IDs must be contiguous. The following IDs are missing:\n{', '.join([str(elem) for elem in missing_ids])}.")
        
    # Make sure the parameters are sorted by ID
    mi.param_sets = sorted(mi.param_sets, key=lambda pi: pi.ID)

def pack_entities(path, mi):
    entities_path = os.path.join(path, "entities")
    if not os.path.isdir(entities_path):
        return
    
    registered_global_ids = {}
    for csv_file in os.listdir(entities_path):
        if os.path.isfile(os.path.join(entities_path, csv_file)):
            entity_type, ext = os.path.splitext(csv_file)
            with open(os.path.join(entities_path, csv_file), 'r', newline='', encoding="utf8") as F:
                csvreader = csv.reader(F, delimiter=',', quotechar='"')
                
                header = next(csvreader)
                
                for row in csvreader:
                    ei = EntityInterface.init_from_type(entity_type)
                    # Pack ID, Name, Controller ID, and Unknown
                    try:
                        ei.ID = int(row[0])
                    except Exception:
                        raise Exception(f"Attempted to pack {entity_type} entry {row[0]}; could not convert ID '{row[0]}' to int.")
                    ei.name = row[1]
                    try:
                        ei.controller_id = int(row[2])
                    except Exception:
                        raise Exception(f"Attempted to pack {entity_type} entry {ei.ID}; could not convert controller_id '{row[2]}' to int.")
                    try:
                        if len(row[3]):
                            ei.unknown = int(row[3])
                        else:
                            ei.unknown = None
                    except Exception:
                        raise Exception(f"Attempted to pack {entity_type} entry {ei.ID}; could not convert Unknown to int.")
                    
                    # Since we currently have global parameter IDs, let's check
                    # that the ID hasn't already been registered
                    if ei.ID not in registered_global_ids:
                        registered_global_ids[ei.ID] = entity_type
                    else:
                        raise Exception(f"Attempted to pack {entity_type} entry {ei.ID}; ID already used in {registered_global_ids[ei.ID]}.")
                    
                    # Now pack up the Entity IDs
                    param_refs = [pref for subentity in ei.all_flat_entities() for pref in subentity.parameters]
                    param_values = row[4:]
                    if len(param_values) != len(param_refs):
                        raise Exception(f"Attempted to pack {entity_type} entry {ei.ID}; number of parameters ({len(row)-4}) does not match definition ({len(param_refs)}).")
                    
                    for i, (pref, elem) in enumerate(zip(param_refs, param_values)):
                        try:
                            int_elem = int(elem)
                        except Exception:
                            raise Exception(f"Attempted to convert '{header[i+4]}' entry of {entity_type} entry {ei.ID}; could not convert {elem} to 'int'.")
                            
                        pref.param_id = int_elem
                        real_type = mi.param_sets[int_elem].param_type
                        if pref.type != real_type:
                           raise Exception(f"Attempted to pack {entity_type} entry {ei.ID}; the parameter {int_elem} is of type {real_type} but {pref.type} is required.")
                    
                    mi.entities.append(ei)
    
    # Sort the entities by ID
    mi.entities = sorted(mi.entities, key=lambda ei: (ei.entity.type, ei.ID))

def pack_paths(path, mi):
    paths_path = os.path.join(path, "paths")
    if not os.path.isdir(paths_path):
        return
    
    path_lookup = {}
    paths_csv = os.path.join(paths_path, "paths.csv")
    if not os.path.isfile(paths_csv):
        raise Exception("Attempted to pack the 'paths' folder, but could not find 'paths/paths.csv'.")
        
            
    # Gather all path IDs referenced by the parameters
    required_paths = []
    for param_set in mi.param_sets:
        param_id = param_set.ID
        type_def = param_set.get_type_def()
        struct_def = type_def.get("struct", [])
        flat_struct = {}
        for substruct in struct_def:
            flat_struct.update(substruct)
        for type_name, type_type in flat_struct.items():
            if type_type[1:] == "path":
                if "paths" not in type_def:
                    raise Exception(f"Tried to find path '{type_name}' in parameter def '{param_set.param_type}', but no path library was found in the definition file.")
                if type_name not in type_def["paths"]:
                    raise Exception(f"Tried to find path '{type_name}' in parameter def '{param_set.param_type}', but it was not found in the definition file's path library.")
                
                if param_set.parameters[type_name] != -1:
                    required_paths.append([param_set.parameters[type_name], type_def["paths"][type_name], param_id, param_set.param_type])
    
    # Build lookups for checking path consistency
    path_lookup_by_id = {}
    for path_links in required_paths:
        path_id = path_links[0]
        if path_id not in path_lookup_by_id:
            path_lookup_by_id[path_id] = []
        path_lookup_by_id[path_id].append([path_links[1], path_links[2], path_links[3]])
    path_lookup_by_id = {k:v for k, v in sorted(path_lookup_by_id.items(), key=lambda x: x[0])}
        
    # Check that pyValkLib doesn't have a bug in the structure definitions,
    # construct a lookup for path types
    path_types_lookup = {}
    parameter_ids_linked_to_paths = {}
    for id_, data in path_lookup_by_id.items():
        path_types = set([d[0] for d in data])
        if len(path_types) != 1:
            raise Exception("Attempted to pack path {id_}: encountered a critical internal pyValkLib error - more than one type was found for this path: {', '.join([str(e) for e in sorted(path_types)])}.")
        path_types_lookup[id_] = list(path_types)[0]
        parameter_ids_linked_to_paths[id_] = [d[1:3] for d in data]
    del path_lookup_by_id
        
    # Read paths
    with open(paths_csv, 'r', newline='', encoding="utf8") as F:
        csvreader = csv.reader(F, delimiter=',', quotechar='"')
        
        header = next(csvreader)
        
        for i, row in enumerate(csvreader):
            if len(row) == 0:
                continue
                
            # Get path ID
            try:
                path_id = int(row[0])
            except Exception:
                raise Exception(f"Attempted to pack path with ID '{row[0]}'; could not convert ID to int.")
            
            # Get path name
            if len(row) < 1:
                path_name = ""
            else:
                path_name = row[1]
                    
            path_lookup[path_id] = path_name
    
    # Read in path in turn
    required_path_ids = set([x[0] for x in required_paths])
    located_path_ids = set()
    graphs = []
    for path_id, path_name in path_lookup.items():
        gi = GraphInterface()
        
        graph_type = None
        if path_id in path_types_lookup:
            graph_type = path_types_lookup[path_id]
        
        this_path_path = os.path.join(paths_path, path_name)
        if not os.path.isdir(this_path_path):
            raise Exception(f"Attempted to pack path '{path_name}'; could not find the directory {this_path_path}.")
        
        # Validate the subgraph files
        subgraph_files = os.listdir(this_path_path)
        for file in subgraph_files:
            try:
                int(os.path.splitext(file)[0])
            except Exception as e:
                raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}': could not interpret filename '{os.path.splitext(file)[0]}' as an integer.") from e
        subgraph_files = sorted(subgraph_files, key=lambda x: int(os.path.splitext(x)[0]))
        
        # Pack each subgraph
        for i, subgraph_file in enumerate(subgraph_files):
            sgi = SubgraphInterface()
            subgraph_file_path = os.path.join(this_path_path, subgraph_file)
            with open(subgraph_file_path, 'r', newline='', encoding="utf8") as F:
                csvreader = csv.reader(F, delimiter=',', quotechar='"')
                
                header = next(csvreader)
                
                # Make a map of indices to rows
                row_map = {}
                rows = []
                for row_idx, row in enumerate(csvreader):              
                    # Validate the ID
                    if len(row) < 1:
                        raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}': row {i+1} has a length of 0 and therefore does not have an ID.")
                    try:
                        int_id = int(row[0])
                    except Exception as e:
                        raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}', row {i+1}: could not interpret parameter ID '{row[0]}' as an integer.") from e
        
                    row_map[int_id] = row_idx
                    rows.append((row_idx, row))
                    
                # Pack each node in the subgraph
                for row_idx, row in rows:
                    ni = NodeInterface()
                    
                    # Validate the parameter idx
                    if len(row) < 2:
                        raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}': row {i+1} only has a length of 1 and therefore does not have a parameter.")
                    try:
                        int_param = int(row[1])
                    except Exception as e:
                        raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}', row {i+1}: could not interpret parameter ID '{row[1]}' as an integer.") from e
        
                    # Pack the ID
                    param_type = mi.param_sets[int_param].param_type
                    if graph_type is None:
                        graph_type = param_type
                    else:
                        if graph_type != param_type:
                          raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}', row {i+1}: type of first graph node's parameter is '{graph_type}', but encountered node's parameter is '{param_type}'.")
          
                    ni.param_id = int_param
                    
                    # Pack the next edges
                    num_remaining_elements = len(row) - 2
                    for nni in range((num_remaining_elements // 2) - 1):
                        ei = EdgeInterface()
                                            
                        # Validate the node ID
                        next_node_id = row[nni*2 + 2]
                        try:
                            int_next_node_id = int(next_node_id)
                        except Exception as e:
                            raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}', row {i+1}: could not interpret next node ID '{next_node_id}' as an integer.") from e
            
                        ei.next_node = row_map[int_next_node_id]
                        
                        # Validate the parameter IDs
                        next_param_ids = row[nni*2 + 3]
                        next_param_ids = next_param_ids.split(" ")
                        next_param_ids = [e.strip() for e in next_param_ids if len(e)]
                        bad_ids = []
                        for nnpi_idx, nnpi in enumerate(next_param_ids):
                            try:
                                int_nnpi = int(nnpi)
                                ei.param_ids.append(int_nnpi)
                            except Exception:
                                bad_ids.append(nnpi_idx, nnpi)
                        if len(bad_ids):
                            raise Exception(f"Attempted to pack path '{path_name}', subgraph file '{file}', row {i+1}: could not interpret next node parameters '{next_param_ids}' as a list of integers. Values {', '.join([str(nnpi_idx) + ' (' + str(nnpi) + ') for nnpi_idx, nnpi in bad_values'])} were problematic.")
            
                        ni.next_edges.append(ei)
                    sgi.nodes.append(ni)
                        
            gi.subgraphs.append(sgi)
            
        gi.name = path_name
        gi.node_type = graph_type
        graphs.append((path_id, gi))
        located_path_ids.add(path_id)
                
    # Check that any paths we needed are not missing
    required_path_ids -= located_path_ids
    if len(required_path_ids):
        error_string = ""
        for id_ in sorted(required_path_ids):
            param_info = parameter_ids_linked_to_paths[id_]
            error_string += str(id_) + ": "
            error_string += ", ".join(f"{p_id} ({p_type})" for p_id, p_type in param_info)
            error_string += "\n"
        raise Exception(f"Attempted to pack paths, but some IDs referenced in the parameters were not defined in paths.csv. Was unable to find the IDs referenced by the following parameters:\n{error_string}") 
           
    # Check that no graph IDs are missing
    graphs = sorted(graphs, key=lambda x: x[0])
    graph_ids = [x[0] for x in graphs]
    missing_ids = list(range(graph_ids[0]))
    for id_1, id_2 in zip(graph_ids, graph_ids[1:]):
        if id_2 != id_1 + 1:
            missing_ids.extend(range(id_1+1, id_2))
    if len(missing_ids):
        raise Exception(f"Attempted to pack paths, but path IDs were non-contiguous. Missing IDs:\n{', '.join([str(e) for e in missing_ids])}.")
            
    # Assign the paths
    mi.path_graphs = [x[1] for x in graphs]
    
def pack_assets(path, mi):
    assets_path = os.path.join(path, "assets.csv")
    if not os.path.isfile(assets_path):
        return
    
    # Gather all asset IDs referenced by the parameters
    required_assets = []
    for param_set in mi.param_sets:
        param_id = param_set.ID
        type_def = param_set.get_type_def()
        struct_def = type_def.get("struct", [])
        flat_struct = {}
        for substruct in struct_def:
            flat_struct.update(substruct)
        for type_name, type_type in flat_struct.items():
            if type_type[1:] == "asset":
                if "assets" not in type_def:
                    raise Exception(f"Tried to find asset '{type_name}' in parameter def '{param_set.param_type}', but no asset library was found in the definition file.")
                if type_name not in type_def["assets"]:
                    raise Exception(f"Tried to find asset '{type_name}' in parameter def '{param_set.param_type}', but it was not found in the definition file's asset library.")
                
                if param_set.parameters[type_name] != -1:
                    required_assets.append([param_set.parameters[type_name], type_def["assets"][type_name], param_id, param_set.param_type])
    
    # Build lookups for checking asset consistency
    asset_lookup_by_id = {}
    for asset_links in required_assets:
        asset_id = asset_links[0]
        if asset_id not in asset_lookup_by_id:
            asset_lookup_by_id[asset_id] = []
        asset_lookup_by_id[asset_id].append([asset_links[1], asset_links[2], asset_links[3]])
    asset_lookup_by_id = {k:v for k, v in sorted(asset_lookup_by_id.items(), key=lambda x: x[0])}
    
    # Check that pyValkLib doesn't have a bug in the structure definitions,
    # construct a lookup for asset types
    asset_types_lookup = {}
    parameter_ids_linked_to_asset = {}
    for id_, data in asset_lookup_by_id.items():
        asset_types = set([d[0] for d in data])
        if len(asset_types) != 1:
            raise Exception("Attempted to pack asset {id_}: encountered a critical internal pyValkLib error - more than one type was found for this asset: {', '.join([str(e) for e in sorted(asset_types)])}.")
        asset_types_lookup[id_] = list(asset_types)[0]
        parameter_ids_linked_to_asset[id_] = [d[1:3] for d in data]
    del asset_lookup_by_id
    
    # Now read in the assets we have data for
    required_asset_ids = set([x[0] for x in required_assets])
    located_asset_ids = set()
    with open(assets_path, 'r', newline='', encoding="utf8") as F:
        csvreader = csv.reader(F, delimiter=',', quotechar='"')
        
        next(csvreader)
    
        for row_idx, row in enumerate(csvreader):
            if len(row) < 4:
                raise Exception(f"Attempted to pack asset row '{row_idx}': row has fewer than 5 elements. Expected: [ID, Asset Type, Unknown ID 1, Unknown ID 2, Asset Path]")

            ai = AssetInterface()
            int_row = []
            for i in range(3):
                try:
                    int_elem = int(row[i])
                except Exception as e:
                    raise Exception(f"Attempted to pack asset row '{row_idx}', column {i}: cannot interpret '{row[i]}' as an integer.") from e
                int_row.append(int_elem)
            
            asset_id        = int_row[0]
            ai.ID = asset_id
            ai.unknown_id_1 = int_row[1]
            ai.unknown_id_2 = int_row[2]
            ai.filepath     = row[3]
            
            # if asset_ID not in asset_types_lookup:
            #    raise Exception(f"Attempted to pack asset row '{row_idx}, ID {asset_ID}': CRITICAL INTERNAL ERROR. ASSET WAS NOT GIVEN A TYPE. PLEASE REPORT WITH FULL REPRODUCTION DETAILS.")
               
            filepath_extension = os.path.splitext(ai.filepath)[1].lstrip(os.path.extsep)  
            atype = asset_types_lookup.get(asset_id, "???")

            if atype not in ai.asset_defs:
                asset_lookup_heuristic = {
                    ext: num for ext, num in ai.asset_defs.values() 
                    if num != 21 # 21 is texmerge, probably want the "main" htex type
                }
                print(asset_lookup_heuristic)
                if filepath_extension not in asset_lookup_heuristic:
                    raise Exception(f"Attempted to pack asset row '{row_idx}', ID {asset_id}: unknown file extension '{filepath_extension}'.")
                ai.asset_type = asset_lookup_heuristic[filepath_extension]
            else:
                ai.asset_type, asset_extension = ai.asset_defs[asset_types_lookup[asset_id]]
                if asset_extension != filepath_extension:
                    error_string = ""
                    param_info = parameter_ids_linked_to_asset[asset_id]
                    error_string += ", ".join(f"{p_id} ({p_type})" for p_id, p_type in param_info)
                    error_string += "\n"
                    raise Exception(f"Attempted to pack asset row '{row_idx}', ID {asset_id}: found filepath extension '{filepath_extension}', but the asset is referenced by parameters that expect the extension '{asset_extension}'. These parameters are:\n{error_string}")
                    
            mi.assets.append(ai)
            
            located_asset_ids.add(asset_id)
            
    # Check that any assets we needed are not missing
    required_asset_ids -= located_asset_ids
    if len(required_asset_ids):
        error_string = ""
        for id_ in sorted(required_asset_ids):
            param_info = parameter_ids_linked_to_asset[id_]
            error_string += str(id_) + ": "
            error_string += ", ".join(f"{p_id} ({p_type})" for p_id, p_type in param_info)
            error_string += "\n"
        raise Exception(f"Attempted to pack assets, but some IDs referenced in the parameters were not defined in assets.csv. Was unable to find the IDs referenced by the following parameters:\n{error_string}") 
            
    # Assign assets
    mi.assets = sorted(mi.assets, key=lambda ai: ai.ID)
    
    # Check that all asset IDs are contiguous
    asset_ids = [ai.ID for ai in mi.assets]
    missing_ids = list(range(asset_ids[0]))
    for id_1, id_2 in zip(asset_ids, asset_ids[1:]):
        if id_2 != id_1 + 1:
            missing_ids.extend(range(id_1+1, id_2))
    if len(missing_ids):
        raise Exception(f"Attempted to pack assets, but asset IDs were non-contiguous. Missing IDs:\n{', '.join([str(e) for e in missing_ids])}.")
        
            