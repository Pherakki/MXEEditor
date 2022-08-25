#from pyValkLib.utils.Compression.Stencilled import SCRelRep, SCRelativeTemplateGenerator, CCRSTemplateComponent
#from pyValkLib.utils.Compression.Stencilled import SCUnpackedRep, SCTemplatePack, SCTemplate, CCRSUnpackedTemplateComponents

from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
#from pyValkLib.utils.Compression.integers import compressInt, decompressInt

class CCRSReadWriter(ValkSerializable32BH):
    FILETYPE = "CCRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.padding_0x20 = 0
        self.num_groups = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20)
        self.num_groups   = rw.rw_uint32(self.num_groups)
        rw.align(rw.local_tell(), 0x10)
        
        rw.assert_is_zero(self.padding_0x20)
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10, endianness='<')
