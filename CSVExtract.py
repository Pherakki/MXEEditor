import csv
import os

def interface_to_csvs(outpath, mi, filename):
    os.makedirs(os.path.join(outpath, filename), exist_ok=True)
    
    # Write out parameters
    if len(mi.param_sets):
        params_by_type = {}
        for param_set in mi.param_sets:
            ptype = param_set.param_type
            if ptype not in params_by_type:
                params_by_type[ptype] = []
            params_by_type[ptype].append(param_set)
            
        param_path = os.path.join(outpath, filename, "params")
        os.makedirs(param_path, exist_ok=True)
        for ptype, pdata in params_by_type.items():
            # Dump the parameter data
            param_def = pdata[0].get_type_def()
            
            subparam_data = {nm: [] for nm in param_def.get("subparams", {})}
            with open(os.path.join(param_path, ptype + ".csv"), 'w', newline='', encoding="utf8") as F:
                csvwriter = csv.writer(F, delimiter=',', quotechar='"')
                
                header = ["ID", "Name", *pdata[0].parameters.keys()]
                csvwriter.writerow(header)
                
                for pdata_elems in pdata:
                    param_vals = list(pdata_elems.parameters.values())
                    param_vals = [" ".join([str(se) for se in e]) if (hasattr(e, "__iter__") and not type(e) == str) else str(e) for e in param_vals]
                    row = [pdata_elems.ID, pdata_elems.name, *param_vals]

                    csvwriter.writerow(row)
                    
                    for subparam_set_name, subparam_set in pdata_elems.subparameters.items():
                        for subparam in subparam_set:
                            subparam_data[subparam_set_name].append([pdata_elems.ID, subparam])
            
            # Dump the subparameters
            if len(subparam_data):
                subparam_path = os.path.join(param_path, ptype)
                os.makedirs(subparam_path, exist_ok=True)
                for subparam_name, subparam_datum in subparam_data.items():
                    with open(os.path.join(subparam_path, subparam_name + ".csv"), 'w', newline='', encoding="utf8") as F:
                        csvwriter = csv.writer(F, delimiter=',', quotechar='"')
                        header = ["Parent ID", *subparam_datum[0][1].parameters.keys()]
                        csvwriter.writerow(header)
                        
                        for parent_id, pdata_elems in subparam_datum:
                            param_vals = list(pdata_elems.parameters.values())
                            param_vals = [" ".join([str(se) for se in e]) if (hasattr(e, "__iter__") and not type(e) == str) else e for e in param_vals]
                            row = [parent_id, *param_vals]
                            csvwriter.writerow(row)
                            
    # Write out entities
    if len(mi.entities):
        entities_by_type = {}
        for entity in mi.entities:
            etype = entity.entity.type
            if etype not in entities_by_type:
                entities_by_type[etype] = []
            entities_by_type[etype].append(entity)
            
        entity_path = os.path.join(outpath, filename, "entities")
        os.makedirs(entity_path, exist_ok=True)
        for etype, edata in entities_by_type.items():
            with open(os.path.join(entity_path, etype + ".csv"), 'w', newline='', encoding="utf8") as F:
                csvwriter = csv.writer(F, delimiter=',', quotechar='"')
                
                header = ["ID", "Name", "Controller Entity", "Unknown"]
                subcomps = edata[0].all_flat_entities()
                for subcomp in subcomps:
                    for param_ref in subcomp.parameters:
                        header.append(param_ref.type)
                
                csvwriter.writerow(header)
                
                for edatum in edata:
                    row = [edatum.ID, edatum.name, edatum.controller_id, edatum.unknown]
                    for subentity in edatum.all_flat_entities():
                        for param_ref in subentity.parameters:
                            row.append(param_ref.param_id)
                    csvwriter.writerow(row)
                
    # Write out paths
    if len(mi.path_graphs):
        path_dir = os.path.join(outpath, filename, "paths")
        for path_graph in mi.path_graphs:
            this_path_dir = os.path.join(path_dir, path_graph.name)
            os.makedirs(this_path_dir, exist_ok=True)
            
            # Write nodes
            for i, subgraph in enumerate(path_graph.subgraphs):
                with open(os.path.join(this_path_dir, f"{i}.csv"), 'w', newline='', encoding="utf8") as F:
                    csvwriter = csv.writer(F, delimiter=',', quotechar='"')
                    
                    num_edges = max([len(node.next_edges) for node in subgraph.nodes])
                    
                    header = ["ID", "Node Parameter"]
                    header.extend([subitem for item in [[f"Next Node {i+1}", f"Node Node {i+1} Parameters"] for i in range(num_edges)] for subitem in item])
                    csvwriter.writerow(header)
                    
                    for i, node in enumerate(subgraph.nodes):
                        row = [i, node.param_id]
                        for next_edge in node.next_edges:
                            row.append(str(next_edge.next_node))
                            row.append(" ".join([str(id_) for id_ in next_edge.param_ids]))
                        csvwriter.writerow(row)
    
        
        with open(os.path.join(path_dir, "paths.csv"), 'w', newline='', encoding="utf8") as F:
            csvwriter = csv.writer(F, delimiter=',', quotechar='"')
            
            header = ["ID", "Name"]
            csvwriter.writerow(header)
            for i, path_graph in enumerate(mi.path_graphs):
                row = [i, path_graph.name]
                csvwriter.writerow(row)
        
    # Write out assets
    if len(mi.assets):
        with open(os.path.join(outpath, filename, "assets.csv"), 'w', newline='', encoding="utf8") as F:
            csvwriter = csv.writer(F, delimiter=',', quotechar='"')
            header = ["ID", "Unknown ID 1", "Unknown ID 2", "Asset Path"]
            csvwriter.writerow(header)
            
            for i, asset in enumerate(mi.assets):
                row = [asset.ID, asset.unknown_id_1, asset.unknown_id_2, asset.filepath]
                csvwriter.writerow(row)
    