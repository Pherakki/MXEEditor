from pyValkLib.serialisation.Serializable import Serializable


class AssetEntry(Serializable):
    
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.flags = None
        self.ID = None
        self.folder_name_ptr = None
        self.file_name_ptr = None
        
        self.filetype = None
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.padding_0x30 = 0
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0   
        
    def read_write(self, rw): 
        # Contents_flags? 
        # 0x000 = all -1
        # 0x100 = something in unknown_0x14, unknown_0x20
        # 0x200 = something in unknown_0x24
        # Unknown0x14 appears to be another ID
        # Unknown_0x20 is 0 if Unknown0x14 > -1
        # Unknown_0x24 also appears to be another ID
        
        # Filetypes?
        # - HMD: 1
        # - HTX: 2
        # - HMT: 3
        # - MCL: 6
        # - MLX: 8
        # - ABR: 9
        # - ABD: 10
        # - CVD: 12
        # - HST: 12
        # - BHV: 12
        # - PVS: 20
        # - HTX: 21 (MergeTexture)
        # - HTR: 22
        # - MMF: 24
        # - MMR: 25
        self.flags           = rw.rw_uint32(self.flags)
        self.ID              = rw.rw_uint32(self.ID)
        self.folder_name_ptr = rw.rw_pointer(self.folder_name_ptr)
        self.file_name_ptr   = rw.rw_pointer(self.file_name_ptr)
        self.filetype        = rw.rw_uint32(self.filetype)
        self.unknown_0x14    = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18    = rw.rw_uint64(self.unknown_0x18)
   
        self.unknown_0x20    = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24    = rw.rw_int32(self.unknown_0x24)
        self.padding_0x28    = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C    = rw.rw_pad32(self.padding_0x2C)
        
        self.padding_0x30    = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34    = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38    = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C    = rw.rw_pad32(self.padding_0x3C)
        
        rw.assert_is_zero(self.unknown_0x18)
        
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
        rw.assert_equal(self.unknown_0x14 > -1, self.unknown_0x20 + 1)
