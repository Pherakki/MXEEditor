from pyValkLib.serialisation.Serializable import Serializable
from .AssetEntry import AssetEntry
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray


class AssetTable(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.padding_0x00 = 0
        self.asset_references_count = None
        self.asset_references_offset = None
        self.asset_use_count = None
        self.asset_use_offset = None
        self.padding_0x14 = 0
        self.padding_0x18 = 0
        self.padding_0x1C = 0
        
        self.entries = PointerIndexableArray(self.context)
        self.asset_slot_offsets = []
                
    def rw_fileinfo(self, rw):
        rw.mark_new_contents_array()
        rw.mark_new_contents_array_member()
        
        self.padding_0x00            = rw.rw_uint32(self.padding_0x00)
        self.asset_references_count   = rw.rw_uint32(self.asset_references_count)
        self.asset_references_offset = rw.rw_pointer(self.asset_references_offset)
        self.asset_use_count         = rw.rw_uint32(self.asset_use_count)
        self.asset_use_offset        = rw.rw_pointer(self.asset_use_offset)
        self.padding_0x14            = rw.rw_pad32(self.padding_0x14)
        self.padding_0x18            = rw.rw_pad32(self.padding_0x18)
        self.padding_0x1C            = rw.rw_pad32(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x00)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
        if rw.mode() == 'read':
            self.init_structs()
        
    def init_structs(self):
        self.entries.data = [AssetEntry(self.context) for _ in range(self.asset_references_count)]
        
    def rw_entry_headers(self, rw):
        rw.rw_obj(self.entries)
        
    def rw_asset_slot_offsets(self, rw):
        rw.mark_new_contents_array()
        self.asset_slot_offsets = rw.rw_uint32s(self.asset_slot_offsets, self.asset_use_count)
