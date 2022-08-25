from pyValkLib.containers.MXEN.MXENReadWriter import MXENReadWriter
from pyValkLib.containers.MXEN.MXEC.MXECInterface import MXECInterface
from pyValkLib.containers.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable

# Most of this should go into an MXENInterface
class MXE(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.MXEN = MXENReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    @classmethod
    def init_from_file(cls, filepath):
        instance = cls()
        instance.read(filepath)
        return MXECInterface.from_subreader(instance.MXEN.MXEC)
    
    @classmethod
    def init_from_mxecinterface(cls, mxec):
        instance = cls()
        instance.MXEN.MXEC = mxec.to_subreader(1)
        instance.MXEN.header.depth = 0
        instance.MXEN.header.contents_length = instance.MXEN.header.data_length + instance.MXEN.MXEC.header.header_length + instance.MXEN.MXEC.header.contents_length
        
        instance.EOFC.header.flags           = 0x10000000
        instance.EOFC.header.depth           = 0
        instance.EOFC.header.data_length     = 0
        instance.EOFC.header.contents_length = 0
        return instance
    
    def read_write(self, rw):
        rw.rw_obj(self.MXEN)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
