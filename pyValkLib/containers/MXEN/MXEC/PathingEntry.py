from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray


class PathingEntry(Serializable):
    __slots__ = ("name_offset", "graph_edges", "unused_nodes",
                 "node_count", "nodes_offset", "graph_nodes",
                 "edge_count", "edges_offset",
                 "subgraphs_count", "subgraphs_offset", "subgraphs",
                 "unused_node_count", "unused_nodes_offset",
                 "padding_0x24", "padding_0x28", "padding_0x2C",
                 "padding_0x30", "padding_0x34", "padding_0x38", "padding_0x3C")

    def __init__(self, context):
        super().__init__(context)
        self.name_offset = 0
        self.node_count  = 0
        self.nodes_offset = 0
        self.edge_count  = 0
        self.edges_offset = 0
        self.subgraphs_count  = 0
        self.subgraphs_offset = 0
        self.unused_node_count  = 0
        self.unused_nodes_offset = 0
        
        self.padding_0x24 = 0
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.padding_0x30 = 0
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0

        self.graph_nodes  = []
        self.graph_edges  = []
        self.subgraphs    = []
        self.unused_nodes = []

    def __repr__(self):
        out = "<PathingEntry>\n"
        out += f"Name Offset: {self.name_offset}\n"
        out += f"Node Count/Offset: {self.node_count}/{self.nodes_offset}\n"
        out += f"Edge Count/Offset: {self.edge_count}/{self.edges_offset}\n"
        out += f"Subgraph Count/Offset: {self.subgraphs_count}/{self.subgraphs_offset}\n"
        out += f"Unused Count/Offset: {self.unused_node_count}/{self.unused_nodes_offset}\n"
        out += "</PathingEntry>"
        
        return out
        
    def read_write(self, rw):
        rw.mark_new_contents_array()
        
        self.name_offset  = rw.rw_pointer(self.name_offset)
        self.node_count   = rw.rw_uint32(self.node_count)
        self.nodes_offset = rw.rw_pointer(self.nodes_offset)
        self.edge_count   = rw.rw_uint32(self.edge_count)
        
        self.edges_offset      = rw.rw_pointer(self.edges_offset)
        self.subgraphs_count   = rw.rw_uint32(self.subgraphs_count)
        self.subgraphs_offset  = rw.rw_pointer(self.subgraphs_offset)
        self.unused_node_count = rw.rw_uint32(self.unused_node_count)
        
        self.unused_nodes_offset = rw.rw_pointer(self.unused_nodes_offset)
        self.padding_0x24        = rw.rw_pad32(self.padding_0x24)
        self.padding_0x28        = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C        = rw.rw_pad32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)

        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)

    def rw_data(self, rw):
        if self.nodes_offset:
            rw.assert_local_file_pointer_now_at("Node Headers:", self.nodes_offset)
            rw.rw_obj_method(self, self.rw_nodes)

        if self.edges_offset:
            rw.assert_local_file_pointer_now_at("Edge Headers:", self.edges_offset)
            rw.rw_obj_method(self, self.rw_edges)

        for node in self.graph_nodes:
            if node.next_edge_list_offset:
                rw.assert_local_file_pointer_now_at("Node Next Edges:", node.next_edge_list_offset)
                rw.rw_obj_method(node, node.rw_next_edge_ids)
            if node.prev_edge_list_offset:
                rw.assert_local_file_pointer_now_at("Node Prev Edges:", node.prev_edge_list_offset)
                rw.rw_obj_method(node, node.rw_prev_edge_ids)

        for edge in self.graph_edges:
            if edge.param_list_offset:
                rw.assert_local_file_pointer_now_at("Graph Edge Parameter List:", edge.param_list_offset)
                rw.rw_obj_method(edge, edge.rw_param_ids)

        rw.align(rw.local_tell(), 0x10)

        if self.subgraphs_offset:
            rw.assert_local_file_pointer_now_at("Subgraphs:", self.subgraphs_offset)
            rw.rw_obj_method(self, self.rw_subgraphs)
            for subgraph in self.subgraphs:
                if subgraph.node_list_offset:
                    rw.assert_local_file_pointer_now_at("Subgraph Nodes:", subgraph.node_list_offset)
                rw.rw_obj_method(subgraph, subgraph.rw_node_id_list)
                if subgraph.edge_list_offset:
                    rw.assert_local_file_pointer_now_at("Subgraph Edges:", subgraph.edge_list_offset)
                rw.rw_obj_method(subgraph, subgraph.rw_edge_id_list)
                if subgraph.end_node_offset:
                    rw.assert_local_file_pointer_now_at("Subgraph End Nodes:", subgraph.end_node_offset)
                rw.rw_obj_method(subgraph, subgraph.rw_end_node_ids)
                if subgraph.start_node_offset:
                    rw.assert_local_file_pointer_now_at("Subgraph Start Nodes:", subgraph.start_node_offset)
                rw.rw_obj_method(subgraph, subgraph.rw_start_node_ids)

        if self.unused_nodes_offset:
            rw.assert_local_file_pointer_now_at("Unused Graph Nodes:", self.unused_nodes_offset)
            rw.rw_obj_method(self, self.rw_unused_nodes)

        rw.align(rw.local_tell(), 0x10)

    def rw_nodes(self, rw):
        if rw.mode() == "read":
            self.graph_nodes = [PathNode(self.context) for _ in range(self.node_count)]
        for node in self.graph_nodes:
            rw.rw_obj(node)

    def rw_edges(self, rw):
        if rw.mode() == "read":
            self.graph_edges = [PathEdge(self.context) for _ in range(self.edge_count)]
        for edge in self.graph_edges:
            rw.rw_obj(edge)

    def rw_subgraphs(self, rw):
        if rw.mode() == "read":
            self.subgraphs = [SubGraph(self.context) for _ in range(self.subgraphs_count)]
        for subgraph in self.subgraphs:
            rw.rw_obj(subgraph)

    def rw_unused_nodes(self, rw):
        self.unused_nodes = rw.rw_uint32s(self.unused_nodes, self.unused_node_count)

        
