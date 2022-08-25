from pyValkLib.serialisation.Serializable import Context
from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayCStr, PointerIndexableArrayUint64
from pyValkLib.containers.MXEN.MXEC.EntryTable import EntryTable 
from pyValkLib.containers.MXEN.MXEC.ParameterEntry import ParameterEntry
from pyValkLib.containers.MXEN.MXEC.ECSEntityEntry import EntityEntry
from pyValkLib.containers.MXEN.MXEC.PathingEntry import PathingEntry
from pyValkLib.containers.MXEN.MXEC.AssetTable import AssetTable
from pyValkLib.containers.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.CCRS.CCRSReadWriter import CCRSReadWriter
from pyValkLib.containers.EOFC.EOFCReadWriter import EOFCReadWriter

import struct


class MXECReadWriter(ValkSerializable32BH):
    FILETYPE = "MXEC"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.content_flags            = 0x00000000
        self.parameter_sets_table_ptr = 0
        self.entity_table_ptr         = 0
        self.asset_table_ptr          = 0
        
        self.unknown_0x30             = 1
        self.pathing_table_ptr        = 0
        self.texmerge_count           = 0
        self.texmerge_ptrs_ptr        = 0
        
        self.pvs_record_ptr           = 0
        self.mergefile_record_ptr     = 0
        self.padding_0x48             = 0
        self.padding_0x4C             = 0
        
        self.padding_0x50             = 0
        self.padding_0x54             = 0
        self.padding_0x58             = 0
        self.padding_0x5C             = 0
        
        self.parameter_sets_table = EntryTable(ParameterEntry, self.context) # Parameter table
        self.entity_table         = EntryTable(EntityEntry, self.context)    # Entity table
        self.pathing_table        = EntryTable(PathingEntry, self.context)   # Path Graph table
        self.asset_table          = AssetTable(self.context)                 # Asset table

        self.texmerge_ptr = None
        self.sjis_strings = PointerIndexableArrayCStr(self.context, "cp932")
        self.utf8_strings = PointerIndexableArrayCStr(self.context, "utf8")
        self.unknowns = PointerIndexableArrayUint64(self.context)

        subcontainer_context = Context()
        subcontainer_context.endianness = '<'
        self.POF0 = POF0ReadWriter({}, '<')
        self.ENRS = ENRSReadWriter({}, '<')
        self.CCRS = CCRSReadWriter({}, '<')
        self.EOFC = EOFCReadWriter('<')
            
    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.CCRS, self.EOFC]
    
    def __repr__(self):
        return f"MXEC Object [{self.header.depth}] [0x{self.header.flags:0>8x}]:\n" \
               f"[{len(self.parameter_sets_table.entries.data)}] Parameter Sets.\n"\
               f"[{len(self.entity_table.entries.data)}] Entities.\n"\
               f"[{len(self.pathing_table.entries.data)}] Pathing Entries.\n"\
               f"[{len(self.asset_table.entries.data)}] Asset References.\n"\
               f"[{len(self.asset_table.asset_slot_offsets)}] Asset Pointers.\n"\
               f"Contains POF0, ENRS, CCRS, and EOFC."
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        self.rw_fileinfo(rw)
        self.rw_parameter_sets_table(rw)
        self.rw_entities_table(rw)
        self.rw_pathing_table(rw)
        self.rw_asset_table(rw)
        self.rw_strings(rw)
        self.rw_unknowns(rw)
        
        rw.mark_new_contents_array()
        
    def rw_fileinfo(self, rw):
        # Read/write
        rw.mark_new_contents_array()
        rw.mark_new_contents_array_member()

        self.content_flags            = rw.rw_uint32(self.content_flags)
        self.parameter_sets_table_ptr = rw.rw_pointer(self.parameter_sets_table_ptr)
        self.entity_table_ptr         = rw.rw_pointer(self.entity_table_ptr)
        self.asset_table_ptr          = rw.rw_pointer(self.asset_table_ptr)

        self.unknown_0x30             = rw.rw_uint32(self.unknown_0x30)
        self.pathing_table_ptr        = rw.rw_pointer(self.pathing_table_ptr)
        self.texmerge_count           = rw.rw_uint32(self.texmerge_count)
        self.texmerge_ptrs_ptr        = rw.rw_pointer(self.texmerge_ptrs_ptr)
        
        self.pvs_record_ptr           = rw.rw_pointer(self.pvs_record_ptr)
        self.mergefile_record_ptr     = rw.rw_pointer(self.mergefile_record_ptr)
        self.padding_0x48             = rw.rw_pad32(self.padding_0x48)
        self.padding_0x4C             = rw.rw_pad32(self.padding_0x4C)
        
        self.padding_0x50             = rw.rw_pad32(self.padding_0x50)
        self.padding_0x54             = rw.rw_pad32(self.padding_0x54)
        self.padding_0x58             = rw.rw_pad32(self.padding_0x58)
        self.padding_0x5C             = rw.rw_pad32(self.padding_0x5C)

        # VALIDATION
        
        # 0x00000100 -> ??? Always active, may be related to unknown_0x30
        # 0x00000400 -> texmerge count + ptrs_ptr enabled
        # 0x00001800 -> pvs enabled
        # 0x01000000 -> mergefile enabled
        unknown_enabled   = (self.content_flags & 0x00000100) == 0x00000100
        texmerge_enabled  = (self.content_flags & 0x00000400) == 0x00000400
        pvs_enabled       = (self.content_flags & 0x00001800) == 0x00001800
        mergefile_enabled = (self.content_flags & 0x01000000) == 0x01000000
        
        # Check we've got all the flags
        cflags = self.content_flags
        cflags -=   unknown_enabled * 0x00000100
        cflags -=  texmerge_enabled * 0x00000400
        cflags -=       pvs_enabled * 0x00001800
        cflags -= mergefile_enabled * 0x01000000
        assert cflags == 0, f"Some MXEC flags uncaught! 0x{cflags:0>8x}"
        
        rw.assert_equal(self.unknown_0x30, 1)
        rw.assert_equal((self.texmerge_count > 0), texmerge_enabled)
        rw.assert_equal((self.texmerge_ptrs_ptr > 0), texmerge_enabled)
        
        rw.assert_equal(self.padding_0x48, 0)
        rw.assert_equal(self.padding_0x4C, 0)
        rw.assert_equal((self.pvs_record_ptr > 0), pvs_enabled)
        rw.assert_equal((self.mergefile_record_ptr > 0), mergefile_enabled)

        rw.assert_equal(self.padding_0x50, 0)
        rw.assert_equal(self.padding_0x54, 0)
        rw.assert_equal(self.padding_0x58, 0)
        rw.assert_equal(self.padding_0x5C, 0)
        
    def rw_parameter_sets_table(self, rw):
        if self.parameter_sets_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Parameter Sets Table", self.parameter_sets_table_ptr)
            rw.rw_obj_method(self.parameter_sets_table, self.parameter_sets_table.rw_fileinfo)
            rw.assert_local_file_pointer_now_at("Parameter Sets Table Entry Headers", self.parameter_sets_table.entry_ptr)
            rw.rw_obj_method(self.parameter_sets_table, self.parameter_sets_table.rw_entry_headers)
            rw.rw_obj_method(self.parameter_sets_table, self.parameter_sets_table.rw_entries)

    def rw_entities_table(self, rw):
        if self.entity_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Entity Table", self.entity_table_ptr)
            rw.rw_obj_method(self.entity_table, self.entity_table.rw_fileinfo)
            rw.assert_local_file_pointer_now_at("Entity Table Entry Headers", self.entity_table.entry_ptr)
            rw.rw_obj_method(self.entity_table, self.entity_table.rw_entry_headers)
            rw.rw_obj_method(self.entity_table, self.entity_table.rw_entries)
            
            rw.align(rw.local_tell(), 0x10)
            
    def rw_pathing_table(self, rw):
        if self.pathing_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Pathing Table", self.pathing_table_ptr)
            rw.rw_obj_method(self.pathing_table, self.pathing_table.rw_fileinfo_brt)
            rw.assert_local_file_pointer_now_at("Pathing Table Entry Headers", self.pathing_table.entry_ptr)
            rw.rw_obj_method(self.pathing_table, self.pathing_table.rw_entry_headers)
            for entry in self.pathing_table.entries:
                rw.rw_obj_method(entry, entry.rw_data)

    def rw_asset_table(self, rw):
        if self.asset_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Asset Table", self.asset_table_ptr)
            rw.rw_obj_method(self.asset_table, self.asset_table.rw_fileinfo)
            
            rw.assert_local_file_pointer_now_at("Asset Table Entry Headers", self.asset_table.asset_references_offset)
            rw.rw_obj_method(self.asset_table, self.asset_table.rw_entry_headers)

                
            rw.assert_local_file_pointer_now_at("Asset Table Entries", self.asset_table.asset_use_offset)
            rw.rw_obj_method(self.asset_table, self.asset_table.rw_asset_slot_offsets)
            
            if self.texmerge_ptrs_ptr != 0:
                rw.assert_local_file_pointer_now_at("Texmerge pointers", self.texmerge_ptrs_ptr)
                self.texmerge_ptr = rw.rw_pointers(self.texmerge_ptr, self.texmerge_count)
            
            rw.align(rw.local_tell(), 0x10)
        
    def rw_strings(self, rw):
        if (rw.mode() == "read"):
            self.read_strings(rw)
        else:# (rw.mode() == "write"):
            self.write_strings(rw)
        #else:
        #    raise Exception("Unknown mode!")
            
        rw.align(rw.local_tell(), 0x10)
        
    def read_strings(self, rw):
        # Instead of reading/writing blobs, might make sense to collect a list
        # of string pointers during the read/write and then make those read/writes.
        # You would of course have to keep separate lists for UTF-8 and SHIFT-JIS strings.
        curpos = rw.local_tell()
        start_pos = rw.local_tell()

        # Get the start of the unknown data
        entity_data_offsets = [elem.unknown_data_ptr for elem in self.entity_table.entries.data if elem.unknown_data_ptr > 0]
        end_point = min(entity_data_offsets) if len(entity_data_offsets) else self.header.header_length + self.header.data_length


        # Get the start of the UTF-8 strings
        utf8_string_offsets = [elem.data.get_string_ptrs() for elem in self.parameter_sets_table.entries]
        utf8_string_offsets = [subitem for item in utf8_string_offsets for subitem in item]
        
        start_of_utf8_strings = min(utf8_string_offsets) if len(utf8_string_offsets) else end_point

        main_string_blob      = memoryview(rw.bytestream.read(start_of_utf8_strings - start_pos))

        n_entries = 0
        first_string = True
        while curpos < start_of_utf8_strings:
            strn, size = parse_null_terminated_string(main_string_blob[curpos-start_pos:])
            if strn == "" and not first_string:
                curpos += 1  # Looks like we read a null-terminator, must be at alignment
                break

            self.sjis_strings.data.append(strn)
            self.sjis_strings.ptr_to_idx[curpos] = n_entries
            self.sjis_strings.idx_to_ptr[n_entries] = curpos
            n_entries += 1
            curpos += size
            first_string = False

        remaining_stuff = main_string_blob[curpos-start_pos:].tobytes()
        if remaining_stuff != (b'\x00'*len(remaining_stuff)):
            print(remaining_stuff)
            raise Exception(f"End of SHIFT-JIS String Bank not reached!\n{remaining_stuff}")
        rw.align(rw.local_tell(), 0x10) # Will already be aligned since we've read an aligned blob
        curpos = rw.local_tell()

        rw.assert_local_file_pointer_now_at("Start of UTF-8 String Bank", start_of_utf8_strings)
        utf8_string_blob = memoryview(rw.bytestream.read(end_point - start_of_utf8_strings))
        n_entries = 0
        first_string = True
        while curpos < end_point:
            strn, size = parse_null_terminated_string_utf8(utf8_string_blob[curpos-start_of_utf8_strings:])
            if strn == "" and not first_string:
                curpos += 1
                break

            self.utf8_strings.data.append(strn)
            self.utf8_strings.ptr_to_idx[curpos] = n_entries
            self.utf8_strings.idx_to_ptr[n_entries] = curpos
            n_entries += 1
            curpos += size
            first_string = False

        remaining_stuff = utf8_string_blob[curpos-start_of_utf8_strings:].tobytes()
        if remaining_stuff != (b'\x00'*len(remaining_stuff)):
            print(remaining_stuff)
            raise Exception("End of UTF-8 String Bank not reached!")
        rw.align(rw.local_tell(), 0x10) # Will already be aligned since we've read an aligned blob
        rw.assert_local_file_pointer_now_at("End of UTF-8 String Bank", end_point)
        
    def write_strings(self, rw):
        for string in self.sjis_strings:
            rw.rw_cstr(string, encoding="cp932")
            #rw.bytestream.write(string.encode("cp932"))
            #rw.bytestream.write(b"\x00")
        rw.align(rw.local_tell(), 0x10)
        for string in self.utf8_strings:
            rw.rw_cstr(string, encoding="utf8")
            #rw.bytestream.write(string.encode("utf8"))
            #rw.bytestream.write(b"\x00")
        rw.align(rw.local_tell(), 0x10)
        
    def read_unknowns(self, rw):
        entity_data_offsets = sorted(set([elem.unknown_data_ptr for elem in self.entity_table.entries.data if elem.unknown_data_ptr > 0]))
        for offset in entity_data_offsets:
            rw.assert_local_file_pointer_now_at("Unknowns Offset", offset)
            idx =  len(self.unknowns.idx_to_ptr)
            self.unknowns.ptr_to_idx[offset] = len(self.unknowns.idx_to_ptr)
            self.unknowns.idx_to_ptr[idx] = offset
            self.unknowns.data.append((struct.unpack('Q', rw.bytestream.read(8))[0]))

    def write_unknowns(self, rw):
        for data in self.unknowns.data:
            rw.rw_uint64(data)

    def rw_unknowns(self, rw):
        # Pretty sure this can just be read/written as a PIA if you put the
        # uniqueness check on it
        if (rw.mode() == "read"):
            self.read_unknowns(rw)
        else:# (rw.mode() == "write"):
            self.write_unknowns(rw)
        #else:
        #    raise Exception("Unknown mode!")
        rw.align(rw.local_tell(), 0x10)
        

def parse_null_terminated_string(data):
    size = 0
    while data[size] != 0:
        size += 1
    try:
        string = data[0:size].tobytes().decode('cp932') # Asset table strings are UTF8, all others are SHIFT-JIS... delay decode for the particular table
    except Exception as e:
        print(data[0:size].tobytes())
        raise e
    return string, size+1

def parse_null_terminated_string_utf8(data):
    size = 0
    while data[size] != 0:
        size += 1
    try:
        string = data[0:size].tobytes().decode('utf8') # Asset table strings are UTF8, all others are SHIFT-JIS... delay decode for the particular table
    except Exception as e:
        print(data[0:size].tobytes())
        raise e
    return string, size+1
