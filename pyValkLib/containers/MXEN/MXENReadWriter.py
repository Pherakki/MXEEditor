from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.containers.MXEN.MXEC.MXECReadWriter import MXECReadWriter


class MXENReadWriter(ValkSerializable32BH):
    FILETYPE = "MXEN"
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        
        self.header.data_length = 0
        self.header.flags = 0x10000005
        self.MXEC = MXECReadWriter(endianness)
        
    def get_subcontainers(self):
        return [self.MXEC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000005, lambda x: hex(x))
        
    def __repr__(self):
        return f"MXEN Object [{self.header.depth}] [0x{self.header.flags:0>8x}]: Contains MXEC."
