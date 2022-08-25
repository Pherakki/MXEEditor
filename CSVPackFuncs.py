import struct

class ExceptionMessageGenerator(Exception):
    __slots__ = ("error_msg",)
    
    def __init__(self, error_msg):
        super().__init__()
        self.error_msg = error_msg

    def generate_exception_msg(self):
        return self.error_msg

def stoi(val):
    try:
        int_val = int(val)
    except Exception as e:
        raise ExceptionMessageGenerator(f"'{val}' cannot be interpreted as an integer.") from e
    return int_val

def hstoi(val):
    try:
        int_val = int(val, 16)
    except Exception as e:
        raise ExceptionMessageGenerator(f"'{val}' is not a valid hexadecimal string.") from e
    return int_val    

def stof(val):
    try:
        float_val = float(val)
    except Exception as e:
        raise ExceptionMessageGenerator(f"'{val}' cannot be interpreted as a float.") from e
    return float_val

type_strings = {
    "B": "an unsigned 8-bit integer",
    "H": "an unsigned 16-bit integer",
    "I": "an unsigned 32-bit integer",
    "Q": "an unsigned 64-bit integer",
    "b": "a signed 8-bit integer",
    "h": "a signed 16-bit integer",
    "i": "a signed 32-bit integer",
    "q": "a signed 64-bit integer",
    "e": "a 16-bit float",
    "f": "a 32-bit float",
    "d": "a 64-bit float"
}

def repack_int(val, condition):
    int_val = stoi(val)
    try:
        struct.pack(condition, int_val)
    except Exception as e:
        raise ExceptionMessageGenerator(f"'{val}' cannot be serialized to a {type_strings[condition]}.") from e
    return int_val

def repack_hex(val, condition):
    if val[:2] != "0x":
        raise ExceptionMessageGenerator(f"'{val}' is not a valid hex string: must begin with '0x'.")
    
    int_val = hstoi(val)
    try:
        struct.pack(condition, int_val)
    except Exception as e:
        raise ExceptionMessageGenerator(f"the hex string '{val}' cannot be serialized to a {type_strings[condition]}.") from e
    return val

def repack_float(val, condition):
    float_val = stof(val)
    try:
        struct.pack(condition, float_val)
    except Exception as e:
        raise ExceptionMessageGenerator(f"'{val}' cannot be serialized to a {type_strings[condition]}.") from e
    return float_val

def repack_pad(val):
    int_val = stoi(val)
    if not (int_val == 0):
        raise ExceptionMessageGenerator(f"'{val}' is a padding value and must be 0.")
    
    return int_val

def repack_color32(color_val):
    values = color_val.split(" ")
    values = [val.strip() for val in values if len(val)]
    
    good_values = [0, 0, 0, 0]
    bad_values = []
    for i, val in enumerate(values):
        try:
            int_val = stoi(val)
            good_values[i] = int_val
        except Exception:
            bad_values.append((i, val))
    if len(bad_values):
        raise ExceptionMessageGenerator(f"the color32 '{color_val}' components "
                                        f"{', '.join(v[0] for v in bad_values)}"
                                        f"could not be interpreted as integers."
        )
        
    unpackable_values = []
    for i, val in enumerate(good_values):
        try:
            struct.pack('B', val)
        except Exception:
            unpackable_values.append((i, val))
    if len(unpackable_values):
        raise ExceptionMessageGenerator(f"the color32 '{color_val}' components "
                                        f"{', '.join(v[0] for v in unpackable_values)}"
                                        f"could not be serialised as unsigned 8-bit integers."
        )
        
    return good_values

def repack_color128(color_val):
    values = color_val.split(" ")
    values = [val.strip() for val in values if len(val)]
    
    good_values = [0, 0, 0, 0]
    bad_values = []
    for i, val in enumerate(values):
        try:
            float_val = stof(val)
            good_values[i] = float_val
        except Exception:
            bad_values.append((i, val))
    if len(bad_values):
        raise ExceptionMessageGenerator(f"the color128 '{color_val}' components "
                                        f"{', '.join(v[0] for v in bad_values)}"
                                        f"could not be interpreted as floats."
        )
        
    unpackable_values = []
    for i, val in enumerate(good_values):
        try:
            struct.pack('f', val)
        except Exception:
            unpackable_values.append((i, val))
    if len(unpackable_values):
        raise ExceptionMessageGenerator(f"the color128 '{color_val}' components "
                                        f"{', '.join(v[0] for v in unpackable_values)}"
                                        f"could not be serialised as 32-bit floats."
        )
        
    return good_values


repack_funcs = {
    "int8"       : lambda x: repack_int(x, "b"),
    "int16"      : lambda x: repack_int(x, "h"),
    "int32"      : lambda x: repack_int(x, "i"),
    "int64"      : lambda x: repack_int(x, "q"), 
    "uint8"      : lambda x: repack_int(x, "B"),
    "uint16"     : lambda x: repack_int(x, "H"),
    "uint32"     : lambda x: repack_int(x, "I"),
    "uint64"     : lambda x: repack_int(x, "Q"),
    "hex8"       : lambda x: repack_hex(x, "B"),
    "hex16"      : lambda x: repack_hex(x, "H"),
    "hex32"      : lambda x: repack_hex(x, "I"),
    "hex64"      : lambda x: repack_hex(x, "Q"),
    "float16"    : lambda x: repack_float(x, "e"),
    "float32"    : lambda x: repack_float(x, "f"),
    "float64"    : lambda x: repack_float(x, "d"),
    "pad8"       : lambda x: repack_pad(x),
    "pad16"      : lambda x: repack_pad(x),
    "pad32"      : lambda x: repack_pad(x),
    "pad64"      : lambda x: repack_pad(x),
    "path"       : lambda x: repack_int(x, "i"),
    "asset"      : lambda x: repack_int(x, "q"),
    "pointer32"  : lambda x: repack_int(x, "I"),
    "utf8_string": lambda x: x,
    "sjis_string": lambda x: x,
    "color32"    : lambda x: repack_color32(x),
    "color128"   : lambda x: repack_color128(x)   
}
