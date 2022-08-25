import array

from pyValkLib.serialisation import Serializable
from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH, Header32B

#from pyValkLib.utils.Compression.Stencilled import SCRelRep, SCRelativeTemplateGenerator, ENRSTemplateComponent
#from pyValkLib.utils.Compression.Stencilled import SCUnpackedRep, SCTemplatePack, SCTemplate, ENRSUnpackedTemplateComponents
#from pyValkLib.utils.Compression.integers import compressInt, decompressInt
#from pyValkLib.utils.Compression.integers import compressSubStencil, compressSubStencil_test, decompressSubStencil


class ENRSReadWriter(ValkSerializable32BH):
    FILETYPE = "ENRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.padding_0x20 = 0
        self.num_groups = None
        self.data = []
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x : hex(x))
        
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20, endianness='<')
        self.num_groups   = rw.rw_uint32(self.num_groups, endianness='<')
        rw.align(rw.local_tell(), 0x10)
        rw.assert_equal(self.padding_0x20, 0)
        
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10)
        rw.align(rw.local_tell(), 0x10)


#################
# DECOMPRESSION #
#################

def pull_bytecode_Bytes(ENRS_iter, byte_power, bytecode_value):
    out = []
    for _ in range((1 << byte_power) - 1):
        out.append(next(ENRS_iter))
        
    return out

