from pyValkLib.serialisation.ValkyriaBaseRW import BaseRW

        
##############
# DATA TYPES #
##############
        
class MxParameterFog(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C)
        
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C ]
    
class HyColor(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C)
        
    def asset_table_offsets(self):
        return []
    
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]
    
class MxParameterLight(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "f", endianness='>')
        self.rw_var("unknown_0x48", "f", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_ptr_1", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.assert_is_zero("unknown_0x54")
        self.assert_is_zero("unknown_0x58")
        self.assert_is_zero("unknown_0x5C")
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_ptr_1, self.unknown_0x54, self.unknown_0x58, self.unknown_0x5C)
    
    def asset_table_offsets(self):
        return []
            
    def pof0_offsets(self):
        return [0x50]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C , 0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50 ]
        
class MxParameterStaticLight(BaseRW):
    def __init__(self):
        super().__init__()
        self.lights = []
        
    def read_write(self):
        self.rw_var("light_count", "I", endianness='>')
        self.rw_var("unknown_ptr", "I", endianness='>')
        self.rw_var("padding_0x08", "I", endianness='>')
        self.rw_var("padding_0x0C", "I", endianness='>')
        
        self.assert_is_zero("padding_0x08")
        self.assert_is_zero("padding_0x0C")
        
        if self.rw_method == "read":
            self.lights = [MxParameterLight() for _ in range(self.light_count)]
            
        for light in self.lights:
            getattr(light, self.rw_method)(self.bytestream)
        
    def get_data(self):
        return (self.light_count, self.unknown_ptr, [light.get_data() for light in self.lights])

    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return [0x04]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]
    
class VlMxFogParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='<')
        
        
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, 
                self.unknown_0x14)
        
    def asset_table_offsets(self):
        return []
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10 ]
    
class VlMxShaderParamSetId(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C)
         
    def asset_table_offsets(self):
        return []  
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C ]
    
class VlMxStandardLightParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "f", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "f", endianness='>')
        self.rw_var("unknown_0x48", "f", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "f", endianness='>')
        self.rw_var("unknown_0x64", "f", endianness='>')
        self.rw_var("unknown_0x68", "f", endianness='>')
        self.rw_var("unknown_0x6C", "f", endianness='>')
        
        self.rw_var("unknown_0x70", "f", endianness='>')
        self.rw_var("unknown_0x74", "f", endianness='>')
        self.rw_var("unknown_0x78", "f", endianness='>')
        self.rw_var("unknown_0x7C", "f", endianness='>')
        
        self.rw_var("unknown_0x80", "I", endianness='>')
        self.rw_var("unknown_0x84", "I", endianness='>')
        self.rw_var("unknown_0x88", "I", endianness='>')
        self.rw_var("unknown_0x8C", "I", endianness='>')
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54, self.unknown_0x58, self.unknown_0x5C,
                self.unknown_0x60, self.unknown_0x64, self.unknown_0x68, self.unknown_0x6C,
                self.unknown_0x70, self.unknown_0x74, self.unknown_0x78, self.unknown_0x7C,
                self.unknown_0x80, self.unknown_0x84, self.unknown_0x88, self.unknown_0x8C)

    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,         0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C
               ]

class EnTalkEventMapParam(BaseRW):
    def read_write(self):
        # THESE ALL SEEM TO BE FLAGS
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                 0x110, 0x118
               ]

class VlMxAddEsdInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]
    
class VlMxCharacterAffinityInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08)
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08 ]

class VlMxCharacterCommonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "f", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "I", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "f", endianness='>')
        self.rw_var("unknown_0x48", "f", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54 )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54
               ]

class VlMxCharacterEachInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
        self.rw_var("unknown_0x58", "f", endianness='>')
        self.rw_var("unknown_0x5C", "f", endianness='>')
        
        self.rw_var("unknown_0x60", "f", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='>')
        self.rw_var("unknown_0x78", "i", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='>')
        
        self.rw_var("unknown_0xD0", "i", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
        self.rw_var("unknown_0xF8", "i", endianness='>')
        self.rw_var("unknown_0xFC", "i", endianness='>')
        
        self.rw_var("unknown_0x0100", "i", endianness='>')
        self.rw_var("unknown_0x0104", "i", endianness='>')
        self.rw_var("unknown_0x0108", "i", endianness='>')
        self.rw_var("unknown_0x010C", "i", endianness='>')
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "i", endianness='>')
        self.rw_var("unknown_0x014C", "i", endianness='>')
        
        self.rw_var("unknown_0x0150", "i", endianness='>')
        self.rw_var("unknown_0x0154", "i", endianness='>')
        self.rw_var("unknown_0x0158", "i", endianness='>')
        self.rw_var("unknown_0x015C", "i", endianness='>')
        
        self.rw_var("unknown_0x0160", "i", endianness='>')
        self.rw_var("unknown_0x0164", "i", endianness='>')
        self.rw_var("unknown_0x0168", "i", endianness='>')
        self.rw_var("unknown_0x016C", "i", endianness='>')
        
        self.rw_var("unknown_0x0170", "i", endianness='>')
        self.rw_var("unknown_0x0174", "i", endianness='>')
        self.rw_var("unknown_0x0178", "i", endianness='>')
        self.rw_var("unknown_0x017C", "i", endianness='>')
        
        self.rw_var("unknown_0x0180", "i", endianness='>')
        self.rw_var("unknown_0x0184", "i", endianness='>')
        self.rw_var("unknown_0x0188", "i", endianness='>')
        self.rw_var("unknown_0x018C", "i", endianness='>')
        
        self.rw_var("unknown_0x0190", "i", endianness='>')
        self.rw_var("unknown_0x0194", "i", endianness='>')
        self.rw_var("unknown_0x0198", "i", endianness='>')
        self.rw_var("unknown_0x019C", "i", endianness='>')
        
        self.rw_var("unknown_0x01A0", "i", endianness='>')
        self.rw_var("unknown_0x01A4", "i", endianness='>')
        self.rw_var("unknown_0x01A8", "i", endianness='>')
        self.rw_var("unknown_0x01AC", "i", endianness='>')
        
        self.rw_var("unknown_0x01A0", "i", endianness='>')
        self.rw_var("unknown_0x01A4", "i", endianness='>')
        self.rw_var("unknown_0x01A8", "i", endianness='>')
        self.rw_var("unknown_0x01AC", "i", endianness='>')
        
        self.rw_var("unknown_0x01B0", "i", endianness='>')
        self.rw_var("unknown_0x01B4", "i", endianness='>')
        self.rw_var("unknown_0x01B8", "i", endianness='>')
        self.rw_var("unknown_0x01BC", "i", endianness='>')
        
        self.rw_var("unknown_0x01C0", "i", endianness='>')
        self.rw_var("unknown_0x01C4", "i", endianness='>')
        self.rw_var("unknown_0x01C8", "i", endianness='>')
        self.rw_var("unknown_0x01CC", "i", endianness='>')
        
        self.rw_var("unknown_0x01D0", "i", endianness='>')
        self.rw_var("unknown_0x01D4", "i", endianness='>')
        self.rw_var("unknown_0x01D8", "i", endianness='>')
        self.rw_var("unknown_0x01DC", "i", endianness='>')
        
        self.rw_var("unknown_0x01E0", "i", endianness='>')
        self.rw_var("unknown_0x01E4", "i", endianness='>')
        self.rw_var("unknown_0x01E8", "i", endianness='>')
        self.rw_var("unknown_0x01EC", "i", endianness='>')
        
        self.rw_var("unknown_0x01F0", "i", endianness='>')
        self.rw_var("unknown_0x01F4", "i", endianness='>')
        self.rw_var("unknown_0x01F8", "i", endianness='>')
        self.rw_var("unknown_0x01FC", "i", endianness='>')
        
        self.rw_var("unknown_0x0200", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198,  self.unknown_0x019C,
                 self.unknown_0x01A0,  self.unknown_0x01A4,  self.unknown_0x01A8,  self.unknown_0x01AC,
                 self.unknown_0x01B0,  self.unknown_0x01B4,  self.unknown_0x01B8,  self.unknown_0x01BC,
                 self.unknown_0x01C0,  self.unknown_0x01C4,  self.unknown_0x01C8,  self.unknown_0x01CC,
                 self.unknown_0x01D0,  self.unknown_0x01D4,  self.unknown_0x01D8,  self.unknown_0x01DC,
                 self.unknown_0x01E0,  self.unknown_0x01E4,  self.unknown_0x01E8,  self.unknown_0x01EC,
                 self.unknown_0x01F0,  self.unknown_0x01F4,  self.unknown_0x01F8,  self.unknown_0x01FC,
                 
                 self.unknown_0x0200 )  
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x38, 0x3C, 0x40, 0x44, 0x48 ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                 0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                 0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  
                 0xB8,  0xBA,  0xBC,  0xBE,
                 0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                 0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                0x180, 0x184, 0x188, 0x18C, 0x190, 0x194, 0x198, 0x19C,
                0x1A0, 0x1A4, 0x1A8, 0x1AC, 0x1B0, 0x1B4, 0x1B8, 0x1BC,
                0x1C0, 0x1C4, 0x1C8, 0x1CC, 0x1D0, 0x1D4, 0x1D8, 0x1DC,
                0x1E0, 0x1E4, 0x1E8, 0x1EC, 0x1F0, 0x1F4, 0x1F8, 0x1FC,
                0x200, 0x204, 0x208, 0x20C, 0x210
               ]

class VlMxCharacterInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [0x04, 0x08, 0x0C, 0x10, 0x14, 0x18]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C
               ]
    
class VlMxClothesInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
      
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x00, 0x04 ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20
               ]
    
class VlMxExplosiveInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='<')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')  
          
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, self.unknown_0x08,  
                 self.unknown_0x0C, self.unknown_0x10 )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08,  0x0C,  0x10 ]
        
class VlMxForceInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
      
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20
               ]
    
class VlMxGalliaRareWeaponCandidateInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='<')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "h", endianness='>')  
        self.rw_var("unknown_0x16", "h", endianness='>') 
        self.rw_var("unknown_0x18", "h", endianness='>') 
        self.rw_var("unknown_0x1A", "h", endianness='>')  
          
    def get_data(self):
        return ( self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C, 
                 self.unknown_0x10, self.unknown_0x14, self.unknown_0x16, self.unknown_0x18, 
                 self.unknown_0x1A, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x04,  0x08,  0x0C,  0x10,  0x14,  0x16, 0x18,  0x1A ]
  
class VlMxGeneralCharInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.rw_var("unknown_0x30", "I", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "I", endianness='>')
        self.rw_var("unknown_0x74", "I", endianness='>')
        self.rw_var("unknown_0x78", "I", endianness='>')
        self.rw_var("unknown_0x7C", "I", endianness='>')
        
        self.rw_var("unknown_0x80", "I", endianness='>')
        self.rw_var("unknown_0x84", "I", endianness='>')
        self.rw_var("unknown_0x88", "I", endianness='>')
        self.rw_var("unknown_0x8C", "I", endianness='>')
        
        self.rw_var("unknown_0x90", "I", endianness='>')
        self.rw_var("unknown_0x94", "I", endianness='>')
        self.rw_var("unknown_0x98", "I", endianness='>')
        self.rw_var("unknown_0x9C", "I", endianness='>')
        
        self.rw_var("unknown_0xA0", "I", endianness='>')
        self.rw_var("unknown_0xA4", "I", endianness='>')
        self.rw_var("unknown_0xA8", "I", endianness='>')
        self.rw_var("unknown_0xAC", "I", endianness='>')
        
        self.rw_var("unknown_0xB0", "I", endianness='>')
        self.rw_var("unknown_0xB4", "I", endianness='>')
        self.rw_var("unknown_0xB8", "I", endianness='>')
        self.rw_var("unknown_0xBC", "I", endianness='>')
        
        self.rw_var("unknown_0xC0", "I", endianness='>')
        self.rw_var("unknown_0xC4", "I", endianness='>')
        self.rw_var("unknown_0xC8", "I", endianness='>')
        self.rw_var("unknown_0xCC", "I", endianness='>')
        
        self.rw_var("unknown_0xD0", "I", endianness='>')
        self.rw_var("unknown_0xD4", "I", endianness='>')
        self.rw_var("unknown_0xD8", "I", endianness='>')
        self.rw_var("unknown_0xDC", "I", endianness='>')
        
        self.rw_var("unknown_0xE0", "I", endianness='>')
        self.rw_var("unknown_0xE4", "I", endianness='>')
        self.rw_var("unknown_0xE8", "I", endianness='>')
        self.rw_var("unknown_0xEC", "I", endianness='>')
        
        self.rw_var("unknown_0xF0", "I", endianness='>')
        self.rw_var("unknown_0xF4", "I", endianness='>')
        self.rw_var("unknown_0xF8", "I", endianness='>')
        self.rw_var("unknown_0xFC", "I", endianness='>')
        
        self.rw_var("unknown_0x0100", "I", endianness='>')
        self.rw_var("unknown_0x0104", "I", endianness='>')
        self.rw_var("unknown_0x0108", "I", endianness='>')
        self.rw_var("unknown_0x010C", "I", endianness='>')
        
        self.rw_var("unknown_0x0110", "I", endianness='>')
        self.rw_var("unknown_0x0114", "I", endianness='>')
        self.rw_var("unknown_0x0118", "I", endianness='>')
        self.rw_var("unknown_0x011C", "I", endianness='>')
        
        self.rw_var("unknown_0x0120", "I", endianness='>')
        self.rw_var("unknown_0x0124", "I", endianness='>')
        self.rw_var("unknown_0x0128", "I", endianness='>')
        self.rw_var("unknown_0x012C", "I", endianness='>')
        
        self.rw_var("unknown_0x0130", "I", endianness='>')
        self.rw_var("unknown_0x0134", "I", endianness='>')
        self.rw_var("unknown_0x0138", "I", endianness='>')
        self.rw_var("unknown_0x013C", "I", endianness='>')
        
        self.rw_var("unknown_0x0140", "I", endianness='>')
        self.rw_var("unknown_0x0144", "I", endianness='>')
        self.rw_var("unknown_0x0148", "I", endianness='>')
        self.rw_var("unknown_0x014C", "I", endianness='>')
        
        self.rw_var("unknown_0x0150", "I", endianness='>')
        self.rw_var("unknown_0x0154", "I", endianness='>')
        self.rw_var("unknown_0x0158", "I", endianness='>')
        self.rw_var("unknown_0x015C", "I", endianness='>')
        
        self.rw_var("unknown_0x0160", "I", endianness='>')
        self.rw_var("unknown_0x0164", "I", endianness='>')
        self.rw_var("unknown_0x0168", "I", endianness='>')
        self.rw_var("unknown_0x016C", "I", endianness='>')
        
        self.rw_var("unknown_0x0170", "I", endianness='>')
        self.rw_var("unknown_0x0174", "I", endianness='>')
        self.rw_var("unknown_0x0178", "I", endianness='>')
        self.rw_var("unknown_0x017C", "I", endianness='>')
        
        self.rw_var("unknown_0x0180", "I", endianness='>')
        self.rw_var("unknown_0x0184", "I", endianness='>')
        self.rw_var("unknown_0x0188", "I", endianness='>')
        self.rw_var("unknown_0x018C", "I", endianness='>')
        
        self.rw_var("unknown_0x0190", "I", endianness='>')
        self.rw_var("unknown_0x0194", "I", endianness='>')
        self.rw_var("unknown_0x0198", "I", endianness='>')
        
        self.assert_is_zero("unknown_0x0198")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198 )   
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [                0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                 0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                 0x180, 0x184, 0x188, 0x18C, 0x190, 0x194
               ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                 0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                 0x180, 0x184, 0x188, 0x18C, 0x190, 0x194
               ]
    
class VlMxGeneralCharParamSetInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58
               ]
    
class VlMxJobInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='>')
        self.rw_var("unknown_0x78", "i", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='>')
        
        self.rw_var("unknown_0xD0", "i", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
        self.rw_var("unknown_0xF8", "i", endianness='>')
        self.rw_var("unknown_0xFC", "i", endianness='>')
        
        self.rw_var("unknown_0x0100", "i", endianness='>')
        self.rw_var("unknown_0x0104", "i", endianness='>')
        self.rw_var("unknown_0x0108", "i", endianness='>')
        self.rw_var("unknown_0x010C", "i", endianness='>')
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128, )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return [ 0x08, 0x0C, 0x10 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128
               ]
    
class VlMxMapObjectCommonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    
class VlMxMapObjectInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24
               ]
    
class VlMxNewsPaperInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14  ]
    
class VlMxOrderDirectionInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, )
    
    def asset_table_offsets(self):
        return [0x08]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08  ]
    
class VlMxOrderInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1A", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='<')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='<')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x54")
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04, 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1A, 0x1C,
                  0x20,         0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,         0x4C,  0x50
               ]
    
class VlMxParameterConvertTable(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "f", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "f", endianness='>')
        self.rw_var("unknown_0x48", "f", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
        self.rw_var("unknown_0x58", "f", endianness='>')
        self.rw_var("unknown_0x5C", "f", endianness='>')
        
        self.rw_var("unknown_0x60", "f", endianness='>')
        self.rw_var("unknown_0x64", "f", endianness='>')
        self.rw_var("unknown_0x68", "f", endianness='>')
        self.rw_var("unknown_0x6C", "f", endianness='>')
        
        self.rw_var("unknown_0x70", "f", endianness='>')
        self.rw_var("unknown_0x74", "f", endianness='>')
        self.rw_var("unknown_0x78", "f", endianness='>')
        self.rw_var("unknown_0x7C", "f", endianness='>')
        
        self.rw_var("unknown_0x80", "f", endianness='>')
        self.rw_var("unknown_0x84", "f", endianness='>')
        self.rw_var("unknown_0x88", "f", endianness='>')
        self.rw_var("unknown_0x8C", "f", endianness='>')
        
        self.rw_var("unknown_0x90", "f", endianness='>')
        self.rw_var("unknown_0x94", "f", endianness='>')
        self.rw_var("unknown_0x98", "f", endianness='>')
        self.rw_var("unknown_0x9C", "f", endianness='>')
        
        self.rw_var("unknown_0xA0", "f", endianness='>')
        self.rw_var("unknown_0xA4", "f", endianness='>')
        self.rw_var("unknown_0xA8", "f", endianness='>')
        self.rw_var("unknown_0xAC", "f", endianness='>')
        
        self.rw_var("unknown_0xB0", "f", endianness='>')
        self.rw_var("unknown_0xB4", "f", endianness='>')
        
        self.assert_is_zero("unknown_0xB4")
    
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0
               ]
    
class VlMxPotentialInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='<')
        
        
        self.rw_var("unknown_0x10", "i", endianness='<')
        self.rw_var("unknown_0x14", "i", endianness='<')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04, 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,                       0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,
               ]
    
class VlMxSlgInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
        self.rw_var("unknown_0x20", "q", endianness='>')
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18, 
                 self.unknown_0x20,)
    
    def asset_table_offsets(self):
        return [0x18, 0x20]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,
                  0x20
               ]
        
class VlMxSlgLandformInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10  ]

class VlMxSlgStrongholdCommonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28
               ]
  
class VlMxUnitCommonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "f", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "f", endianness='>')
        self.rw_var("unknown_0x48", "f", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
        self.rw_var("unknown_0x58", "f", endianness='>')
        self.rw_var("unknown_0x5C", "f", endianness='>')
        
        self.rw_var("unknown_0x60", "f", endianness='>')
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60
               ]
    
class VlMxUnitGrowthTypeInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C  ]
    
class VlMxVehicleCommonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20
               ]
    
class VlMxVehicleDevChangeParamInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04 )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04  ]
    

class VlMxVehicleDevInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "h", endianness='>')
        self.rw_var("unknown_0x2E", "h", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='<')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='<')
        
        
        self.rw_var("unknown_0x50", "i", endianness='<')
        self.rw_var("unknown_0x54", "h", endianness='<')
        self.rw_var("unknown_0x56", "h", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='<')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  
                 self.unknown_0x28,                      self.unknown_0x2C,  self.unknown_0x2E,
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x00, 0x04, 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x2E,
                  0x30,         0x38,  0x3C, 
                  0x40,  0x44,  0x48,                0x56,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70
               ]
    
class VlMxVehicleEachInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
        self.rw_var("unknown_0x58", "f", endianness='>')
        self.rw_var("unknown_0x5C", "f", endianness='>')
        
        self.assert_is_zero("unknown_0x50")
        self.assert_is_zero("unknown_0x54")
        self.assert_is_zero("unknown_0x58")
        
        self.rw_var("unknown_0x60", "f", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='>')
        self.rw_var("unknown_0x78", "i", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='>')
        
        self.rw_var("unknown_0xD0", "i", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
        self.rw_var("unknown_0xF8", "i", endianness='>')
        self.rw_var("unknown_0xFC", "i", endianness='>')
        
        self.rw_var("unknown_0x0100", "i", endianness='>')
        self.rw_var("unknown_0x0104", "i", endianness='>')
        self.rw_var("unknown_0x0108", "i", endianness='>')
        self.rw_var("unknown_0x010C", "i", endianness='>')
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "i", endianness='>')
        self.rw_var("unknown_0x014C", "i", endianness='>')
        
        self.rw_var("unknown_0x0150", "i", endianness='>')
        self.rw_var("unknown_0x0154", "i", endianness='>')
        self.rw_var("unknown_0x0158", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158, )
    
    def asset_table_offsets(self):
        return []
        
    def pof0_offsets(self):
        return [ 0x18, 0x24, 0x28, 0x2C, 0x30, 0x34 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,                       0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158
               ]

class VlMxVehicleInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
        self.rw_var("unknown_0x58", "f", endianness='>')
        self.rw_var("unknown_0x5C", "f", endianness='>')
        
        self.rw_var("unknown_0x60", "f", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='<')
        
        
        self.rw_var("unknown_0xB0", "i", endianness='<')
        self.rw_var("unknown_0xB4", "i", endianness='<')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
  
  
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='<')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC)
    
    def asset_table_offsets(self):
        return [0x70, 0x78]
        
    def pof0_offsets(self):
        return [ 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x24, 0x28 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,         0x78,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,                       0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8
               ]
    
class VlMxWeaponBringOnUnwholesomeInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10, )
    
    def asset_table_offsets(self):
        return []        
    
    def pof0_offsets(self):
        return [ ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10  ]

class VlMxWeaponCommonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, )
    
    def asset_table_offsets(self):
        return []      
    
    def pof0_offsets(self):
        return [ ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04  ]

class VlMxWeaponInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
        self.rw_var("unknown_0x58", "f", endianness='>')
        self.rw_var("unknown_0x5C", "f", endianness='>')
        
        self.rw_var("unknown_0x60", "f", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='>')
        self.rw_var("unknown_0x78", "i", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='>')
        
        self.rw_var("unknown_0xD0", "i", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC,
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC,
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC,
                 self.unknown_0xF0,  self.unknown_0xF4)
    
    def asset_table_offsets(self):
        return [0x08, 0x10]     
    
    def pof0_offsets(self):
        return [ 0x00, 0x04  ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,         0x10,         0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4
               ]

class VlMxBookDecorationInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14, )

class VlMxBookHistoryInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "f", endianness='>')
        self.rw_var("unknown_0x54", "f", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54 )

  
class VlMxBookPersonInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.rw_var("unknown_0x30", "I", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "I", endianness='>')
        self.rw_var("unknown_0x74", "I", endianness='>')
        self.rw_var("unknown_0x78", "I", endianness='>')
        self.rw_var("unknown_0x7C", "I", endianness='>')
        
        self.rw_var("unknown_0x80", "I", endianness='>')
        self.rw_var("unknown_0x84", "I", endianness='>')
        self.rw_var("unknown_0x88", "I", endianness='>')
        self.rw_var("unknown_0x8C", "I", endianness='>')
        
        self.rw_var("unknown_0x90", "I", endianness='>')
        self.rw_var("unknown_0x94", "I", endianness='>')
        self.rw_var("unknown_0x98", "I", endianness='>')
        self.rw_var("unknown_0x9C", "I", endianness='>')
        
        self.rw_var("unknown_0xA0", "I", endianness='>')
        self.rw_var("unknown_0xA4", "I", endianness='>')
        self.rw_var("unknown_0xA8", "I", endianness='>')
        self.rw_var("unknown_0xAC", "I", endianness='>')
        
        self.rw_var("unknown_0xB0", "I", endianness='>')
        self.rw_var("unknown_0xB4", "I", endianness='>')
        self.rw_var("unknown_0xB8", "I", endianness='>')
        self.rw_var("unknown_0xBC", "I", endianness='>')
        
        self.rw_var("unknown_0xC0", "I", endianness='>')
        self.rw_var("unknown_0xC4", "I", endianness='>')
        self.rw_var("unknown_0xC8", "I", endianness='>')
        self.rw_var("unknown_0xCC", "I", endianness='>')
        
        self.rw_var("unknown_0xD0", "I", endianness='>')
        self.rw_var("unknown_0xD4", "I", endianness='>')
        self.rw_var("unknown_0xD8", "I", endianness='>')
        self.rw_var("unknown_0xDC", "I", endianness='>')
        
        self.rw_var("unknown_0xE0", "I", endianness='>')
        self.rw_var("unknown_0xE4", "I", endianness='>')
        self.rw_var("unknown_0xE8", "I", endianness='>')
        self.rw_var("unknown_0xEC", "I", endianness='>')
        
        self.rw_var("unknown_0xF0", "I", endianness='>')
        self.rw_var("unknown_0xF4", "I", endianness='>')
        self.rw_var("unknown_0xF8", "I", endianness='>')
        self.rw_var("unknown_0xFC", "I", endianness='>')
        
        self.rw_var("unknown_0x0100", "I", endianness='>')
        self.rw_var("unknown_0x0104", "I", endianness='>')
        self.rw_var("unknown_0x0108", "I", endianness='>')
        self.rw_var("unknown_0x010C", "I", endianness='>')
        
        self.rw_var("unknown_0x0110", "I", endianness='>')
        self.rw_var("unknown_0x0114", "I", endianness='>')
        self.rw_var("unknown_0x0118", "I", endianness='>')
        self.rw_var("unknown_0x011C", "I", endianness='>')
        
        self.rw_var("unknown_0x0120", "I", endianness='>')
        self.rw_var("unknown_0x0124", "I", endianness='>')
        self.rw_var("unknown_0x0128", "I", endianness='>')
        self.rw_var("unknown_0x012C", "I", endianness='>')
        
        self.rw_var("unknown_0x0130", "I", endianness='>')
        self.rw_var("unknown_0x0134", "I", endianness='>')
        self.rw_var("unknown_0x0138", "I", endianness='>')
        self.rw_var("unknown_0x013C", "I", endianness='>')
        
        self.rw_var("unknown_0x0140", "I", endianness='>')
        self.rw_var("unknown_0x0144", "I", endianness='>')
        self.rw_var("unknown_0x0148", "I", endianness='>')
        self.rw_var("unknown_0x014C", "I", endianness='>')
        
        self.rw_var("unknown_0x0150", "I", endianness='>')
        self.rw_var("unknown_0x0154", "I", endianness='>')
        self.rw_var("unknown_0x0158", "I", endianness='>')
        self.rw_var("unknown_0x015C", "I", endianness='>')
        
        self.rw_var("unknown_0x0160", "I", endianness='>')
        self.rw_var("unknown_0x0164", "I", endianness='>')
        self.rw_var("unknown_0x0168", "I", endianness='>')
        self.rw_var("unknown_0x016C", "I", endianness='>')
        
        self.rw_var("unknown_0x0170", "I", endianness='>')
        self.rw_var("unknown_0x0174", "I", endianness='>')
        self.rw_var("unknown_0x0178", "I", endianness='>')
        self.rw_var("unknown_0x017C", "I", endianness='>')
        
        self.rw_var("unknown_0x0180", "I", endianness='>')
        self.rw_var("unknown_0x0184", "I", endianness='>')
        self.rw_var("unknown_0x0188", "I", endianness='>')
        self.rw_var("unknown_0x018C", "I", endianness='>')
        
        self.rw_var("unknown_0x0190", "I", endianness='>')
        self.rw_var("unknown_0x0194", "I", endianness='>')
        self.rw_var("unknown_0x0198", "I", endianness='>')
        self.rw_var("unknown_0x019C", "I", endianness='>')
        
        self.rw_var("unknown_0x01A0", "I", endianness='>')
        self.rw_var("unknown_0x01A4", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198,  self.unknown_0x019C,
                 self.unknown_0x01A0,  self.unknown_0x01A4, )   
    
class VlMxBookSoundInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, )
    
    
class EnTalkEventObjParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "q", endianness='>')
        self.rw_var("unknown_0x38", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x38")
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x28, 
                 self.unknown_0x30,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C, 
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118
              ]
    
class EnEventDecorParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "I", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "I", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x108", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x110", "q", endianness='>')
        self.rw_var("unknown_0x118", "q", endianness='>')  # Padding
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,  
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,
                 self.unknown_0x70,  self.unknown_0x78,  
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,  
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,  
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,  
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,  
                 self.unknown_0x100, self.unknown_0x108,
                 self.unknown_0x110, self.unknown_0x118
                 )   
         
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110,]
    
class EnHeightMapParam(BaseRW):
    def read_write(self):
        # THESE ALL SEEM TO BE FLAGS
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "I", endianness='>')  # Padding
        
        self.rw_var("unknown_0x30", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "I", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "I", endianness='>')  # Padding
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,  
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,  
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,
                 self.unknown_0x70,  self.unknown_0x78,  
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,  
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,  
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,  
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 self.unknown_0x0100, self.unknown_0x0108,
                 self.unknown_0x0110, self.unknown_0x0118)
    

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0, 
                 0x110, 0x118,
                 ]
      
class EnSkyParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "q", endianness='>')
        self.rw_var("unknown_0x38", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x38")
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')  # Padding
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,
                 self.unknown_0x30,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110, 0x114 ]
      
class VlMxBookWeaponInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.rw_var("unknown_0x30", "I", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "I", endianness='>')
        self.rw_var("unknown_0x74", "I", endianness='>')
        self.rw_var("unknown_0x78", "I", endianness='>')
        self.rw_var("unknown_0x7C", "I", endianness='>')
        
        self.rw_var("unknown_0x80", "I", endianness='>')
        self.rw_var("unknown_0x84", "I", endianness='>')
        self.rw_var("unknown_0x88", "I", endianness='>')
        self.rw_var("unknown_0x8C", "I", endianness='>')
        
        self.rw_var("unknown_0x90", "I", endianness='>')
        self.rw_var("unknown_0x94", "I", endianness='>')
        self.rw_var("unknown_0x98", "I", endianness='>')
        self.rw_var("unknown_0x9C", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C )   
    
  
class VlMxCanvasShaderParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.rw_var("unknown_0x30", "I", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "I", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "I", endianness='>')
        self.rw_var("unknown_0x74", "I", endianness='>')
        self.rw_var("unknown_0x78", "I", endianness='>')
        self.rw_var("unknown_0x7C", "I", endianness='>')
        
        self.rw_var("unknown_0x80", "I", endianness='>')
        self.rw_var("unknown_0x84", "I", endianness='>')
        self.rw_var("unknown_0x88", "I", endianness='>')
        self.rw_var("unknown_0x8C", "I", endianness='>')
        
        self.rw_var("unknown_0x90", "I", endianness='>')
        self.rw_var("unknown_0x94", "I", endianness='>')
        self.rw_var("unknown_0x98", "I", endianness='>')
        self.rw_var("unknown_0x9C", "I", endianness='>')
        
        self.rw_var("unknown_0xA0", "I", endianness='>')
        self.rw_var("unknown_0xA4", "I", endianness='>')
        self.rw_var("unknown_0xA8", "I", endianness='>')
        self.rw_var("unknown_0xAC", "I", endianness='>')
        
        self.rw_var("unknown_0xB0", "I", endianness='>')
        self.rw_var("unknown_0xB4", "I", endianness='>')
        self.rw_var("unknown_0xB8", "I", endianness='>')
        self.rw_var("unknown_0xBC", "I", endianness='>')
        
        self.rw_var("unknown_0xC0", "I", endianness='>')
        self.rw_var("unknown_0xC4", "I", endianness='>')
        self.rw_var("unknown_0xC8", "I", endianness='>')
        self.rw_var("unknown_0xCC", "I", endianness='>')
        
        self.rw_var("unknown_0xD0", "I", endianness='>')
        self.rw_var("unknown_0xD4", "I", endianness='>')
        self.rw_var("unknown_0xD8", "I", endianness='>')
        self.rw_var("unknown_0xDC", "I", endianness='>')
        
        self.rw_var("unknown_0xE0", "I", endianness='>')
        self.rw_var("unknown_0xE4", "I", endianness='>')
        self.rw_var("unknown_0xE8", "I", endianness='>')
        self.rw_var("unknown_0xEC", "I", endianness='>')
        
        self.rw_var("unknown_0xF0", "I", endianness='>')
        self.rw_var("unknown_0xF4", "I", endianness='>')
        self.rw_var("unknown_0xF8", "I", endianness='>')
        self.rw_var("unknown_0xFC", "I", endianness='>')
        
        self.rw_var("unknown_0x0100", "I", endianness='>')
        self.rw_var("unknown_0x0104", "I", endianness='>')
        self.rw_var("unknown_0x0108", "I", endianness='>')
        self.rw_var("unknown_0x010C", "I", endianness='>')
        
        self.rw_var("unknown_0x0110", "I", endianness='>')
        self.rw_var("unknown_0x0114", "I", endianness='>')
        self.rw_var("unknown_0x0118", "I", endianness='>')
        self.rw_var("unknown_0x011C", "I", endianness='>')
        
        self.rw_var("unknown_0x0120", "I", endianness='>')
        self.rw_var("unknown_0x0124", "I", endianness='>')
        self.rw_var("unknown_0x0128", "I", endianness='>')
        self.rw_var("unknown_0x012C", "I", endianness='>')
        
        self.rw_var("unknown_0x0130", "I", endianness='>')
        self.rw_var("unknown_0x0134", "I", endianness='>')
        self.rw_var("unknown_0x0138", "I", endianness='>')
        self.rw_var("unknown_0x013C", "I", endianness='>')
        
        self.rw_var("unknown_0x0140", "I", endianness='>')
        self.rw_var("unknown_0x0144", "I", endianness='>')
        self.rw_var("unknown_0x0148", "I", endianness='>')
        self.rw_var("unknown_0x014C", "I", endianness='>')
        
        self.rw_var("unknown_0x0150", "I", endianness='>')
        self.rw_var("unknown_0x0154", "I", endianness='>')
        self.rw_var("unknown_0x0158", "I", endianness='>')
        self.rw_var("unknown_0x015C", "I", endianness='>')
        
        self.rw_var("unknown_0x0160", "I", endianness='>')
        self.rw_var("unknown_0x0164", "I", endianness='>')
        self.rw_var("unknown_0x0168", "I", endianness='>')
        self.rw_var("unknown_0x016C", "I", endianness='>')
        
        self.rw_var("unknown_0x0170", "I", endianness='>')
        self.rw_var("unknown_0x0174", "I", endianness='>')
        self.rw_var("unknown_0x0178", "I", endianness='>')
        self.rw_var("unknown_0x017C", "I", endianness='>')
        
        self.rw_var("unknown_0x0180", "I", endianness='>')
        self.rw_var("unknown_0x0184", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  )   
    
 
class MxParameterTextureMerge(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "q", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  )    
 
    def asset_table_offsets(self):
        return [0x00, 0x08]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08 ]
    
class MxParameterMergeFile(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "q", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x10")
        self.assert_is_zero("unknown_0x18")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  )
    
    def asset_table_offsets(self):
        return [0x00, 0x08]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08 ]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138]
    
class VlMxDrawModelLodParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14 ]
    
class VlMapObjectParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    
    
class EnTreeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", 'i', endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x013C")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x88, 
                 self.unknown_0x90,  self.unknown_0x98, 
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8, 
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C )   

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138]

class EnWaterSurfaceParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34)
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34]
  
class SlgEnGrassPathNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
                
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgMapObjectParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x04")
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  self.unknown_0x1C,  )
        
    def asset_table_offsets(self):
        return [0x08, 0x10]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08,  0x10,  0x18,  0x1C ]
  
class SlgEnGrassParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0124, self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144, self.unknown_0x0148,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]

    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144]
    
class StaticBox(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "f", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.assert_is_zero("unknown_0x44")
        self.assert_is_zero("unknown_0x48")
        self.assert_is_zero("unknown_0x4C")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [0x00, 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
                0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C,
                0x40]
    
class EnUvScrollParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0118")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110,]
    
    
class SlgEnBreakableStructureParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "q", endianness='>')
        self.rw_var("unknown_0x0148", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0148
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118, 0x120, 0x128, 0x140]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x148]
    
class EnConvexParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,)  
    
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110, 0x114, 0x118]
       
class EnCEffectParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
    
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x0128")
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88, 
                 self.unknown_0x90,  self.unknown_0x98, 
                 self.unknown_0xA0,  self.unknown_0xA8,
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8, 
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,)  
          
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120,]
    
class VlMxBriefingInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='<')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "I", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.rw_var("unknown_0x30", "I", endianness='>')
        self.rw_var("unknown_0x34", "I", endianness='>')
        self.rw_var("unknown_0x38", "I", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "I", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
        
        self.rw_var("unknown_0x50", "I", endianness='>')
        self.rw_var("unknown_0x54", "I", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='>')
        self.rw_var("unknown_0x78", "i", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='>')
        
        self.rw_var("unknown_0xD0", "i", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
        self.rw_var("unknown_0xF8", "I", endianness='>')
        self.rw_var("unknown_0xFC", "i", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC,)
   
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [            0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
                0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C,
                0x40, 0x44, 0x48, 0x4C, 0x50, 0x54,
                0xF8
               ]
    
    def enrs_offsets(self):
        return [ 0x00,         0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                 0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                 0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                 0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                 0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC
               ]

class VlMxFieldInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "q", endianness='>')
        
        self.rw_var("unknown_0x40", "q", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54 )
    
    def asset_table_offsets(self):
        return [0x08, 0x10, 0x40]
        
    
    def pof0_offsets(self):
        return [ 0x00, 0x04, 0x1C ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,         0x10,         0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,
                 0x40,  0x48,  0x4C,  0x50,  0x54
               ]
          
class VlMxResultInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='<')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,         0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C
               ]
  
    
class VlMxStageInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='<')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "I", endianness='>')
        
        self.rw_var("unknown_0x60", "I", endianness='>')
        self.rw_var("unknown_0x64", "I", endianness='>')
        self.rw_var("unknown_0x68", "I", endianness='>')
        self.rw_var("unknown_0x6C", "I", endianness='>')
        
        self.rw_var("unknown_0x70", "I", endianness='>')
        self.rw_var("unknown_0x74", "I", endianness='>')
        self.rw_var("unknown_0x78", "I", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "I", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "I", endianness='>')
        self.rw_var("unknown_0xCC", "I", endianness='>')
        
        self.rw_var("unknown_0xD0", "I", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
        self.rw_var("unknown_0xF8", "i", endianness='>')
        self.rw_var("unknown_0xFC", "i", endianness='>')
        
        self.rw_var("unknown_0x0100", "i", endianness='>')
        self.rw_var("unknown_0x0104", "i", endianness='>')
        self.rw_var("unknown_0x0108", "i", endianness='>')
        self.rw_var("unknown_0x010C", "i", endianness='>')
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "i", endianness='>')
        self.rw_var("unknown_0x014C", "i", endianness='>')
        
        self.rw_var("unknown_0x0150", "i", endianness='>')
        self.rw_var("unknown_0x0154", "i", endianness='>')
        self.rw_var("unknown_0x0158", "i", endianness='>')
        self.rw_var("unknown_0x015C", "i", endianness='>')
        
        self.rw_var("unknown_0x0160", "i", endianness='>')
        self.rw_var("unknown_0x0164", "i", endianness='>')
        self.rw_var("unknown_0x0168", "i", endianness='>')
        self.rw_var("unknown_0x016C", "i", endianness='>')
        
        self.rw_var("unknown_0x0170", "i", endianness='>')
        self.rw_var("unknown_0x0174", "i", endianness='>')
        self.rw_var("unknown_0x0178", "i", endianness='>')
        self.rw_var("unknown_0x017C", "i", endianness='>')
        
        self.rw_var("unknown_0x0180", "i", endianness='>')
        self.rw_var("unknown_0x0184", "i", endianness='>')
        self.rw_var("unknown_0x0188", "i", endianness='>')
        self.rw_var("unknown_0x018C", "h", endianness='>')
        self.rw_var("unknown_0x018E", "h", endianness='>')
        
        self.rw_var("unknown_0x0190", "i", endianness='>')
        self.rw_var("unknown_0x0194", "i", endianness='>')
        self.rw_var("unknown_0x0198", "i", endianness='>')
        self.rw_var("unknown_0x019C", "i", endianness='>')
        
        self.rw_var("unknown_0x01A0", "i", endianness='>')
        self.rw_var("unknown_0x01A4", "i", endianness='>')
        self.rw_var("unknown_0x01A8", "i", endianness='>')
        self.rw_var("unknown_0x01AC", "i", endianness='>')
        
        self.rw_var("unknown_0x01B0", "i", endianness='>')
        self.rw_var("unknown_0x01B4", "i", endianness='>')
        self.rw_var("unknown_0x01B8", "i", endianness='>')
        self.rw_var("unknown_0x01BC", "i", endianness='>')
        
        self.rw_var("unknown_0x01C0", "i", endianness='>')
        self.rw_var("unknown_0x01C4", "i", endianness='>')
        self.rw_var("unknown_0x01C8", "i", endianness='>')
        self.rw_var("unknown_0x01CC", "i", endianness='>')
        
        self.rw_var("unknown_0x01D0", "i", endianness='>')
        self.rw_var("unknown_0x01D4", "i", endianness='>')
        self.rw_var("unknown_0x01D8", "i", endianness='>')
        self.rw_var("unknown_0x01DC", "i", endianness='>')
        
        self.rw_var("unknown_0x01E0", "i", endianness='>')
        self.rw_var("unknown_0x01E4", "h", endianness='>')
        self.rw_var("unknown_0x01E6", "h", endianness='>')
        self.rw_var("unknown_0x01E8", "h", endianness='>')
        self.rw_var("unknown_0x01EA", "h", endianness='>')
        self.rw_var("unknown_0x01EC", "h", endianness='>')
        self.rw_var("unknown_0x01EE", "h", endianness='>')
        
        self.rw_var("unknown_0x01F0", "h", endianness='>')
        self.rw_var("unknown_0x01F2", "h", endianness='>')
        self.rw_var("unknown_0x01F4", "h", endianness='>')
        self.rw_var("unknown_0x01F6", "h", endianness='>')
        self.rw_var("unknown_0x01F8", "h", endianness='>')
        self.rw_var("unknown_0x01FA", "h", endianness='>')
        self.rw_var("unknown_0x01FC", "h", endianness='>')
        self.rw_var("unknown_0x01FE", "h", endianness='>')
        
        self.rw_var("unknown_0x0200", "h", endianness='>')
        self.rw_var("unknown_0x0202", "h", endianness='>')
        self.rw_var("unknown_0x0204", "h", endianness='>')
        self.rw_var("unknown_0x0206", "h", endianness='>')
        self.rw_var("unknown_0x0208", "h", endianness='>')
        self.rw_var("unknown_0x020A", "h", endianness='>')
        self.rw_var("unknown_0x020C", "i", endianness='>')
        
        self.rw_var("unknown_0x0210", "i", endianness='>')
        self.rw_var("unknown_0x0214", "h", endianness='>')
        self.rw_var("unknown_0x0216", "h", endianness='>')
        self.rw_var("unknown_0x0218", "i", endianness='>')
        self.rw_var("unknown_0x021C", "i", endianness='>')
        
        self.rw_var("unknown_0x0220", "i", endianness='>')
        self.rw_var("unknown_0x0224", "i", endianness='>')
        self.rw_var("unknown_0x0228", "i", endianness='>')
        self.rw_var("unknown_0x022C", "i", endianness='>')
        
        self.rw_var("unknown_0x0230", "i", endianness='>')
        self.rw_var("unknown_0x0234", "i", endianness='>')
        self.rw_var("unknown_0x0238", "i", endianness='>')
        self.rw_var("unknown_0x023C", "i", endianness='>')
        
        self.rw_var("unknown_0x0240", "i", endianness='>')
        self.rw_var("unknown_0x0244", "i", endianness='>')
        self.rw_var("unknown_0x0248", "i", endianness='>')
        self.rw_var("unknown_0x024C", "i", endianness='>')
        
        self.rw_var("unknown_0x0250", "i", endianness='>')
        self.rw_var("unknown_0x0254", "i", endianness='>')
        self.rw_var("unknown_0x0258", "i", endianness='>')
        self.rw_var("unknown_0x025C", "i", endianness='>')
        
        self.rw_var("unknown_0x0260", "i", endianness='>')
        self.rw_var("unknown_0x0264", "i", endianness='>')
        self.rw_var("unknown_0x0268", "i", endianness='>')
        self.rw_var("unknown_0x026C", "h", endianness='>')
        self.rw_var("unknown_0x026E", "h", endianness='>')
        
        self.rw_var("unknown_0x0270", "h", endianness='>')
        self.rw_var("unknown_0x0272", "h", endianness='>')
        self.rw_var("unknown_0x0274", "h", endianness='>')
        self.rw_var("unknown_0x0276", "h", endianness='>')
        self.rw_var("unknown_0x0278", "h", endianness='>')
        self.rw_var("unknown_0x027A", "h", endianness='>')
        self.rw_var("unknown_0x027C", "h", endianness='>')
        self.rw_var("unknown_0x027E", "h", endianness='>')
        
        self.rw_var("unknown_0x0280", "h", endianness='>')
        self.rw_var("unknown_0x0282", "h", endianness='>')
        self.rw_var("unknown_0x0284", "h", endianness='>')
        self.rw_var("unknown_0x0286", "h", endianness='>')
        self.rw_var("unknown_0x0288", "h", endianness='>')
        self.rw_var("unknown_0x028A", "h", endianness='>')
        self.rw_var("unknown_0x028C", "h", endianness='>')
        self.rw_var("unknown_0x028E", "h", endianness='>')
        
        self.rw_var("unknown_0x0290", "h", endianness='>')
        self.rw_var("unknown_0x0292", "h", endianness='>')
        self.rw_var("unknown_0x0294", "i", endianness='>')
        self.rw_var("unknown_0x0298", "i", endianness='>')
        self.rw_var("unknown_0x029C", "i", endianness='>')
        
        self.rw_var("unknown_0x02A0", "i", endianness='>')
        self.rw_var("unknown_0x02A4", "i", endianness='>')
        self.rw_var("unknown_0x02A8", "i", endianness='>')
        self.rw_var("unknown_0x02AC", "i", endianness='>')
        
        self.rw_var("unknown_0x02B0", "i", endianness='>')
        self.rw_var("unknown_0x02B4", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x18, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C, 
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C, 
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C, 
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C, 
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C, 
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C, 
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C, 
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C, 
                 
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C, self.unknown_0x018E,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198,  self.unknown_0x019C, 
                 self.unknown_0x01A0,  self.unknown_0x01A4,  self.unknown_0x01A8,  self.unknown_0x01AC, 
                 self.unknown_0x01B0,  self.unknown_0x01B4,  self.unknown_0x01B8,  self.unknown_0x01BC,
                 self.unknown_0x01C0,  self.unknown_0x01C4,  self.unknown_0x01C8,  self.unknown_0x01CC, 
                 self.unknown_0x01D0,  self.unknown_0x01D4,  self.unknown_0x01D8,  self.unknown_0x01DC, 
                 self.unknown_0x01E0,  self.unknown_0x01E4,  self.unknown_0x01E6,  
                 self.unknown_0x01E8,  self.unknown_0x01EA,  self.unknown_0x01EC,  self.unknown_0x01EE,
                 self.unknown_0x01F0,  self.unknown_0x01F2,  self.unknown_0x01F4,  self.unknown_0x01F6, 
                 self.unknown_0x01F8,  self.unknown_0x01FA,  self.unknown_0x01FC,  self.unknown_0x01FE,
                 
                 self.unknown_0x0200,  self.unknown_0x0202,  self.unknown_0x0204,  self.unknown_0x0206,
                 self.unknown_0x0208,  self.unknown_0x020A,  self.unknown_0x020C, 
                 self.unknown_0x0210,  self.unknown_0x0214,  self.unknown_0x0216,
                 self.unknown_0x0218,  self.unknown_0x021C, 
                 self.unknown_0x0220,  self.unknown_0x0224,  self.unknown_0x0228,  self.unknown_0x022C, 
                 self.unknown_0x0230,  self.unknown_0x0234,  self.unknown_0x0238,  self.unknown_0x023C, 
                 self.unknown_0x0240,  self.unknown_0x0244,  self.unknown_0x0248,  self.unknown_0x024C, 
                 self.unknown_0x0250,  self.unknown_0x0254,  self.unknown_0x0258,  self.unknown_0x025C, 
                 self.unknown_0x0260,  self.unknown_0x0264,  
                 self.unknown_0x0268,  self.unknown_0x026C,  self.unknown_0x026E,
                 self.unknown_0x0270,  self.unknown_0x0272,  self.unknown_0x0274,  self.unknown_0x0276, 
                 self.unknown_0x0278,  self.unknown_0x027A,  self.unknown_0x027C,  self.unknown_0x027E,
                
                 self.unknown_0x0280,  self.unknown_0x0282,  self.unknown_0x0284,  self.unknown_0x0286,
                 self.unknown_0x0288,  self.unknown_0x028A,  self.unknown_0x028C,  self.unknown_0x028E,
                 
                 self.unknown_0x0290,  self.unknown_0x0292,  self.unknown_0x0294,  
                 self.unknown_0x0298,  self.unknown_0x029C, 
                 self.unknown_0x02A0,  self.unknown_0x02A4,  self.unknown_0x02A8,  self.unknown_0x02AC, 
                 self.unknown_0x02B0,  self.unknown_0x02B4,  
                 )
    
    def asset_table_offsets(self):
        return [0x10, 0x18]   
    
    def pof0_offsets(self):
        return [ 0x5C, 
                 0x60, 0x64, 0x68, 0x6C, 0x70, 0x74, 0x78, 
                 0xA8, 0xC8, 0xCC, 0xD0 
               ]
    
    def enrs_offsets(self):
        return [  0x00,         0x08,  0x0C,  0x10,         0x18,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                 0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                 0x180, 0x184, 0x188, 0x18C, 0x18E, 
                 0x190, 0x194, 0x198, 0x19C, 0x1A0, 0x1A4, 0x1A8, 0x1AC,
                 0x1B0, 0x1B4, 0x1B8, 0x1BC, 0x1C0, 0x1C4, 0x1C8, 0x1CC,
                 0x1D0, 0x1D4, 0x1D8, 0x1DC, 
                 0x1E0, 0x1E4, 0x1E6, 0x1E8, 0x1EA, 0x1EC, 0x1EE,
                 0x1F0, 0x1F2, 0x1F4, 0x1F6, 0x1F8, 0x1FA, 0x1FC, 0x1FE,
                 0x200, 0x202, 0x204, 0x206, 0x208, 0x20A, 0x20C,
                 0x210,        0x214, 0x216, 0x218,        0x21C,
                 0x220, 0x224, 0x228, 0x22C, 0x230, 0x234, 0x238, 0x23C,
                 0x240, 0x244, 0x248, 0x24C, 0x250, 0x254, 0x258, 0x25C,
                 0x260,        0x264,        0x268,        0x26C, 0x26E,
                 0x270, 0x272, 0x274, 0x276, 0x278, 0x27A, 0x27C, 0x27E,
                 0x280, 0x282, 0x284, 0x286, 0x288, 0x28A, 0x28C, 0x28E,
                 0x290, 0x292, 0x294,        0x298,        0x29C,
                 0x2A0, 0x2A4, 0x2A8, 0x2AC, 0x2B0, 0x2B4
               ]
    
class VlMxCountryInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08)
        
class VlMxSlgCameraInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  )
  
    
class VlMxSlgCommandCursorInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C )
   
    
class VlMxTargetModeGazeFixedInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30 )
  
class VlMxPhysicsMaterialInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C )
    
class VlMxSurroundInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C )  


class MxParameterPvs(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "q", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18, )  
    
    def asset_table_offsets(self):
        return [0x00]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00, ]
    
class SlgEnStrongholdPathNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnStrongholdParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.rw_var("unknown_0x0130", "q", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
        self.rw_var("unknown_0x0140", "q", endianness='>')
        self.rw_var("unknown_0x0148", "i", endianness='>')
        self.rw_var("unknown_0x014C", "i", endianness='>')
        
        self.rw_var("unknown_0x0150", "i", endianness='>')
        self.rw_var("unknown_0x0154", "i", endianness='>')
        self.rw_var("unknown_0x0158", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138,
                 self.unknown_0x0140,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154, self.unknown_0x0158
                 )

    def asset_table_offsets(self):
        return [ 0x70,  0x78,  0x80,  0x88,  0x90,  0x98,  0xa0, 0xa8, 
                0x110, 0x118, 0x120, 0x128, 0x130, 0x138, 0x140       ]
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x138,
                0x140, 0x148, 0x14C,
                0x150, 0x154, 0x158
               ]

class EnWindmillParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "i", endianness='>')
        self.rw_var("unknown_0x014C", "i", endianness='>')
        
        self.rw_var("unknown_0x0150", "i", endianness='>')
        self.rw_var("unknown_0x0154", "i", endianness='>')
        self.rw_var("unknown_0x0158", "i", endianness='>')
        self.rw_var("unknown_0x015C", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124, self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144, self.unknown_0x0148, self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154, self.unknown_0x0158, self.unknown_0x015C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148, 0x14C,
                0x150, 0x154]
    
class AISlgUnitMxParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')  # Ptr
        self.rw_var("unknown_0x04", "I", endianness='>')  # Ptr
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "i", endianness='>')
        self.rw_var("unknown_0x74", "i", endianness='>')
        self.rw_var("unknown_0x78", "i", endianness='>')
        self.rw_var("unknown_0x7C", "i", endianness='>')
        
        self.rw_var("unknown_0x80", "i", endianness='>')
        self.rw_var("unknown_0x84", "i", endianness='>')
        self.rw_var("unknown_0x88", "i", endianness='>')
        self.rw_var("unknown_0x8C", "i", endianness='>')
        
        self.rw_var("unknown_0x90", "i", endianness='>')
        self.rw_var("unknown_0x94", "i", endianness='>')
        self.rw_var("unknown_0x98", "i", endianness='>')
        self.rw_var("unknown_0x9C", "i", endianness='>')
        
        self.rw_var("unknown_0xA0", "i", endianness='>')
        self.rw_var("unknown_0xA4", "i", endianness='>')
        self.rw_var("unknown_0xA8", "i", endianness='>')
        self.rw_var("unknown_0xAC", "i", endianness='>')
        
        self.rw_var("unknown_0xB0", "i", endianness='>')
        self.rw_var("unknown_0xB4", "i", endianness='>')
        self.rw_var("unknown_0xB8", "i", endianness='>')
        self.rw_var("unknown_0xBC", "i", endianness='>')
        
        self.rw_var("unknown_0xC0", "i", endianness='>')
        self.rw_var("unknown_0xC4", "i", endianness='>')
        self.rw_var("unknown_0xC8", "i", endianness='>')
        self.rw_var("unknown_0xCC", "i", endianness='>')
        
        self.rw_var("unknown_0xD0", "i", endianness='>')
        self.rw_var("unknown_0xD4", "i", endianness='>')
        self.rw_var("unknown_0xD8", "i", endianness='>')
        self.rw_var("unknown_0xDC", "i", endianness='>')
        
        self.rw_var("unknown_0xE0", "i", endianness='>')
        self.rw_var("unknown_0xE4", "i", endianness='>')
        self.rw_var("unknown_0xE8", "i", endianness='>')
        self.rw_var("unknown_0xEC", "i", endianness='>')
        
        self.rw_var("unknown_0xF0", "i", endianness='>')
        self.rw_var("unknown_0xF4", "i", endianness='>')
        self.rw_var("unknown_0xF8", "i", endianness='>')
        self.rw_var("unknown_0xFC", "i", endianness='>')
        
        self.rw_var("unknown_0x0100", "i", endianness='>')
        self.rw_var("unknown_0x0104", "i", endianness='>')
        self.rw_var("unknown_0x0108", "i", endianness='>')
        self.rw_var("unknown_0x010C", "i", endianness='>')
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C, 
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C, 
                 self.unknown_0x0120,  self.unknown_0x0124, )
    

    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return [0x00, 0x04]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                 0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                 0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                 0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                 0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124]
    
class SlgEnUnitPlacementPointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
                
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100, self.unknown_0x0108,
                 self.unknown_0x0110, self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120, self.unknown_0x0124, self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130, self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140, self.unknown_0x0144, self.unknown_0x0148
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148
               ]
    
class SlgEnMedicPointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnWarpPointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
                
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0128")
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "q", endianness='>')
        self.rw_var("unknown_0x0148", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0148")
        
        self.rw_var("unknown_0x0150", "i", endianness='>')
        self.rw_var("unknown_0x0154", "i", endianness='>')
        self.rw_var("unknown_0x0158", "i", endianness='>')
        self.rw_var("unknown_0x015C", "i", endianness='>')
        
        self.rw_var("unknown_0x0160", "q", endianness='>')
        self.rw_var("unknown_0x0168", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0168")
        
        self.rw_var("unknown_0x0170", "i", endianness='>')
        self.rw_var("unknown_0x0174", "i", endianness='>')
        self.rw_var("unknown_0x0178", "i", endianness='>')
        self.rw_var("unknown_0x017C", "i", endianness='>')
        
        self.rw_var("unknown_0x0180", "q", endianness='>')
        self.rw_var("unknown_0x0188", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0188")
        
        self.rw_var("unknown_0x0190", "i", endianness='>')
        self.rw_var("unknown_0x0194", "i", endianness='>')
        self.rw_var("unknown_0x0198", "i", endianness='>')
        self.rw_var("unknown_0x019C", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0114, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0148,
                 self.unknown_0x0150,  self.unknown_0x0154, self.unknown_0x0158, self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0168,
                 self.unknown_0x0170,  self.unknown_0x0174, self.unknown_0x0178, self.unknown_0x017C,
                 self.unknown_0x0180,  self.unknown_0x0188,
                 self.unknown_0x0190,  self.unknown_0x0194, self.unknown_0x0198, self.unknown_0x019C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120,
                0x130, 0x134, 0x138, 0x13C,
                0x140,
                0x150, 0x154, 0x158, 0x15C,
                0x160, 
                0x170, 0x174, 0x178, 0x17C,
                0x180,
                0x190, 0x194, 0x198, 0x19C
               ]
    
class SlgEnExplosiveParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    
class SlgEnTriggerBaseParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
                
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
        self.rw_var("unknown_0x0140", "i", endianness='>')
        self.rw_var("unknown_0x0144", "i", endianness='>')
        self.rw_var("unknown_0x0148", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100, self.unknown_0x0108,
                 self.unknown_0x0110, self.unknown_0x0118,
                 self.unknown_0x0120, self.unknown_0x0128,
                 self.unknown_0x0130, self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140, self.unknown_0x0144, self.unknown_0x0148
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118, 0x120, 0x128]
          
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148
               ]
    
class SlgEnMineParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x04")
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18 )
    
    def asset_table_offsets(self):
        return [0x08, 0x10]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08,  0x10,  0x18
               ]

class SlgEnAreaSurveillancePathNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0]
    

class SlgEnAreaSurveillanceParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0118")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110]
    
class EnMovePathNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100, self.unknown_0x0108,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class EnMovePathParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>') # Padding 
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118
               ]
    
    
class SlgEnReinforcePointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.rw_var("unknown_0x0130", "q", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0138")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130
               ]

class SlgEnGregoalStayPointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0118")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110
              ]
      
class SlgEnGregoalParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.rw_var("unknown_0x0130", "q", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
        self.rw_var("unknown_0x0140", "q", endianness='>')
        self.rw_var("unknown_0x0148", "q", endianness='>')
        
        self.rw_var("unknown_0x0150", "q", endianness='>')
        self.rw_var("unknown_0x0158", "q", endianness='>')
        
        self.rw_var("unknown_0x0160", "q", endianness=">")
        self.rw_var("unknown_0x0168", "q", endianness=">")
        
        self.assert_is_zero("unknown_0x0168")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138,
                 self.unknown_0x0140,  self.unknown_0x0148,
                 self.unknown_0x0150,  self.unknown_0x0158,
                 self.unknown_0x0160,  self.unknown_0x0168
                 )

    def asset_table_offsets(self):
        return [              0x70,   0x78,  0x80,  0x88,  0x90,  0x98,  0xa0,  0xa8,
                0x110, 0x118, 0x120, 0x128, 0x130, 0x138, 0x140, 0x148, 0x150, 0x158 ]

    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x138,
                0x140, 0x148,
                0x150, 0x158,
                0x160
              ]

class SlgEnDummyTankParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]

class SlgEnBreakableBridgeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    

class SlgEnControlLancePieceParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C)
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]

class SlgEnDefenseWallParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "h", endianness='>')
        self.rw_var("unknown_0x02", "h", endianness='>')
        self.rw_var("unknown_0x04", "h", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00, self.unknown_0x04,)
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x02, 0x04, ]
    
class SlgEnTemplePartsParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18, )
    
    def asset_table_offsets(self):
        return [0x08, 0x10, 0x18]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x10,  0x18 ]
    

class SlgEnLancePieceParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]
    
class SlgEnTowerParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08 )
    
    def asset_table_offsets(self):
        return []
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08 ]
    
      
class VlMxUnitResourceInfo(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "q", endianness='>')
        
        self.rw_var("unknown_0x20", "q", endianness='>')
        self.rw_var("unknown_0x28", "q", endianness='>')
        
        self.rw_var("unknown_0x30", "q", endianness='>')
        self.rw_var("unknown_0x38", "q", endianness='>')
        
        self.rw_var("unknown_0x40", "q", endianness='>')
        self.rw_var("unknown_0x48", "q", endianness='>')
        
        self.rw_var("unknown_0x50", "q", endianness='>')
        self.rw_var("unknown_0x58", "q", endianness='>')
        
        self.rw_var("unknown_0x60", "q", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x18, 
                 self.unknown_0x20,  self.unknown_0x28, 
                 self.unknown_0x30,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x48, 
                 self.unknown_0x50,  self.unknown_0x58, 
                 self.unknown_0x60,)
    
    def asset_table_offsets(self):
        return [0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0x40, 0x48, 0x50, 0x58, 0x60]

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x18,
                  0x20,  0x28,  0x30,  0x38,  0x40,  0x48,  0x50,  0x58, 
                  0x60
               ]

class EnSimpleWallParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x2C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x34", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x38", "i", endianness='>')  # Padding
        self.rw_var("unknown_0x3C", "i", endianness='>')  # Padding
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0100", "q", endianness='>')  # Padding
        self.rw_var("unknown_0x0108", "q", endianness='>')  # Padding
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')  # Padding
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110,
               ]

class SlgEnProduceBorderParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
               ]
    
class SlgEnProduceGndParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='<')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='<')
        
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118
               ]
    
class SlgEnBreakableGateParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04 )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]

      
class SlgEnChainBreakdownParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138]
      
      
class SlgEnSlayingAreaParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x44")
        self.assert_is_zero("unknown_0x48")
        self.assert_is_zero("unknown_0x4C")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
               )
    
    def asset_table_offsets(self):
        return []
          
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  
               ]
    
class SlgEnSurroundPathNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
                
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnOrderAllAttackPointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnSurroundParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138
               ]
    
class SlgEnTriggerEnterParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x54")
        self.assert_is_zero("unknown_0x58")
        self.assert_is_zero("unknown_0x5C")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50
               ]
    
class SlgEnAlterOperationMapParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "q", endianness='>')
        self.rw_var("unknown_0x08", "q", endianness='>')
        
        self.rw_var("unknown_0x10", "q", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18, self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24, )
    
    def asset_table_offsets(self):
        return [0x00, 0x08, 0x10]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24
               ]
    
class SlgEnSandstormParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]

class SlgEnTerrainParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
                
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118
               ]
    
class StaticSphere(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "I", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "I", endianness='>')
        self.rw_var("unknown_0x28", "I", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.assert_is_zero("unknown_0x14")
        self.assert_is_zero("unknown_0x18")
        self.assert_is_zero("unknown_0x1C")
        
        self.assert_is_zero("unknown_0x24")
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, ) 

    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [0x00, 0x04, 0x08, 0x0C, 0x10, 0x20]
    
class SlgEnSearchLightPathNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0118")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x88, 
                 self.unknown_0x90,  self.unknown_0x98, 
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8, 
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108, 
                 self.unknown_0x0110,  self.unknown_0x0118, 
                 )
    
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
      
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110
               ]
    
class SlgEnLongRangeHEProposedImpactParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110,
               ]

class SlgEnSearchLightJointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, ) 

    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]


class SlgEnTriggerHerbParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')

        self.assert_is_zero("unknown_0x44")
        self.assert_is_zero("unknown_0x48")
        self.assert_is_zero("unknown_0x4C")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, ) 
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40
               ]

    
class SlgEnSearchLightParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
        self.rw_var("unknown_0x0120", "i", endianness='>')
        self.rw_var("unknown_0x0124", "i", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124
               ]

class SlgEnCentralLorryParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, ) 
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]

    
class SlgEnLorryParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C
               ]

class SlgEnLiftJointParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]
    
class SlgEnLiftSwitchParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "I", endianness='>')
        self.rw_var("unknown_0x04", "I", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, ) 

    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C
               ]
    
class SlgEnSteepleBarrierParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118
               ]
    
class SlgEnLiftParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "i", endianness='>')
        self.rw_var("unknown_0x011C", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C
               ]

class SlgEnBunkerCannonParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128
               ]
    
class SlgEnReplaceModelParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0128")
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120
               ]

class SlgEnRailWaySwitchParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, ) 
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C
               ]
    
class SlgEnSwitchDoorParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "q", endianness='>')
        self.rw_var("unknown_0x08", "I", endianness='>')
        self.rw_var("unknown_0x0C", "I", endianness='>')
        
        self.assert_is_zero("unknown_0x08")
        self.assert_is_zero("unknown_0x0C")
        
        self.rw_var("unknown_0x10", "I", endianness='>')
        self.rw_var("unknown_0x14", "I", endianness='>')
        self.rw_var("unknown_0x18", "I", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "f", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "f", endianness='>')
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "f", endianness='>')
        self.rw_var("unknown_0x4C", "f", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x58")
        self.assert_is_zero("unknown_0x5C")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, )
    
    def asset_table_offsets(self):
        return [0x00]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,
               ]

class SlgEnMarmot1stPathParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0118")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110
               ]
    
class SlgEnMarmot1stStopNodeParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  )  
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
               ]
    
class SlgEnCliffExplosiveParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]

class SlgEnMarmot1stParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134
               ]
    

class SlgEnCatwalkParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "q", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "i", endianness='>')
        self.rw_var("unknown_0x012C", "i", endianness='>')
        
        self.rw_var("unknown_0x0130", "q", endianness='>')
        self.rw_var("unknown_0x0138", "q", endianness='>')
        
        self.rw_var("unknown_0x0140", "q", endianness='>')
        self.rw_var("unknown_0x0148", "i", endianness='>')
        self.rw_var("unknown_0x014C", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0138,
                 self.unknown_0x0140,  self.unknown_0x0148, self.unknown_0x014C,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120, 0x138, 0x140]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x138,
                0x140, 0x148, 0x14C]

class SlgEnCatwalkHoleParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,  
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,  )   
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
               ]