class PathNode(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.next_edge_count       = 0
        self.next_edge_list_offset = 0
        self.prev_edge_count       = 0
        self.prev_edge_list_offset = 0
        self.node_param_id = 0
        self.padding_0x14  = 0
        self.padding_0x18  = 0
        self.padding_0x1C  = 0
        
        self.next_edges = []
        self.prev_edges = []
        
    def __eq__(self, other):
        res = True
        res &= self.next_edge_count       == other.next_edge_count
        res &= self.next_edge_list_offset == other.next_edge_list_offset
        res &= self.prev_edge_count       == other.prev_edge_count
        res &= self.prev_edge_list_offset == other.prev_edge_list_offset
        res &= self.node_param_id         == other.node_param_id
        res &= all(e1 == e2 for e1, e2 in zip(self.next_edges, other.next_edges))
        res &= all(e1 == e2 for e1, e2 in zip(self.prev_edges, other.prev_edges))
        
        return res
        
    def __repr__(self):
        open_tag   = "<PathNode>\n"
        elem_1     = f"Next Edge Count/Offset: {self.next_edge_count}/{self.next_edge_list_offset}\n"
        elem_2     = f"Prev Edge Count/Offset: {self.prev_edge_count}/{self.prev_edge_list_offset}\n"
        param      = f"Param: {self.node_param_id}\n"
        next_edges = f"Next Edges: {', '.join([str(elem) for elem in self.next_edges])}\n"
        prev_edges = f"Prev Edges: {', '.join([str(elem) for elem in self.prev_edges])}\n"
        close_tag  = "</PathNode>"

        return open_tag + elem_1 + elem_2 + param + next_edges + prev_edges + close_tag

    def read_write(self, rw):
        self.next_edge_count       = rw.rw_uint32(self.next_edge_count)
        self.next_edge_list_offset = rw.rw_pointer(self.next_edge_list_offset)
        self.prev_edge_count       = rw.rw_uint32(self.prev_edge_count)
        self.prev_edge_list_offset = rw.rw_pointer(self.prev_edge_list_offset)
        
        self.node_param_id = rw.rw_uint32(self.node_param_id)
        self.padding_0x14  = rw.rw_pad32(self.padding_0x14)
        self.padding_0x18  = rw.rw_pad32(self.padding_0x18)
        self.padding_0x1C  = rw.rw_pad32(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
    def rw_next_edge_ids(self, rw):
        rw.assert_local_file_pointer_now_at("PathNode: Previous Edges: ", self.next_edge_list_offset)
        self.next_edges = rw.rw_uint32s(self.next_edges, self.next_edge_count)
        
    def rw_prev_edge_ids(self, rw):
        rw.assert_local_file_pointer_now_at("PathNode: Next Edges:", self.prev_edge_list_offset)
        self.prev_edges = rw.rw_uint32s(self.prev_edges, self.prev_edge_count)
        

class PathEdge(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.prev_node         = 0
        self.next_node         = 0
        self.param_count       = 0
        self.param_list_offset = 0
        self.edge_param_ids    = []
    
    def __repr__(self):
        open_tag = "<PathEdge>\n"
        line_1    = f"  Prev Node: {self.prev_node} Next Node: {self.next_node}\n"
        line_2    = f"  Param Count/Offset: {self.param_count}/{self.param_list_offset}\n"
        line_3    = f"  Param IDs: {self.edge_param_ids}\n"
        close_tag = "</PathEdge>"
        
        return open_tag + line_1 + line_2 + line_3 + close_tag
    
    def read_write(self, rw):     
        self.prev_node         = rw.rw_uint32(self.prev_node)
        self.next_node         = rw.rw_uint32(self.next_node)
        self.param_count       = rw.rw_uint32(self.param_count)
        self.param_list_offset = rw.rw_pointer(self.param_list_offset)
        
        rw.assert_equal(self.param_count, self.param_list_offset > 0)

    def rw_param_ids(self, rw):
        rw.assert_local_file_pointer_now_at("Path Edges: ", self.param_list_offset)
        self.edge_param_ids = rw.rw_uint32s(self.edge_param_ids, self.param_count)


class SubGraph(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.node_count        = 0
        self.node_list_offset  = 0
        self.edge_count        = 0
        self.edge_list_offset  = 0
        self.start_node_count  = 0
        self.start_node_offset = 0
        self.end_node_count    = 0
        self.end_node_offset   = 0
        
        self.is_loop      = 0
        self.padding_0x24 = 0
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.padding_0x30 = 0
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0
        
        self.node_id_list       = []
        self.edge_id_list       = []
        self.start_node_id_list = []
        self.end_node_id_list   = []
    
    def read_write(self, rw):
        self.node_count       = rw.rw_uint32(self.node_count)
        self.node_list_offset = rw.rw_pointer(self.node_list_offset)
        self.edge_count       = rw.rw_uint32(self.edge_count)
        self.edge_list_offset = rw.rw_pointer(self.edge_list_offset)
        
        self.end_node_count    = rw.rw_uint32(self.end_node_count)
        self.end_node_offset   = rw.rw_pointer(self.end_node_offset)
        self.start_node_count  = rw.rw_uint32(self.start_node_count)
        self.start_node_offset = rw.rw_pointer(self.start_node_offset)
        
        self.is_loop      = rw.rw_uint32(self.is_loop)
        self.padding_0x24 = rw.rw_pad32(self.padding_0x24)
        self.padding_0x28 = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C = rw.rw_pad32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)
        
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)

    def rw_node_id_list(self, rw):
        self.node_id_list = rw.rw_uint32s(self.node_id_list, self.node_count)
        
    def rw_edge_id_list(self, rw):
        self.edge_id_list = rw.rw_uint32s(self.edge_id_list, self.edge_count)
        
    def rw_end_node_ids(self, rw):
        self.end_node_id_list = rw.rw_uint32s(self.end_node_id_list, self.end_node_count)
        
    def rw_start_node_ids(self, rw):
        self.start_node_id_list = rw.rw_uint32s(self.start_node_id_list, self.start_node_count)
        
