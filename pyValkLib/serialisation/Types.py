class Typecode:
    __slots__ = ("name", "typecode", "width")
    
    def __init__(self, name, typecode, width):
        self.name = name
        self.typecode = typecode
        self.width = width
    
int8_t   = Typecode(  "int8", "b", 1)
uint8_t  = Typecode( "uint8", "B", 1)
int16_t  = Typecode( "int16", "h", 2)
uint16_t = Typecode("uint16", "H", 2)
int32_t  = Typecode( "int32", "i", 4)
uint32_t = Typecode("uint32", "I", 4)
int64_t  = Typecode( "int64", "q", 8)
uint64_t = Typecode("uint64", "Q", 8)

float16_t = Typecode("float16", "e", 2)
float32_t = Typecode("float32", "f", 4)
float64_t = Typecode("float64", "d", 8)

PRIMITIVE_TYPES = [ int8_t,  uint8_t,
                   int16_t, uint16_t,
                   int32_t, uint32_t,
                   int64_t, uint64_t,
             
                   float16_t,
                   float32_t, 
                   float64_t]
