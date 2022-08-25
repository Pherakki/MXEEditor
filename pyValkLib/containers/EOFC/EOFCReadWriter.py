from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH


class EOFCReadWriter(ValkSerializable32BH):
    FILETYPE = "EOFC"
    
    __slots__ = tuple()
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"EOFC Object [{self.header.depth}] [0x{self.header.flags:0>8x}]: Zero data."
