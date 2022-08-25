#################
# DECOMPRESSION #
#################
def parseCompressedInt(ENRS_iter, byte_power, bytecode_value):
    for _ in range((1 << byte_power) - 1):
        elem = next(ENRS_iter)
        bytecode_value <<= 8
        bytecode_value |= elem
        
    return bytecode_value

def decompressInt(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power     = (elem & 0xC0) >> 6
    bytecode_value = (elem & 0x3F) >> 0
    
    return parseCompressedInt(ENRS_iter, byte_power, bytecode_value)


def decompressSubStencil(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power       = (elem & 0xC0) >> 6
    array_byte_power = (elem & 0x30) >> 4
    bytecode_value   = (elem & 0x0F) >> 0
    
    return parseCompressedInt(ENRS_iter, byte_power, bytecode_value), array_byte_power

###############
# COMPRESSION #
###############
def compressInt(integer):
    data = []
    if integer < 2**6:
        power_val = 0x00
        
        byte_1 = (integer & 0x3F) >> 0x00
        
        data.append(power_val | byte_1)
    elif integer < 2**14:
        power_val = 0x40
        
        byte_1 = (integer & 0x3F00) >> 0x08
        byte_2 = (integer & 0x00FF) >> 0x00
        
        data.append(power_val | byte_1)
        data.append(byte_2)
    elif integer < 2**30:
        power_val = 0x80
        
        byte_1 = (integer & 0x3F000000) >> 0x18
        byte_2 = (integer & 0x00FF0000) >> 0x10
        byte_3 = (integer & 0x0000FF00) >> 0x08
        byte_4 = (integer & 0x000000FF) >> 0x00
        
        data.append(power_val | byte_1)
        data.append(byte_2)
        data.append(byte_3)
        data.append(byte_4)
    else:
        raise ValueError(f"Int can be no larger than 2**30: {integer}.")
    return data

def compressSubStencil(starting_offset, diff):
    data = []
    elem_byte_power = (diff << 4) & 0x30
    if starting_offset < 2**4:
        power_val = 0x00
        
        byte_1 = (starting_offset & 0x0F) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
    elif starting_offset < 2**12:
        power_val = 0x40
        
        byte_1 = (starting_offset & 0x0F00) >> 0x08
        byte_2 = (starting_offset & 0x00FF) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
        data.append(byte_2)
    elif starting_offset < 2**28:
        power_val = 0x80
        
        byte_1 = (starting_offset & 0x0F000000) >> 0x18
        byte_2 = (starting_offset & 0x00FF0000) >> 0x10
        byte_3 = (starting_offset & 0x0000FF00) >> 0x08
        byte_4 = (starting_offset & 0x000000FF) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
        data.append(byte_2)
        data.append(byte_3)
        data.append(byte_4)
    else:
        raise ValueError(f"Offset can be no larger than 2**28: {diff}.")
    return data

def compressSubStencilOld(starting_offset, diff):
    data = []
    #elem_byte_power = (diff << 4) & 0x30
    elem_byte_power = diff << 2
    if starting_offset < 2**4:
        power_val = 0x00
        
        byte_1 = (starting_offset & 0x0F) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
    elif starting_offset < 2**12:
        power_val = 0x40
        
        byte_1 = (starting_offset & 0x0F00) >> 0x08
        byte_2 = (starting_offset & 0x00FF) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
        data.append(byte_2)
    elif starting_offset < 2**28:
        power_val = 0x80
        
        byte_1 = (starting_offset & 0x0F000000) >> 0x18
        byte_2 = (starting_offset & 0x00FF0000) >> 0x10
        byte_3 = (starting_offset & 0x0000FF00) >> 0x08
        byte_4 = (starting_offset & 0x000000FF) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
        data.append(byte_2)
        data.append(byte_3)
        data.append(byte_4)
    else:
        raise ValueError(f"Offset can be no larger than 2**28: {diff}.")
    return data
