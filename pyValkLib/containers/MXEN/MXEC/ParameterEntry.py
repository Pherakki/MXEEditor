import json
import os
from pyValkLib.serialisation.Serializable import Serializable


param_structs = {}
struct_path = os.path.abspath("pyValkLib/configuration/MXE/Parameters")
for file in os.listdir(struct_path):
    filename, fileext = os.path.splitext(file)
    if fileext == ".json":
        filepath = os.path.join(struct_path, file)
        with open(filepath, 'r') as F:
            try:
                param_structs[filename] = json.load(F)
            except Exception as e:
                print("Failed to load", filename)
                raise e
            if "struct" not in param_structs[filename]:
                raise Exception(f"Invalid structure file {filename}: No 'struct' member.")

def handle_pad(rw, x, func):
    val = func(x)
    rw.assert_is_zero(val)
    return val

func_lookup = {
    "int8"       : lambda rw, x, en: rw.rw_int8(x, endianness=en),
    "int16"      : lambda rw, x, en: rw.rw_int16(x, endianness=en),
    "int32"      : lambda rw, x, en: rw.rw_int32(x, endianness=en),
    "int64"      : lambda rw, x, en: rw.rw_int64(x, endianness=en),  
    "uint8"      : lambda rw, x, en: rw.rw_uint8(x, endianness=en),
    "uint16"     : lambda rw, x, en: rw.rw_uint16(x, endianness=en),
    "uint32"     : lambda rw, x, en: rw.rw_uint32(x, endianness=en),
    "uint64"     : lambda rw, x, en: rw.rw_uint64(x, endianness=en),
    "hex8"       : lambda rw, x, en: rw.rw_hex8(x, endianness=en),
    "hex16"      : lambda rw, x, en: rw.rw_hex16(x, endianness=en),
    "hex32"      : lambda rw, x, en: rw.rw_hex32(x, endianness=en),
    "hex64"      : lambda rw, x, en: rw.rw_hex64(x, endianness=en),
    "float16"    : lambda rw, x, en: rw.rw_float16(x, endianness=en),
    "float32"    : lambda rw, x, en: rw.rw_float32(x, endianness=en),
    "float64"    : lambda rw, x, en: rw.rw_float64(x, endianness=en),
    "pad8"       : lambda rw, x, en: handle_pad(rw, x, rw.rw_pad8),
    "pad16"      : lambda rw, x, en: handle_pad(rw, x, rw.rw_pad16),
    "pad32"      : lambda rw, x, en: handle_pad(rw, x, rw.rw_pad32),
    "pad64"      : lambda rw, x, en: handle_pad(rw, x, rw.rw_pad64),
    "path"       : lambda rw, x, en: rw.rw_int32(x, endianness=en),
    "asset"      : lambda rw, x, en: rw.rw_int64(x, endianness=en),
    "pointer32"  : lambda rw, x, en: rw.rw_pointer(x, endianness=en),
    "utf8_string": lambda rw, x, en: rw.rw_pointer(x, endianness=en),
    "sjis_string": lambda rw, x, en: rw.rw_pointer(x, endianness=en),
    "color32"    : lambda rw, x, en: rw.rw_color32(x, endianness=en),
    "color128"   : lambda rw, x, en: rw.rw_color128(x, endianness=en)
}

class ParameterSet(Serializable):
    def __init__(self, context, struct_type):
        super().__init__(context)
        self.struct_type = struct_type
        self.struct_obj = param_structs[struct_type]
        self.data = {}
        self.subparams = {}
        self.datatypes = []
        self.sjis_vars = []
        self.utf8_vars = []
        self.asset_vars = []
        
        if "struct" in self.struct_obj:
            for param_chunk in self.struct_obj["struct"]:
                for k, v in param_chunk.items():
                    if type(v) is not str:
                        raise Exception(f"Parameter names must be strings, found {v} (type: {type(v)}).")
                    self.data[k] = None
                    self.datatypes.append(v)
                    
                    if v[1:] == "utf8_string":
                        self.utf8_vars.append(k)
                    elif v[1:] == "sjis_string":
                        self.sjis_vars.append(k)
                    elif v[1:] == "asset":
                        self.asset_vars.append(k)
        
    def init_subparams(self):
        if "subparams" in self.struct_obj:
            for k, v in self.struct_obj["subparams"].items():
                if type(v) is dict:
                    self.init_subparam(k, v)
        
    def init_subparam(self, k, ktype):
        count = self.data[ktype["count"]]
        self.subparams[k] = [ParameterSet(self.context, ktype["type"]) for _ in range(count)]
        
    def read_write(self, rw):
        self.rw_struct(rw)
        self.rw_subparams(rw)
        
    def rw_element(self, rw, typecode, k, endianness):
        self.data[k] = func_lookup[typecode](rw, self.data[k], endianness)
        
    def rw_struct(self, rw):
        for param_chunk in self.struct_obj["struct"]:
            rw.mark_new_contents_array()
            rw.mark_new_contents_array_member()
            
            for k, ktype in param_chunk.items():
                try:
                    endianness, typecode = ktype[0], ktype[1:]
                    self.rw_element(rw, typecode, k, endianness)
                except Exception as e:
                    print("Failed to handle", k, "for", self.struct_type)
                    raise e
                
    def rw_subparams(self, rw):
        if rw.mode() == "read":
            self.init_subparams()
        for subparam_name, subparam_def in self.struct_obj.get("subparams", {}).items():
            self.rw_subparam(rw, subparam_name, subparam_def)
                
    def rw_subparam(self, rw, subparam_name, subparam_def):
        ptr = self.data[subparam_def["pointer"]]
        rw.assert_local_file_pointer_now_at(f"{subparam_def['type']} Member {subparam_name}", ptr)
        for param in self.subparams[subparam_name]:
            rw.rw_obj(param)
                
    def asset_table_offsets(self):
        return [self.data[k] for k in self.asset_vars]
    
    def get_string_ptrs(self):
        return [self.data[k] for k in self.utf8_vars]
    
    def get_shiftjis_string_ptrs(self):
        return [self.data[k] for k in self.sjis_vars]

class ParameterEntry(Serializable):
    __slots__ = ("name", "ID", "name_offset", "data_size", "data_offset", "parameter_type", "data")

    def __init__(self, context):
        super().__init__(context)
        self.ID = 0
        self.name_offset = 0
        self.data_size = 0
        self.data_offset = 0
        
        self.parameter_type = None
        
        self.data = None
        
    def init_params(self, param_type):
        self.data = ParameterSet(self.context, param_type)
        
    def read_write(self, rw):
        self.ID          = rw.rw_uint32(self.ID)
        self.name_offset = rw.rw_pointer(self.name_offset)
        self.data_size   = rw.rw_uint32(self.data_size)
        self.data_offset = rw.rw_pointer(self.data_offset)
        
    def rw_data(self, rw, lookup_name):
        if rw.mode() == "read":
            self.init_params(lookup_name)
        rw.rw_obj(self.data)
        rw.align(rw.local_tell(), 0x10)