def decompressInt_Bytes(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0x3F
    
    return [elem, *pull_bytecode_Bytes(ENRS_iter, byte_power, bytecode_value)]


def decompressSubStencilDef_Bytes(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0xF
    
    return [elem, *pull_bytecode_Bytes(ENRS_iter, byte_power, bytecode_value)]


class ENRSSubStencil:
    def __init__(self, bitwidth, data):
        self.itemsize = bitwidth
        self.data = array.array('I', data)
    
    def __repr__(self):
        return f"<ENRSSubStencil><{self.itemsize}>{self.data}"
    
    def __iter__(self):
        for elem in self.data:
            yield elem
            
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __setitem__(self, idx, value):
        self.data[idx] = value


# def decompressENRS_test(num_groups, data):
#     ENRS_iter_data = iter(data)
#     out = SCRelRep("ENRS")
    
#     for _ in range(num_groups):
#         jump_from_previous_group = decompressInt(ENRS_iter_data)
#         num_sub_stencils = decompressInt(ENRS_iter_data)
#         stencil_size = decompressInt(ENRS_iter_data)
#         stencil_repetitions = decompressInt(ENRS_iter_data)

#         sub_stencil_defs = []
#         for j in range(num_sub_stencils):
#             jump, stride = decompressSubStencil(ENRS_iter_data)
#             count = decompressInt(ENRS_iter_data)
#             sub_stencil_defs.append(ENRSTemplateComponent(jump, count, stride))
            
#         cgen = SCRelativeTemplateGenerator(jump_from_previous_group, stencil_size, stencil_repetitions,
#                                            sub_stencil_defs)
#         out.append(cgen)
        
#     return out.to_abs_rep().to_unpacked_rep()

# def decompressENRS(num_groups, data):
#     offset = 0
#     offsets = []
    
#     ENRS_iter_data = iter(data)
#     for loop in range(num_groups):
#         # Decode the ENRS spec
#         jump_from_previous_stencil_group = decompressInt(ENRS_iter_data)
#         offset += jump_from_previous_stencil_group
        
#         num_sub_stencils = decompressInt(ENRS_iter_data)
#         stencil_size = decompressInt(ENRS_iter_data)
#         stencil_repetitions = decompressInt(ENRS_iter_data)
#         working_offset = offset
#         sub_stencil_defs = []
#         for j in range(num_sub_stencils):    
#             sub_stencil_defs.append((*decompressSubStencil(ENRS_iter_data), decompressInt(ENRS_iter_data)))
            
#         # Generate offsets
#         stencil_group = []
#         for i in range(stencil_repetitions):
#             saved_offset = working_offset + stencil_size
#             stencil = []
            
#             do_print = working_offset == 99072
#             if do_print:
#                 print("NEW DECOMPRESS")
            
#             for j in range(num_sub_stencils):
#                 jump_from_previous_substencil, elem_byte_power, elem_count = sub_stencil_defs[j]
#                 working_offset += jump_from_previous_substencil

                    
#                 diff = 2 << elem_byte_power
#                 sub_stencil = []
#                 for k in range(elem_count):
#                     sub_stencil.append(working_offset)
#                     working_offset += diff

#                 sub_stencil = ENRSSubStencil(diff, sub_stencil)
#                 stencil.append(sub_stencil)
                
#                 if do_print:
#                     print(jump_from_previous_substencil, elem_byte_power, elem_count)
#                     print(sub_stencil)
#             stencil_group.append(stencil)
#             working_offset = saved_offset
#         offsets.append(stencil_group)
        
#     return offsets

# def divideENRSBytes(num_groups, data):
#     bytes_out = []
    
#     ENRS_iter_data = iter(data)
#     for loop in range(num_groups):
#         hdr = []
#         # Decode the ENRS spec
#         hdr.extend(decompressInt_Bytes(ENRS_iter_data))
        
#         num_sub_stencils_bytes = decompressInt_Bytes(ENRS_iter_data)
#         num_sub_stencils = decompressInt(iter(num_sub_stencils_bytes))
#         hdr.extend(num_sub_stencils_bytes)
#         hdr.extend(decompressInt_Bytes(ENRS_iter_data))
#         hdr.extend(decompressInt_Bytes(ENRS_iter_data))

#         subs = []
#         for j in range(num_sub_stencils):    
#             subs.append([*decompressSubStencilDef_Bytes(ENRS_iter_data), decompressInt_Bytes(ENRS_iter_data)])

#         bytes_out.append([hdr, subs])

#     return bytes_out


# ###############
# # COMPRESSION #
# ###############    

# def compressENRS_test(enrs_unpacked_rep):
#     out = []
    
#     enrs_rel_rep = enrs_unpacked_rep.to_abs_rep().to_rel_rep()
#     for tg in enrs_rel_rep:
#         out.extend(compressInt(tg.jump))
#         out.extend(compressInt(len(tg.subs)))
#         out.extend(compressInt(tg.stride))
#         out.extend(compressInt(tg.count))
        
#         for comp in tg:
#             out.extend(compressSubStencil_test(comp.stride, comp.type))
#             out.extend(compressInt(comp.count))
        
#             comp_1 = compressSubStencil_test(comp.stride, comp.type)
#             comp_2 = compressInt(comp.count)
#             decomp_1 = decompressSubStencil(iter(comp_1))
#             decomp_2 = decompressInt(iter(comp_2))
#             if comp.stride != decomp_1[0] or comp.type != decomp_1[1] or comp.count != decomp_2:
#                 print(">>", comp.unpack())
#                 print(">> BEFORE", comp.stride, comp.type, comp.count)
#                 print(">> AFTER", *decomp_1, decomp_2)
#                 assert 0
        
#     return out

# def compressENRS(pointer_offsets):
#     data = []
#     prev_main_array_offset = 0
#     for idx, main_array in enumerate(pointer_offsets):
#         stencil = main_array[0]
        
#         first_offset = main_array[0][0][0]
#         num_array_member_copies = len(main_array)
#         num_sub_stencils = len(main_array[0])
        
#         # Calculate the jump between stencils
#         # Surely this can be simplified?
#         if idx+1 == len(pointer_offsets):
#             #if len(main_array) == 1 and len(main_array[0]) == 1 and len(main_array[0][0]) == 1:
#             #     stencil_size = 1
#             if len(stencil) > 2:
#                 stencil_size = stencil[1][0] - stencil[0][0]
#             else:
#                 stencil_size = stencil[0].itemsize
#         else:
#             #is_contiguous = pointer_offsets[idx+1][0][0][0] == (main_array[-1][-1][-1] + main_array[-1][-1].itemsize)
#             #if len(main_array) == 1 and len(main_array[0]) == 1 and is_contiguous:
#             #     stencil_size = 1
#             #else:
#             offset_to_next_stencil_group = pointer_offsets[idx+1][0][0][0] - stencil[0][0]
#             stencil_size = offset_to_next_stencil_group // len(main_array)
        
#         data.extend(compressInt(first_offset - prev_main_array_offset))
#         data.extend(compressInt(num_sub_stencils))
#         data.extend(compressInt(stencil_size))
#         data.extend(compressInt(num_array_member_copies))
        
#         prev_main_array_offset = first_offset
        
#         do_print = stencil[0][0] == 99072
#         if do_print:
#             print("NEW COMPRESS")
#             print(main_array)
#         previous_substencil_offset = stencil[0][0]
#         for j, sub_stencil in enumerate(stencil):
#             starting_offset = sub_stencil[0] - previous_substencil_offset
#             diff = sub_stencil.itemsize
            
#             sub_stencil_count = len(sub_stencil)
            
#             data.extend(compressSubStencil(starting_offset, diff))
#             data.extend(compressInt(sub_stencil_count))
#             if do_print:
#                 print(">", previous_substencil_offset, sub_stencil[0])
#                 print(">", starting_offset, diff, sub_stencil_count)
#                 print(compressSubStencil(starting_offset, diff), decompressSubStencil(iter(compressSubStencil(starting_offset, diff))))
#                 print(sub_stencil)
#                 print(previous_substencil_offset, diff*sub_stencil_count)
            
#             previous_substencil_offset = sub_stencil[-1] + diff

#     return data
