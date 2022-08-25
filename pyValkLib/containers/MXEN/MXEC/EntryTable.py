from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

class EntryTable(Serializable):
    def __init__(self, entry_cls, context):
        super().__init__(context)
        self.entry_cls = entry_cls
        self.entries = PointerIndexableArray(self.context)
         
        self.padding_0x00 = 0
        self.entry_count  = 0
        self.entry_ptr    = 0
        self.padding_0x0C = 0
        
        self.padding_0x10 = 0
        self.padding_0x14 = 0
        self.padding_0x18 = 0
        self.padding_0x1C = 0
        
        self.padding_0x20 = 0
        self.padding_0x24 = 0
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.padding_0x30 = 0
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0
        
    def rw_fileinfo(self, rw):
        rw.mark_new_contents_array()
        rw.mark_new_contents_array_member()
        
        self.padding_0x00 = rw.rw_uint32(self.padding_0x00)
        self.entry_count  = rw.rw_uint32(self.entry_count)
        self.entry_ptr    = rw.rw_pointer(self.entry_ptr)
        self.padding_0x0C = rw.rw_uint32(self.padding_0x0C)
        
        self.padding_0x10 = rw.rw_uint32(self.padding_0x10)
        self.padding_0x14 = rw.rw_pad32(self.padding_0x14)
        self.padding_0x18 = rw.rw_pad32(self.padding_0x18)
        self.padding_0x1C = rw.rw_pad32(self.padding_0x1C)
        
        self.padding_0x20 = rw.rw_pad32(self.padding_0x20)
        self.padding_0x24 = rw.rw_pad32(self.padding_0x24)
        self.padding_0x28 = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C = rw.rw_pad32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)
                
        rw.assert_is_zero(self.padding_0x00)
        rw.assert_is_zero(self.padding_0x0C)
        
        rw.assert_is_zero(self.padding_0x10)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
        if rw.mode() == "read":
            self.entries.data = [self.entry_cls(self.context) for _ in range(self.entry_count)]

    def rw_fileinfo_brt(self, rw):
        rw.mark_new_contents_array()
        rw.mark_new_contents_array_member()
        
        self.padding_0x00 = rw.rw_uint32(self.padding_0x00)
        self.entry_count  = rw.rw_uint32(self.entry_count)
        self.entry_ptr    = rw.rw_pointer(self.entry_ptr)
        self.padding_0x0C = rw.rw_pad32(self.padding_0x0C) # Also padding bytes

        self.padding_0x10 = rw.rw_pad32(self.padding_0x10) # Also padding bytes
        self.padding_0x14 = rw.rw_pad32(self.padding_0x14)
        self.padding_0x18 = rw.rw_pad32(self.padding_0x18)
        self.padding_0x1C = rw.rw_pad32(self.padding_0x1C)

        self.padding_0x20 = rw.rw_pad32(self.padding_0x20)
        self.padding_0x24 = rw.rw_pad32(self.padding_0x24)
        self.padding_0x28 = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C = rw.rw_pad32(self.padding_0x2C)

        self.padding_0x30 = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)

        rw.assert_is_zero(self.padding_0x00)
        rw.assert_is_zero(self.padding_0x0C)

        rw.assert_is_zero(self.padding_0x10)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)

        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)

        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)

        if rw.mode() == "read":
            self.entries.data = [self.entry_cls(self.context) for _ in range(self.entry_count)]

    def rw_entry_headers(self, rw):
        rw.rw_obj(self.entries)

    def rw_entries(self, rw):
        for entry in sorted([entry for entry in self.entries.data], key=lambda x: x.data_offset):
            if rw.mode() == "read":
                component_type = self.check_struct_type(rw, entry.name_offset)
                entry.parameter_type = component_type
            else:
                component_type = entry.parameter_type
                
            if entry.data_offset:
                rw.assert_local_file_pointer_now_at("Entry Data", entry.data_offset)
                
            rw.rw_obj_method(entry, entry.rw_data, component_type)
                
    def check_struct_type(self, rw, offset, prnt=False):
        curr_offset = rw.local_tell()
        rw.local_seek(offset)
        lookup_type = rw.rw_cstr(None, "cp932")
        lookup_type = lookup_type.split(':')[0]
        lookup_type = lookup_type.split('@')[-1]
        rw.local_seek(curr_offset)
        return lookup_type
