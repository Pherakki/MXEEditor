from pyValkLib.serialisation import Serializable
from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH, Header32B


class POF0ReadWriter(ValkSerializable32BH):
    FILETYPE = "POF0"
    
    __slots__ = ("data_size", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.data_size = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.data_size = rw.rw_uint32(self.data_size, endianness='<')
        self.data      = rw.rw_uint8s(self.data, self.data_size - 4)
        rw.align(rw.local_tell(), 0x10)


        


def decompressPOF0(POF0_data, num_offsets):
    offset = 0
    offsets = []  
    data = iter(POF0_data)

    bytes_to_parse = iter(range(num_offsets))
    for loop in bytes_to_parse:
        elem = next(data)
        power_val = elem & 0xC0
        value = elem & 0x3F
        if power_val == 0x40:
            offset += 4*value
            offsets.append(offset)
        elif power_val == 0x80:
            offset_incr = 4*(value << 8 | next(data))
            offset += offset_incr
            next(bytes_to_parse)
            offsets.append(offset)
        elif power_val == 0xC0:
            offset_incr = 4*(value << 0x18 | next(data) << 0x10 | next(data) << 0x08 | next(data))
            offset += offset_incr
            offsets.append(offset)
            next(bytes_to_parse)
            next(bytes_to_parse)
            next(bytes_to_parse)
        else:
            continue
    return offsets

def decompressPOF0_alt(data):
    offset = 0
    offsets = []  
    data = iter(data)

    for elem in data:
        power_val = elem & 0xC0
        value = elem & 0x3F
        if power_val == 0x40:
            offset += 4*value
            offsets.append(offset)
        elif power_val == 0x80:
            offset_incr = 4*(value << 8 | next(data))
            offset += offset_incr
            offsets.append(offset)
        elif power_val == 0xC0:
            offset_incr = 4*(value << 0x18 | next(data) << 0x10 | next(data) << 0x08 | next(data))
            offset += offset_incr
            offsets.append(offset)
        else:
            continue
    return offsets

def decompressPOF0_alt_alt(data):
    offset = 0
    offsets = []  
    data = iter(data)

    for elem in data:
        bit_power = (elem & 0xC0) >> 6
        if bit_power == 0:
            continue
        bitwidth = 1 << (bit_power - 1)
        value = elem & 0x3F
        for _ in range(bitwidth - 1):
            value << 8
            value |= next(data)
            
        offset = 4*value
        offsets.append(offset)

    return offsets

def compressPOF0(offsets):
    data = []
    previous_offset = 0
    for offset in offsets:
        diff = offset - previous_offset
        assert offset & 0x03 == 0, f"Offset is not a multiple of 4! {offset}"
        if diff < 2**8:
            power_val = 0x40
            byte_1 = diff >> 2
            
            data.append(power_val | byte_1)
        elif diff < 2**16:
            power_val = 0x80
            element_data = diff >> 2
            
            byte_1 = (element_data & 0xFF00) >> 0x08
            byte_2 = (element_data & 0x00FF) >> 0x00
            data.append(power_val | byte_1)
            data.append(byte_2)
        elif diff < 2**32:
            power_val = 0xC0
            element_data = diff >> 2
            
            byte_1 = (element_data & 0xFF000000) >> 0x18
            byte_2 = (element_data & 0x00FF0000) >> 0x10
            byte_3 = (element_data & 0x0000FF00) >> 0x08
            byte_4 = (element_data & 0x000000FF) >> 0x00
            data.append(power_val | byte_1)
            data.append(byte_2)
            data.append(byte_3)
            data.append(byte_4)
        
        else:
            raise ValueError(f"Offset differences can be no larger than 2**32: {previous_offset} {offset} {diff}.")
        previous_offset = offset
    return data
