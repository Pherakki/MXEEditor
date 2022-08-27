import os
import json
import struct

from .MXECReadWriter import MXECReadWriter
from .ParameterEntry import param_structs
from .ECSEntityEntry import EntityEntry, EntityData, EntitySubEntry
from .PathingEntry import PathNode, PathEdge, SubGraph, PathingEntry
from pyValkLib.serialisation.ReadWriter import OffsetTracker, POF0Builder, ENRSBuilder, CCRSBuilder
from pyValkLib.containers.POF0.POF0ReadWriter import compressPOF0
from pyValkLib.containers.ENRS.ENRSCompression import compressENRS, toENRSPackedRep
from pyValkLib.containers.CCRS.CCRSCompression import compressCCRS, toCCRSPackedRep


entity_structs = {}
struct_path = os.path.abspath("pyValkLib/configuration/MXE/Entities")
for file in os.listdir(struct_path):
    filename, fileext = os.path.splitext(file)
    if fileext == ".json":
        filepath = os.path.join(struct_path, file)
        with open(filepath, 'r') as F:
            entity_structs[filename] = json.load(F)
            if "SubEntities" not in entity_structs[filename]:
                raise Exception(f"Invalid Entity structure file {filename}: No 'SubEntities' member.")
            if "Parameters" not in entity_structs[filename]:
                raise Exception(f"Invalid Entity structure file {filename}: No 'Parameters' member.")


class ParameterInterface:
    def __init__(self):
        self.name = None
        self.ID = None
        self.param_type = None
        self.parameters = None
        self.subparameters = None
        
    @classmethod
    def init_from_type(cls, typename):
        if typename not in param_structs:
            raise ValueError(f"{typename} is not a known ParameterSet type.")
        
        param_def = param_structs[typename]
        
        pi = ParameterInterface()
        pi.param_type = typename
        pi.parameters = {}
        for param_chunk in param_def.get("struct", []):
            for param_name, param_type in param_chunk.items():
                param_type_string = param_type[1:]
                if any(param_type_string == ty for ty in ["pad8", "pad16", "pad32", "pad64"]):
                    continue
                else:
                    pi.parameters[param_name] = None
        
        pi.subparameters = {}
        for param_name in param_def.get("subparams", {}):
            pi.subparameters[param_name] = []
            
        return pi
            
    def get_type_def(self, param_type=None):
        if param_type is None:
            param_type = self.param_type
        if param_type not in param_structs:
            raise ValueError(f"{self.param_type} is not a known ParameterSet type.")
        
        return param_structs[param_type]

class EntityParameterReference:
    def __init__(self, type_, subtype_):
        self.param_id = None
        self.type = type_
        self.subtype = subtype_

class EntityComponentInferface:
    def __init__(self, type_):
        self.type = type_
        self.subentities = []
        self.parameters = []
        
        if type_ not in entity_structs:
            raise TypeError(f"No known entity type '{type_}'.")
            
        def_struct = entity_structs[type_]
        for en in def_struct["SubEntities"]:
            self.subentities.append(EntityComponentInferface(en))
        for subtype_, type_ in def_struct["Parameters"]:
            self.parameters.append(EntityParameterReference(type_, subtype_))
        
    def flat_decendants(self):
        out = []
        for subentity in self.subentities:
            out.append(subentity)
            for dec in subentity.flat_decendants():
                out.append(dec)
        return out
    
    def get_param_prefixes(self):
        out = {}
        
        # Append entity name to front of child's stack
        for subentity in self.subentities:
            name_strs = subentity.get_param_prefixes()
            for param_id, name_str in name_strs.items():
                out[param_id] = "!" + self.type + name_str
        
        # Add own parameters to stack
        for param in self.parameters:
            name_str = "!" + self.type + "!@" + param.subtype + "@"
            out[param.param_id] = name_str
            
        return out
        
class EntityInterface:
    def __init__(self):
        self.ID = None
        self.name = None
        self.unknown = None
        self.controller_id = None
        self.entity = None
        
    @classmethod
    def init_from_type(cls, typename):
        ei = EntityInterface()
        ei.entity = EntityComponentInferface(typename)
        
        return ei
        
    def all_flat_entities(self):
        return [self.entity, *self.entity.flat_decendants()]
    
    def get_all_param_prefixes(self):
        return self.entity.get_param_prefixes()
    
class NodeInterface:
    def __init__(self):
        self.param_id = None
        self.next_edges = []
        
class EdgeInterface:
    def __init__(self):
        self.next_node = None
        self.param_ids = []

class SubgraphInterface:
    def __init__(self):
        self.nodes = []

class GraphInterface:
    def __init__(self):
        self.name = None
        self.node_type = None
        self.subgraphs = []
        