class SlgEnPropellerParam(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "i", endianness='>')
        self.rw_var("unknown_0x04", "i", endianness='>')
        self.rw_var("unknown_0x08", "i", endianness='>')
        self.rw_var("unknown_0x0C", "i", endianness='>')
        
        self.rw_var("unknown_0x10", "i", endianness='>')
        self.rw_var("unknown_0x14", "i", endianness='>')
        self.rw_var("unknown_0x18", "i", endianness='>')
        self.rw_var("unknown_0x1C", "i", endianness='>')
        
        self.rw_var("unknown_0x20", "i", endianness='>')
        self.rw_var("unknown_0x24", "i", endianness='>')
        self.rw_var("unknown_0x28", "i", endianness='>')
        self.rw_var("unknown_0x2C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x28")
        self.assert_is_zero("unknown_0x2C")
        
        self.rw_var("unknown_0x30", "i", endianness='>')
        self.rw_var("unknown_0x34", "i", endianness='>')
        self.rw_var("unknown_0x38", "i", endianness='>')
        self.rw_var("unknown_0x3C", "i", endianness='>')
        
        self.assert_is_zero("unknown_0x30")
        self.assert_is_zero("unknown_0x34")
        self.assert_is_zero("unknown_0x38")
        self.assert_is_zero("unknown_0x3C")
        
        self.rw_var("unknown_0x40", "i", endianness='>')
        self.rw_var("unknown_0x44", "i", endianness='>')
        self.rw_var("unknown_0x48", "i", endianness='>')
        self.rw_var("unknown_0x4C", "i", endianness='>')
        
        self.rw_var("unknown_0x50", "i", endianness='>')
        self.rw_var("unknown_0x54", "i", endianness='>')
        self.rw_var("unknown_0x58", "i", endianness='>')
        self.rw_var("unknown_0x5C", "i", endianness='>')
        
        self.rw_var("unknown_0x60", "i", endianness='>')
        self.rw_var("unknown_0x64", "i", endianness='>')
        self.rw_var("unknown_0x68", "i", endianness='>')
        self.rw_var("unknown_0x6C", "i", endianness='>')
        
        self.rw_var("unknown_0x70", "q", endianness='>')
        self.rw_var("unknown_0x78", "q", endianness='>')
        
        self.rw_var("unknown_0x80", "q", endianness='>')
        self.rw_var("unknown_0x88", "q", endianness='>')
        
        self.rw_var("unknown_0x90", "q", endianness='>')
        self.rw_var("unknown_0x98", "q", endianness='>')
        
        self.rw_var("unknown_0xA0", "q", endianness='>')
        self.rw_var("unknown_0xA8", "q", endianness='>')
        
        self.rw_var("unknown_0xB0", "q", endianness='>')
        self.rw_var("unknown_0xB8", "q", endianness='>')
        
        self.rw_var("unknown_0xC0", "q", endianness='>')
        self.rw_var("unknown_0xC8", "q", endianness='>')
        
        self.rw_var("unknown_0xD0", "q", endianness='>')
        self.rw_var("unknown_0xD8", "q", endianness='>')
        
        self.rw_var("unknown_0xE0", "q", endianness='>')
        self.rw_var("unknown_0xE8", "q", endianness='>')
        
        self.rw_var("unknown_0xF0", "q", endianness='>')
        self.rw_var("unknown_0xF8", "q", endianness='>')
        
        self.assert_is_zero("unknown_0xF8")
        
        self.rw_var("unknown_0x0100", "q", endianness='>')
        self.rw_var("unknown_0x0108", "q", endianness='>')
        
        self.assert_is_zero("unknown_0x0100")
        self.assert_is_zero("unknown_0x0108")
        
        self.rw_var("unknown_0x0110", "i", endianness='>')
        self.rw_var("unknown_0x0114", "i", endianness='>')
        self.rw_var("unknown_0x0118", "q", endianness='>')
        
        self.rw_var("unknown_0x0120", "q", endianness='>')
        self.rw_var("unknown_0x0128", "q", endianness='>')
        
        self.rw_var("unknown_0x0130", "i", endianness='>')
        self.rw_var("unknown_0x0134", "i", endianness='>')
        self.rw_var("unknown_0x0138", "i", endianness='>')
        self.rw_var("unknown_0x013C", "i", endianness='>')
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0130, self.unknown_0x0138, self.unknown_0x013C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x120, 0x128]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118,
                0x120, 0x128,
                0x130, 0x134, 0x138, 0x13C
               ]
    
class StaticPyramid(BaseRW):
    def read_write(self):
        self.rw_var("unknown_0x00", "f", endianness='>')
        self.rw_var("unknown_0x04", "f", endianness='>')
        self.rw_var("unknown_0x08", "f", endianness='>')
        self.rw_var("unknown_0x0C", "f", endianness='>')
        
        self.rw_var("unknown_0x10", "f", endianness='>')
        self.rw_var("unknown_0x14", "f", endianness='>')
        self.rw_var("unknown_0x18", "f", endianness='>')
        self.rw_var("unknown_0x1C", "f", endianness='>')
        
        self.rw_var("unknown_0x20", "f", endianness='>')
        self.rw_var("unknown_0x24", "f", endianness='>')
        self.rw_var("unknown_0x28", "f", endianness='>')
        self.rw_var("unknown_0x2C", "I", endianness='>')
        
        self.rw_var("unknown_0x30", "f", endianness='>')
        self.rw_var("unknown_0x34", "f", endianness='>')
        self.rw_var("unknown_0x38", "f", endianness='>')
        self.rw_var("unknown_0x3C", "I", endianness='>')
        
        self.rw_var("unknown_0x40", "f", endianness='>')
        self.rw_var("unknown_0x44", "I", endianness='>')
        self.rw_var("unknown_0x48", "I", endianness='>')
        self.rw_var("unknown_0x4C", "I", endianness='>')
    
        self.assert_is_zero("unknown_0x44")
        self.assert_is_zero("unknown_0x48")
        self.assert_is_zero("unknown_0x4C")
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C ) 

    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [0x00, 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
                0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C,
                0x40]
    
class void(BaseRW):
    def read_write(self):
        pass
    
    def get_data(self):
        return []
    
    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ ]
    
class SlgEnGlowFlyParam(BaseRW):
    def read_write(self):
        pass
    
    def get_data(self):
        []

    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ ]

# TYPES ARE ALPHABETICALLY ORDERED
data_types = {clas.__name__: clas for clas in
              [
                 AISlgUnitMxParam,
                 EnCEffectParam,
                 EnConvexParam,
                 EnEventDecorParam,
                 EnHeightMapParam,
                 EnMovePathParam,
                 EnMovePathNodeParam,
                 EnSimpleWallParam,
                 EnSkyParam,
                 EnTalkEventMapParam,
                 EnTalkEventObjParam,
                 EnTreeParam,
                 EnUvScrollParam,
                 EnWaterSurfaceParam,
                 EnWindmillParam,
                 HyColor,
                 MxParameterFog,
                 MxParameterLight,
                 MxParameterStaticLight,
                 MxParameterTextureMerge,
                 MxParameterMergeFile,
                 MxParameterPvs,
                 SlgEnAlterOperationMapParam,
                 SlgEnAreaSurveillanceParam,
                 SlgEnAreaSurveillancePathNodeParam,
                 SlgEnBreakableBridgeParam,
                 SlgEnBreakableGateParam,
                 SlgEnBreakableStructureParam,
                 SlgEnBunkerCannonParam,
                 SlgEnCatwalkParam,
                 SlgEnCatwalkHoleParam,
                 SlgEnCentralLorryParam,
                 SlgEnChainBreakdownParam,
                 SlgEnCliffExplosiveParam,
                 SlgEnControlLancePieceParam,
                 SlgEnDefenseWallParam,
                 SlgEnDummyTankParam,
                 SlgEnExplosiveParam,
                 SlgEnGlowFlyParam,
                 SlgEnGrassParam,
                 SlgEnGrassPathNodeParam,
                 SlgEnGregoalParam,
                 SlgEnGregoalStayPointParam,
                 SlgEnLancePieceParam,
                 SlgEnLiftJointParam,
                 SlgEnLiftParam,
                 SlgEnLiftSwitchParam,
                 SlgEnLongRangeHEProposedImpactParam,
                 SlgEnLorryParam,
                 SlgEnMarmot1stParam,
                 SlgEnMarmot1stPathParam,
                 SlgEnMarmot1stStopNodeParam,
                 SlgEnMedicPointParam,
                 SlgEnMineParam,
                 SlgEnOrderAllAttackPointParam,
                 SlgEnProduceBorderParam,
                 SlgEnProduceGndParam,
                 SlgEnPropellerParam,
                 SlgEnRailWaySwitchParam,
                 SlgEnReinforcePointParam,
                 SlgEnReplaceModelParam,
                 SlgEnSandstormParam,
                 SlgEnSearchLightJointParam,
                 SlgEnSearchLightParam,
                 SlgEnSearchLightPathNodeParam,
                 SlgEnSlayingAreaParam,
                 SlgEnSteepleBarrierParam,
                 SlgEnStrongholdParam,
                 SlgEnStrongholdPathNodeParam,
                 SlgEnSurroundParam,
                 SlgEnSurroundPathNodeParam,
                 SlgEnSwitchDoorParam,
                 SlgEnTemplePartsParam,
                 SlgEnTerrainParam,
                 SlgEnTriggerBaseParam,
                 SlgEnTriggerEnterParam,
                 SlgEnTriggerHerbParam,
                 SlgEnTowerParam,
                 SlgEnTriggerBaseParam,
                 SlgEnUnitPlacementPointParam,
                 SlgEnWarpPointParam,
                 SlgMapObjectParam,
                 StaticBox,
                 StaticPyramid,
                 StaticSphere,
                 void,
                 VlMapObjectParam,
                 VlMxBookDecorationInfo,
                 VlMxBookHistoryInfo,
                 VlMxBookPersonInfo,
                 VlMxBookSoundInfo,
                 VlMxBookWeaponInfo,
                 VlMxCanvasShaderParam,
                 VlMxDrawModelLodParam,
                 VlMxFogParam,
                 VlMxShaderParamSetId,
                 VlMxStandardLightParam,
                 VlMxAddEsdInfo,
                 VlMxBriefingInfo,
                 VlMxCharacterAffinityInfo,
                 VlMxCharacterCommonInfo,
                 VlMxCharacterEachInfo,
                 VlMxCharacterInfo,
                 VlMxClothesInfo,
                 VlMxCountryInfo,
                 VlMxExplosiveInfo,
                 VlMxFieldInfo,
                 VlMxForceInfo,
                 VlMxGalliaRareWeaponCandidateInfo,
                 VlMxGeneralCharInfo,
                 VlMxGeneralCharParamSetInfo,
                 VlMxJobInfo,
                 VlMxMapObjectCommonInfo,
                 VlMxMapObjectInfo,
                 VlMxNewsPaperInfo,
                 VlMxOrderDirectionInfo,
                 VlMxOrderInfo,
                 VlMxParameterConvertTable,
                 VlMxPhysicsMaterialInfo,
                 VlMxPotentialInfo,
                 VlMxResultInfo,
                 VlMxSlgCameraInfo,
                 VlMxSlgCommandCursorInfo,
                 VlMxSlgInfo,
                 VlMxSlgLandformInfo,
                 VlMxSlgStrongholdCommonInfo,
                 VlMxStageInfo,
                 VlMxSurroundInfo,
                 VlMxTargetModeGazeFixedInfo,
                 VlMxUnitCommonInfo,
                 VlMxUnitGrowthTypeInfo,
                 VlMxVehicleCommonInfo,
                 VlMxVehicleDevChangeParamInfo,
                 VlMxVehicleDevInfo,
                 VlMxVehicleEachInfo,
                 VlMxVehicleInfo,
                 VlMxWeaponBringOnUnwholesomeInfo,
                 VlMxWeaponCommonInfo,
                 VlMxWeaponInfo,
                 VlMxUnitResourceInfo
              ]}