class AssetInterface:
    """
    Main ID Order: ???
    Unknown ID 1 order: ??? Related to entity / parameter types?
    Unknown ID 2 assigned by sorting by extension, then filepath (or file?)
    """
    
    asset_defs = {
        "hmd"           : ( 1, "hmd"),
        "htx"           : ( 2, "htx"),
        "hmt"           : ( 3, "hmt"),
        "mcl"           : ( 6, "mcl"),
        "mlx"           : ( 8, "mlx"),
        "abr"           : ( 9, "abr"),
        "abd"           : (10, "abd"),
        "cvd"           : (12, "cvd"),
        "hst"           : (12, "hst"),
        "bhv"           : (12, "bhv"),
        "pvs"           : (20, "pvs"),
        "htx_merge"     : (21, "htx"),
        "htr"           : (22, "htr"),
        "mmf"           : (24, "mmf"),
        "mmr"           : (25, "mmr")  
    }
    
    def __init__(self):
        self.ID = None
        self.filepath = None
        self.asset_type = None # Should be able to reconstruct this!!!
        self.unknown_id_1 = None
        self.unknown_id_2 = None
        
    def __repr__(self):
        return f"::Asset:: {self.asset_type} {self.unknown_id_1} {self.unknown_id_2} {self.filepath}"

class MXECInterface:
    def __init__(self):
        self.param_sets = []
        self.entities = []
        self.path_graphs = []
        self.assets = []
        
        self.loose_nodes = []
        
    def __repr__(self):
        return "::MXECInterface Object::\n"\
              f"{len(self.param_sets)} parameter sets.\n"\
              f"{len(self.entities)} entities.\n"\
              f"{len(self.path_graphs)} paths.\n"\
              f"{len(self.assets)} assets.\n"
    
    @classmethod
    def generate_param_interface(cls, mxec_rw, param_set):
        pi = ParameterInterface()
        pi.name = None
        pi.ID = None
        pi.param_type = None
        pi.parameters = {}
        pi.subparameters = {}
        for (key, value), dtype in zip(param_set.data.items(), param_set.datatypes):
            if dtype[1:] == "pad8" or dtype[1:] == "pad16" or dtype[1:] == "pad32" or dtype[1:] == "pad64":
                continue
            elif dtype[1:] == "sjis_string":
                try:
                    pi.parameters[key] = mxec_rw.sjis_strings.at_ptr(value)
                except Exception as e:
                    print(pi.param_type, key)
                    raise e
            elif dtype[1:] == "utf8_string":
                try:
                    pi.parameters[key] = mxec_rw.utf8_strings.at_ptr(value)
                except Exception as e:
                    print(pi.param_type, key)
                    raise e
            else:
                pi.parameters[key] = value
                
            for subparam_name, subparams in param_set.subparams.items():
                pi.subparameters[subparam_name] = []
                for subparam in subparams:
                    pi.subparameters[subparam_name].append(cls.generate_param_interface(mxec_rw, subparam))
        return pi
    
    @classmethod
    def from_subreader(cls, mxec_rw):
        instance = cls()
        
        for i, param_set in enumerate(mxec_rw.parameter_sets_table.entries):
            #assert param_set.ID == i, f"{param_set.ID} {i}"
            pi = cls.generate_param_interface(mxec_rw, param_set.data)
            str_name = mxec_rw.sjis_strings.at_ptr(param_set.name_offset).split(':')
            pi.name = str_name[-1]
            pi.ID = param_set.ID
            pi.param_type = param_set.data.struct_type
            
            instance.param_sets.append(pi)
        
        for entity in mxec_rw.entity_table.entries:
            ei = EntityInterface()
            ei.name = mxec_rw.sjis_strings.at_ptr(entity.name_offset)
            ei.ID = entity.ID
            ei.controller_id = entity.controller_entity_id
            if entity.unknown_data_ptr != 0:
                ei.unknown = mxec_rw.unknowns.at_ptr(entity.unknown_data_ptr)
                
                
            parameter_ids = iter(entity.data.data)
            ei.entity = EntityComponentInferface(mxec_rw.sjis_strings.at_ptr(entity.data.subentries[-1].name_offset))
            
            for canon_subentry, data_subentry in zip(ei.all_flat_entities()[::-1], entity.data.subentries):
                data_name_type = mxec_rw.sjis_strings.at_ptr(data_subentry.name_offset)
                if canon_subentry.type != data_name_type or len(ei.all_flat_entities()[::-1]) != len(entity.data.subentries):
                    all_canon_names = [ce.type for ce in ei.all_flat_entities()[::-1]]
                    all_data_names = [mxec_rw.sjis_strings.at_ptr(de.name_offset) for de in entity.data.subentries]
                    
                    print("ERROR: Mismatch between entity definition and data.")
                    print(all_canon_names)
                    print(all_data_names)
                    raise ValueError()
                    
                parameters = [next(parameter_ids) for _ in range(data_subentry.count)]
                for canon_param, data_param in zip(canon_subentry.parameters, parameters):
                    assert instance.param_sets[data_param].param_type == canon_param.type
                    canon_param.param_id = data_param
            instance.entities.append(ei)
            
        all_nodes = {}
        used_nodes = {}
        node_params = {}
        for path in mxec_rw.pathing_table.entries:
            pi = GraphInterface()
            pi.name = mxec_rw.sjis_strings.at_ptr(path.name_offset)
            
            # Find the type of the graph
            # Graphs can only contain one type of node, so if you locate any
            # node in the graph, that gives you the type...
            if len(path.unused_nodes):
                param_id = path.graph_nodes[path.unused_nodes[0]].node_param_id
                pi.node_type = mxec_rw.parameter_sets_table.entries[param_id].data.struct_type
            elif len(path.subgraphs):
                for subgraph in path.subgraphs:
                    if len(subgraph.node_id_list):
                        param_id = path.graph_nodes[subgraph.node_id_list[0]].node_param_id
                        pi.node_type = mxec_rw.parameter_sets_table.entries[param_id].data.struct_type
                        break
            else:
                pi.node_type = None
            
            if pi.node_type not in all_nodes:
                all_nodes[pi.node_type]  = set()
                used_nodes[pi.node_type] = set()
                node_params[pi.node_type] = {}
            
            all_nodes[pi.node_type].update(i for i in range(len(path.graph_nodes)))
            node_params[pi.node_type].update({idx: node.node_param_id for idx, node in enumerate(path.graph_nodes)})
            
            # Convert the subgraphs
            for subgraph in path.subgraphs:
                si = SubgraphInterface()
                node_lookup = {}
                
                for i, node_id in enumerate(subgraph.node_id_list):
                    node_lookup[node_id] = i
                    used_nodes[pi.node_type].add(node_id)
                for node_id in subgraph.node_id_list:
                    node = path.graph_nodes[node_id]
                    
                    ni = NodeInterface()
                    ni.param_id = node.node_param_id
                    for edge_idx in node.next_edges:
                        edge = path.graph_edges[edge_idx]
                        ei = EdgeInterface()
                        ei.param_ids = edge.edge_param_ids
                        ei.next_node = node_lookup[edge.next_node]
                        ni.next_edges.append(ei)
                    si.nodes.append(ni)
                    
                pi.subgraphs.append(si)
            
            instance.path_graphs.append(pi)

        for param_type in all_nodes:
            this_all_nodes = all_nodes[param_type]
            this_used_nodes = used_nodes[param_type]
            this_node_params = node_params[param_type]
            
            unused_nodes = sorted(this_all_nodes.difference(this_used_nodes))
            for node_id in unused_nodes:
                ni = NodeInterface()
                ni.param_id = this_node_params[node_id]
                instance.loose_nodes.append(ni)

        for asset_entry in sorted(mxec_rw.asset_table.entries, key=lambda entry: entry.ID):
            ai = AssetInterface()
            folder_name = mxec_rw.sjis_strings.at_ptr(asset_entry.folder_name_ptr)
            file_name   = mxec_rw.sjis_strings.at_ptr(asset_entry.file_name_ptr)
            
            ai.ID = asset_entry.ID
            ai.filepath = folder_name + "/" + file_name
            ai.asset_type = asset_entry.filetype
            ai.unknown_id_1 = asset_entry.unknown_0x14
            ai.unknown_id_2 = asset_entry.unknown_0x24
            
            instance.assets.append(ai)
            
        return instance

    def to_subreader(self, depth):
        ot = OffsetTracker()
        mxec_rw = MXECReadWriter(endianness=">")
        
        sjis_strings = set()
        utf8_strings = set()
        unknowns     = set()
        sjis_string_lookup = dict()
        utf8_string_lookup = dict()
        unknowns_lookup    = dict()
        
        # Execute this in FIVE passes:
        # 1) First, construct the data structures you need,
        #    find the offsets of major sections,
        #    and fill in offsets of major sections
        # 2) Next, actually fill in the main data in those structures
        # 3) Collect POF0 data
        # 4) Collect ENRS data
        # 5) Collect CCRS data
        
        ######################################################################
        #                               PASS 1                               #
        ######################################################################
        # Generate data structures (also create all needed offsets?)
        # Would it not be better to include offset-linkage automatically inside
        # the read/write function definition?
        # -> Would then allow to you run read/write in another mode: Offset-generator
        mxec_rw.header.read_write(ot)
        mxec_rw.rw_fileinfo(ot)
        
        # Do Parameters
        mxec_rw.parameter_sets_table.entry_count = len(self.param_sets)
        mxec_rw.parameter_sets_table_ptr = ot.tell() if len(self.param_sets) else 0
        mxec_rw.parameter_sets_table.entries.data = [mxec_rw.parameter_sets_table.entry_cls(mxec_rw.context) for _ in range(mxec_rw.parameter_sets_table.entry_count)]
        
        def collect_param_strings(prw, param_set):     
            sjis_strings.update(set([param_set.parameters[nm] for nm in prw.sjis_vars]))
            utf8_strings.update(set([param_set.parameters[nm] for nm in prw.utf8_vars]))
            
            if "subparams" in prw.struct_obj:
                for param_name, param_type in prw.struct_obj["subparams"].items():
                    count = len(param_set.subparameters[param_name])
                    prw.data[param_type["count"]] = count
                    param_set.parameters[param_type["count"]] = count
                    
                    prw.init_subparam(param_name, param_type)
                    for sub_prw, sub_param_set in zip(prw.subparams[param_name], param_set.subparameters[param_name]):
                        collect_param_strings(sub_prw, sub_param_set)
        
        # 1) INTERATE THROUGH ENTITIES
        # 2) CREATE ENTITY STACK FOR EACH PARAM LINKED TO AN ENTITY
        # 3) ACCUMULATE STRING
        # 4) ADD STRING TO ARRAY
        # 5) LOOK UP STRING IN ARRAY WHEN IT NEEDS TO BE LOOKED UP
        parameter_name_prefixes = {}
        for entity in self.entities:
            parameter_name_prefixes.update(entity.get_all_param_prefixes())
        
        mxec_rw.parameter_sets_table.rw_fileinfo(ot)
        mxec_rw.parameter_sets_table.entry_ptr = ot.tell()
        
        param_names = []
        for i, param_set in enumerate(self.param_sets):
            type_prefix = param_set.param_type
            pset_name = ":".join([type_prefix, param_set.name])
            pset_name = parameter_name_prefixes.get(i, '') + pset_name
            sjis_strings.add(pset_name)
            param_names.append(pset_name)
        
        asset_offsets = []
        texmerge_offsets = []
        mxec_rw.parameter_sets_table.rw_entry_headers(ot)
        for param_set, prw in zip(self.param_sets, mxec_rw.parameter_sets_table.entries):
            prw.init_params(param_set.param_type)

            # Collect PVS, MergeFile, TextureMerge
            if param_set.param_type == "MxParameterPvs":
                if mxec_rw.pvs_record_ptr == 0:
                    mxec_rw.pvs_record_ptr = ot.tell()
                else:
                    assert 0, "More than one MxParameterPvs in MXE."
            elif param_set.param_type == "MxParameterMergeFile":
                if mxec_rw.mergefile_record_ptr == 0:
                    mxec_rw.mergefile_record_ptr = ot.tell()
                else:
                    assert 0, "More than one MxParameterMergeFile in MXE."
            elif param_set.param_type == "MxParameterTextureMerge":
                texmerge_offsets.append(ot.tell())

            # Get strings inside the parameters themselves
            collect_param_strings(prw.data, param_set)
            start_offset = ot.tell()
            
            for pname, ptype in zip(prw.data.data, prw.data.datatypes):
                endianness, typecode = ptype[0], ptype[1:]
                if typecode == "asset":
                    asset_offsets.append(ot.tell())
                prw.data.rw_element(ot, typecode, pname, endianness)
            
            prw.data_size = ot.tell() - start_offset
            if prw.data_size > 0:
                prw.data_offset = start_offset
                
            # Now rw subreaders
            struct_obj = prw.data.struct_obj
            for subparam_name, subparam_def in struct_obj.get("subparams", {}).items():
                prw.data.data[subparam_def["pointer"]] = ot.tell()
                param_set.parameters[subparam_def["pointer"]] = ot.tell()               
                prw.data.rw_subparam(ot, subparam_name, subparam_def)
            ot.align(ot.tell(), 0x10)
        
        ot.align(ot.tell(), 0x10)
        
        # Do Entities
        mxec_rw.entity_table_ptr = ot.tell() if len(self.entities) else 0
        if len(self.entities):
            mxec_rw.entity_table.entry_count = len(self.entities)
            mxec_rw.entity_table.entries.data = [EntityEntry(mxec_rw.context) for _ in range(mxec_rw.entity_table.entry_count)]
            
            ot.rw_obj_method(mxec_rw.entity_table, mxec_rw.entity_table.rw_fileinfo)
            mxec_rw.entity_table.entry_ptr = ot.tell()
            ot.rw_obj_method(mxec_rw.entity_table, mxec_rw.entity_table.rw_entry_headers)
            for i, (entity_rw, entity) in enumerate(zip(mxec_rw.entity_table.entries, self.entities)):
                sjis_strings.add(entity.name)
                entity_rw.data_offset = ot.tell()
                entity_rw.count = len(entity.all_flat_entities())
                
                if entity.unknown is not None:
                    unknowns.add(entity.unknown)
                    
                entity_rw.data = EntityData(entity_rw.count, entity_rw.context)
                entity_rw.data.subentries.data = [EntitySubEntry(entity_rw.data.context) for _ in range(entity_rw.count)]
                
                ot.rw_obj_method(entity_rw.data.subentries, entity_rw.data.subentries.read_write)
                
                entity_rw.data.data.data = []
                idx = 0
                ref_offset = ot.tell()
                
                for dec_rw, dec in zip(entity_rw.data.subentries, entity.all_flat_entities()[::-1]):
                    entity_rw.data.data.data.extend([0]*len(dec.parameters))
                    sjis_strings.add(dec.type)
                    dec_rw.count = len(dec.parameters)
                    dec_rw.offset = (ref_offset + idx*4) if dec_rw.count else 0

                    idx += dec_rw.count
                
                ot.rw_obj_method(entity_rw.data.data, entity_rw.data.data.read_write)
            
        ot.align(ot.tell(), 0x10)
        
        # Do Paths
        mxec_rw.pathing_table_ptr = ot.tell() if len(self.path_graphs) else 0
        if len(self.path_graphs):
            # First, collect all nodes from graphs of common types
            global_nodes = {}
            global_nodes_param_lookup = {}
            
            for node in self.loose_nodes:
                param_set = self.param_sets[node.param_id]
                if param_set.param_type not in global_nodes:
                    global_nodes[param_set.param_type] = []
                    global_nodes_param_lookup[param_set.param_type] = set()
                
                param_id = node.param_id
                if param_id in global_nodes_param_lookup[param_set.param_type]:
                    continue
                else:
                    global_nodes[param_set.param_type].append(node)
                    global_nodes_param_lookup[param_set.param_type].add(param_id)
            
            for graph in self.path_graphs:
                if graph.node_type not in global_nodes:
                    global_nodes[graph.node_type] = []
                    global_nodes_param_lookup[graph.node_type] = set()
                    
                for subgraph in graph.subgraphs:
                    for node in subgraph.nodes:
                        param_id = node.param_id
                        if param_id in global_nodes_param_lookup[graph.node_type]:
                            continue
                        else:
                            global_nodes[graph.node_type].append(node)
                            global_nodes_param_lookup[graph.node_type].add(param_id)
                    
            # Now sort the nodes by parameter ID
            global_nodes = {k: sorted(v, key=lambda x: x.param_id) for k, v in global_nodes.items()}
            param_id_to_node_idx_mappings = {k: {x.param_id: idx for idx, x in enumerate(v)} for k,v in global_nodes.items()}

            
            # Now each graph can be dumped using the global information, since
            # each graph actually lists all nodes of a given type and only
            # uses a subset of them..!
            for graph in self.path_graphs:
                param_id_to_node_idx_mapping = param_id_to_node_idx_mappings[graph.node_type]
                path_rw = PathingEntry(mxec_rw.pathing_table.context)
                sjis_strings.add(graph.name)
                
                local_node_idx = 0
                edge_idx = 0
                                                           
                # Create global nodes on each graph
                for node in global_nodes[graph.node_type]:
                    node_rw = PathNode(mxec_rw.pathing_table.context)
                    node_rw.node_param_id = node.param_id
                    path_rw.graph_nodes.append(node_rw)
                
                # Now collect the edges and create the subgraphs
                for subgraph in graph.subgraphs:
                    subgraph_rw = SubGraph(path_rw.context)
                    for node in subgraph.nodes:
                        global_node_idx = param_id_to_node_idx_mapping[node.param_id]
                        subgraph_rw.node_id_list.append(global_node_idx)
                        for edge in node.next_edges:
                            subgraph_rw.edge_id_list.append(edge_idx)
                           
                            next_node = subgraph.nodes[edge.next_node]
                            next_node_global_idx = param_id_to_node_idx_mapping[next_node.param_id]
                            
                            edge_rw = PathEdge(path_rw.context)
                            edge_rw.prev_node      = global_node_idx
                            edge_rw.next_node      = next_node_global_idx
                            edge_rw.edge_param_ids = sorted(edge.param_ids)
                            edge_rw.param_count    = len(edge.param_ids)
                            path_rw.graph_edges.append(edge_rw)
                        
                            path_rw.graph_nodes[global_node_idx].next_edges.append(edge_idx)
                            path_rw.graph_nodes[next_node_global_idx].prev_edges.append(edge_idx)
                        
                            edge_idx += 1
                        local_node_idx += 1
                        
                    for node_rw in path_rw.graph_nodes:
                        node_rw.next_edge_count = len(node_rw.next_edges)
                        node_rw.prev_edge_count = len(node_rw.prev_edges)
                        
                    for node_id in subgraph_rw.node_id_list:
                        node_rw = path_rw.graph_nodes[node_id]
                        if len(node_rw.prev_edges) == 0:
                            subgraph_rw.start_node_id_list.append(node_id)
                        if len(node_rw.next_edges) == 0:
                            subgraph_rw.end_node_id_list.append(node_id)
                    subgraph_rw.is_loop = (len(subgraph_rw.start_node_id_list) == 0) and (len(subgraph_rw.end_node_id_list) == 0)
                    
                    subgraph_rw.node_count       = len(subgraph_rw.node_id_list)
                    subgraph_rw.edge_count       = len(subgraph_rw.edge_id_list)
                    subgraph_rw.start_node_count = len(subgraph_rw.start_node_id_list)
                    subgraph_rw.end_node_count   = len(subgraph_rw.end_node_id_list)
                    
                    path_rw.subgraphs.append(subgraph_rw)
                    
                # Now register unused nodes
                # First we need to see which nodes *are* used
                for i, node_rw in enumerate(path_rw.graph_nodes):
                    if not(len(node_rw.prev_edges) or len(node_rw.next_edges)):
                        path_rw.unused_nodes.append(i)
                        
                path_rw.node_count        = len(path_rw.graph_nodes)
                path_rw.edge_count        = len(path_rw.graph_edges)
                path_rw.subgraphs_count   = len(path_rw.subgraphs)
                path_rw.unused_node_count = len(path_rw.unused_nodes)
                
                # Now we need to sort the edges by parameter
                sorted_edges = sorted([(i, edge) for i, edge in enumerate(path_rw.graph_edges)], key=lambda x: x[1].edge_param_ids)
                edge_mapping = {i: idx for idx, (i, edge) in enumerate(sorted_edges)}
                
                path_rw.graph_edges = [x[1] for x in sorted_edges]
                for node_rw in path_rw.graph_nodes:
                    node_rw.prev_edges = [edge_mapping[idx] for idx in node_rw.prev_edges]
                    node_rw.next_edges = [edge_mapping[idx] for idx in node_rw.next_edges]
                for subgraph_rw in path_rw.subgraphs:
                    subgraph_rw.edge_id_list = sorted([edge_mapping[idx] for idx in subgraph_rw.edge_id_list])
                
                mxec_rw.pathing_table.entries.data.append(path_rw)
                
            mxec_rw.pathing_table.entry_count = len(mxec_rw.pathing_table.entries)
            

            # Now that the structs have all been generated (phew!), let's calculate the offsets
            ot.rw_obj_method(mxec_rw.pathing_table, mxec_rw.pathing_table.rw_fileinfo_brt)
            mxec_rw.pathing_table.entry_ptr = ot.tell()
            for path_rw in mxec_rw.pathing_table.entries:
                ot.rw_obj(path_rw)
            for path_rw in mxec_rw.pathing_table.entries:
                # Do nodes
                if len(path_rw.graph_nodes):
                    path_rw.nodes_offset = ot.tell()
                    ot.rw_obj_method(path_rw, path_rw.rw_nodes)
                
                # Do edges
                if len(path_rw.graph_edges):
                    path_rw.edges_offset = ot.tell()
                    ot.rw_obj_method(path_rw, path_rw.rw_edges)
                
                # Now collect the node and edge data
                for node_rw in path_rw.graph_nodes:
                    if node_rw.next_edge_count:
                        node_rw.next_edge_list_offset = ot.tell()
                        ot.rw_obj_method(node_rw, node_rw.rw_next_edge_ids)
                    if node_rw.prev_edge_count:
                        node_rw.prev_edge_list_offset = ot.tell()
                        ot.rw_obj_method(node_rw, node_rw.rw_prev_edge_ids)    
                for edge_rw in path_rw.graph_edges:
                    if len(edge_rw.edge_param_ids):
                        edge_rw.param_list_offset = ot.tell()
                        ot.rw_obj_method(edge_rw, edge_rw.rw_param_ids)
                ot.align(ot.tell(), 0x10)
                
                # Do subgraphs
                if len(path_rw.subgraphs):
                    path_rw.subgraphs_offset = ot.tell()
                    ot.rw_obj_method(path_rw, path_rw.rw_subgraphs)
                    for subgraph_rw in path_rw.subgraphs:
                        if len(subgraph_rw.node_id_list):
                            subgraph_rw.node_list_offset = ot.tell()
                            ot.rw_obj_method(subgraph_rw, subgraph_rw.rw_node_id_list)
                        if len(subgraph_rw.edge_id_list):
                            subgraph_rw.edge_list_offset = ot.tell()
                            ot.rw_obj_method(subgraph_rw, subgraph_rw.rw_edge_id_list)
                        if len(subgraph_rw.end_node_id_list):
                            subgraph_rw.end_node_offset = ot.tell()
                            ot.rw_obj_method(subgraph_rw, subgraph_rw.rw_end_node_ids)
                        if len(subgraph_rw.start_node_id_list):
                            subgraph_rw.start_node_offset = ot.tell()
                            ot.rw_obj_method(subgraph_rw, subgraph_rw.rw_start_node_ids)
                    
                # Do unused nodes
                if len(path_rw.unused_nodes):
                    path_rw.unused_nodes_offset = ot.tell()
                    ot.rw_obj_method(path_rw, path_rw.rw_unused_nodes)
        
                ot.align(ot.tell(), 0x10)
                
        # Do Assets
        mxec_rw.asset_table_ptr = ot.tell() if len(self.assets) else 0
        if len(self.assets):
            ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_fileinfo)
            mxec_rw.asset_table.asset_references_offset = ot.tell()
            mxec_rw.asset_table.asset_references_count = len(self.assets)
            mxec_rw.asset_table.init_structs()
            ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_entry_headers)
            for asset in self.assets:
                folder_name, file_name = asset.filepath.rsplit('/', 1)
                sjis_strings.add(folder_name)
                sjis_strings.add(file_name)
            
            mxec_rw.asset_table.asset_use_offset = ot.tell()
            mxec_rw.asset_table.asset_use_count = len(asset_offsets)
            ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_asset_slot_offsets)

        # Do texmerge ptrs
        if len(texmerge_offsets):
            mxec_rw.texmerge_ptrs_ptr = ot.tell()
            mxec_rw.texmerge_ptr = texmerge_offsets
            mxec_rw.texmerge_count = len(texmerge_offsets)
            ot.seek(ot.tell() + 4*len(texmerge_offsets))
        ot.align(ot.tell(), 0x10)
        
        # Do Strings
        for i, string_val in enumerate(sorted(sjis_strings)):
            str_bytes = string_val.encode("cp932")
            offset = ot.tell()
            sjis_string_lookup[string_val] = offset
            ot.seek(offset + len(str_bytes) + 1)
        ot.align(ot.tell(), 0x10)
        for i, string_val in enumerate(sorted(utf8_strings)):
            try:
                str_bytes = string_val.encode("cp932")
            except Exception:
                str_bytes = string_val.encode("utf8")
            offset = ot.tell()
            utf8_string_lookup[string_val] = offset
            ot.seek(offset + len(str_bytes) + 1)
        ot.align(ot.tell(), 0x10)
        
        # Do Unknowns
        for i, unknowns_val in enumerate(sorted(unknowns, key=lambda x: struct.unpack('<Q', struct.pack('>Q', x)))):
            offset = ot.tell()
            unknowns_lookup[unknowns_val] = offset
            ot.seek(offset + 8)
        ot.align(ot.tell(), 0x10)
        
        # Clean up header
        mxec_rw.header.flags = 0x18000000
        mxec_rw.header.data_length = ot.tell() - mxec_rw.header.header_length
        mxec_rw.header.depth = depth
        
        mxec_rw.content_flags +=                                  1 * 0x00000100
        mxec_rw.content_flags +=    (mxec_rw.texmerge_ptrs_ptr > 0) * 0x00000400
        mxec_rw.content_flags +=       (mxec_rw.pvs_record_ptr > 0) * 0x00001800
        mxec_rw.content_flags += (mxec_rw.mergefile_record_ptr > 0) * 0x01000000
        
        ######################################################################
        #                               PASS 2                               #
        ######################################################################
        # Fill in data
        
        # Fill in Parameter Sets
        def fill_param_strings(prw_data, param_set, sjis_lookup, utf8_lookup):
            for param_name, param_type in zip(prw_data.data, prw_data.datatypes):
                if param_type[1:] == "sjis_string":
                    prw_data.data[param_name] = sjis_lookup[param_set.parameters[param_name]]
                elif param_type[1:] == "utf8_string":
                    prw_data.data[param_name] = utf8_lookup[param_set.parameters[param_name]]
                elif param_type[1:] in set(["pad8", "pad16", "pad32", "pad64"]):
                    prw_data.data[param_name] = 0
                elif param_type[1:] == "pointer32":
                    pass # Should have already been handled
                else:
                    prw_data.data[param_name] = param_set.parameters[param_name]
            
            for param_name in param_set.subparameters:
                for sub_prw, sub_param_set in zip(prw_data.subparams[param_name], param_set.subparameters[param_name]):
                    fill_param_strings(sub_prw, sub_param_set, sjis_lookup, utf8_lookup)
        
        for i, (prw, param_set, param_set_name) in enumerate(zip(mxec_rw.parameter_sets_table.entries, self.param_sets, param_names)):
            prw.ID = i
            prw.name_offset = sjis_string_lookup[param_set_name]
            fill_param_strings(prw.data, param_set, sjis_string_lookup, utf8_string_lookup)
            
        # Entities
        for entity_rw, entity in zip(mxec_rw.entity_table.entries, self.entities):
            entity_rw.ID = entity.ID
            entity_rw.name_offset = sjis_string_lookup[entity.name]
            entity_rw.controller_entity_id = entity.controller_id
            entity_rw.has_unknown_data     = (entity.unknown is not None)
            entity_rw.unknown_data_ptr = unknowns_lookup[entity.unknown] if entity_rw.has_unknown_data else 0
            
            idx = 0
            for dec_rw, dec in zip(entity_rw.data.subentries, entity.all_flat_entities()[::-1]):
                dec_rw.name_offset = sjis_string_lookup[dec.type]
                for param in dec.parameters:
                    entity_rw.data.data.data[idx] = param.param_id
                    idx += 1
        # Paths
        for path_rw, path in zip(mxec_rw.pathing_table.entries, self.path_graphs):
            path_rw.name_offset = sjis_string_lookup[path.name]
        
        # Assets
        for i, asset in enumerate(self.assets):
            entry = mxec_rw.asset_table.entries[i]
            folder_name, file_name = asset.filepath.rsplit('/', 1)
            
            entry.flags           = 0x100 * (asset.unknown_id_1 > -1) + 0x200 * (asset.unknown_id_2 > -1)
            entry.ID              = i
            entry.folder_name_ptr = sjis_string_lookup[folder_name]
            entry.file_name_ptr   = sjis_string_lookup[file_name]
            entry.filetype        = asset.asset_type
            
            entry.unknown_0x14    = asset.unknown_id_1
            entry.unknown_0x20    = (asset.unknown_id_1 > -1) - 1
            entry.unknown_0x24    = asset.unknown_id_2
            
        mxec_rw.asset_table.asset_slot_offsets = asset_offsets
            
        # Strings
        for string_val, offset in sjis_string_lookup.items():
            idx = len(mxec_rw.sjis_strings)
            mxec_rw.sjis_strings.data.append(string_val)
            mxec_rw.sjis_strings.ptr_to_idx[offset] = idx
            mxec_rw.sjis_strings.idx_to_ptr[idx] = offset
        for string_val, offset in utf8_string_lookup.items():
            idx = len(mxec_rw.utf8_strings)
            mxec_rw.utf8_strings.data.append(string_val)
            mxec_rw.utf8_strings.ptr_to_idx[offset] = idx
            mxec_rw.utf8_strings.idx_to_ptr[idx] = offset
        
        # Unknowns
        for unknown, offset in unknowns_lookup.items():
            idx = len(mxec_rw.unknowns)
            mxec_rw.unknowns.data.append(unknown)
            mxec_rw.unknowns.ptr_to_idx[offset] = idx
            mxec_rw.unknowns.idx_to_ptr[idx] = offset
            
        
        ######################################################################
        #                               PASS 3                               #
        ######################################################################
        # POF0
        
        # Create POF0 data
        pb = POF0Builder()
        pb.virtual_offset = mxec_rw.header.header_length
        mxec_rw.read_write_contents(pb)
        
        pb_data = compressPOF0(pb.pointers)
        mxec_rw.POF0.data_size = len(pb_data) + 4
        mxec_rw.POF0.data = pb_data
        
        # Create POF0 header data
        pb_ot = OffsetTracker()
        mxec_rw.POF0.read_write_contents(pb_ot)
        
        mxec_rw.POF0.header.flags = 0x10000000
        mxec_rw.POF0.header.depth = depth + 1
        mxec_rw.POF0.header.data_length = pb_ot.tell()
        mxec_rw.POF0.header.contents_length = pb_ot.tell()
        
        mxec_rw.POF0.read_write(ot)
        
        ######################################################################
        #                               PASS 4                               #
        ######################################################################
        # ENRS
        # Create POF0 data
        eb = ENRSBuilder(mxec_rw.context.endianness)
        eb.anchor_pos = -mxec_rw.header.header_length
        mxec_rw.read_write_contents(eb)
        
        eb_rawdata = toENRSPackedRep(eb.pointers)
        eb_data = compressENRS(eb_rawdata)
        mxec_rw.ENRS.num_groups = len(eb.pointers)
        mxec_rw.ENRS.data = eb_data
        
        # Create ENRS header data
        mxec_rw.ENRS.header.data_length = len(eb_data) + 0x10
        mxec_rw.ENRS.header.contents_length = len(eb_data) + 0x10
        
        mxec_rw.ENRS.header.flags = 0x10000000
        mxec_rw.ENRS.header.depth = depth + 1
        
        mxec_rw.ENRS.read_write(ot)
        
        ######################################################################
        #                               PASS 5                               #
        ######################################################################
        # CCRS
        cb = CCRSBuilder()
        cb.anchor_pos = -mxec_rw.header.header_length
        mxec_rw.read_write_contents(cb)
        
        cb_rawdata = toCCRSPackedRep(cb.pointers)
        cb_data = compressCCRS(cb_rawdata)
        mxec_rw.CCRS.num_groups = len(cb.pointers)
        mxec_rw.CCRS.data = cb_data
        
        # Create CCRS header data
        mxec_rw.CCRS.header.data_length = len(cb_data) + 0x10
        mxec_rw.CCRS.header.contents_length = len(cb_data) + 0x10
        
        mxec_rw.CCRS.header.flags = 0x10000000
        mxec_rw.CCRS.header.depth = depth + 1
        
        mxec_rw.CCRS.read_write(ot)
        
        ######################################################################
        #                              CLEANUP                               #
        ######################################################################
        # Finish with EOFC
        mxec_rw.EOFC.header.flags           = 0x10000000
        mxec_rw.EOFC.header.depth           = depth + 1
        mxec_rw.EOFC.header.data_length     = 0
        mxec_rw.EOFC.header.contents_length = 0
        
        mxec_rw.header.contents_length = ot.tell()
        
        return mxec_rw
