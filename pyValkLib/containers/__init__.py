from .CCRS.CCRSReadWriter import CCRSReadWriter
from .ENRS.ENRSReadWriter import ENRSReadWriter
from .EOFC.EOFCReadWriter import EOFCReadWriter
# from .IZCA.IZCAReadWriter import IZCAReadWriter
# from .IZCA.CCOL.CCOLReadWriter import CCOLReadWriter
# from .IZCA.HMDL.HMDLReadWriter import HMDLReadWriter
# from .IZCA.HSHP.HSHPReadWriter import HSHPReadWriter
# from .IZCA.HTEX.HTEXReadWriter import HTEXReadWriter
# from .IZCA.MLX0.MLX0ReadWriter import MLX0ReadWriter
# from .IZCA.PJNT.PJNTReadWriter import PJNTReadWriter
# from .IZCA.PACT.PACTReadWriter import PACTReadWriter
from .MXEN.MXENReadWriter import MXENReadWriter
from .MXEN.MXEC.MXECReadWriter import MXECReadWriter
from .POF0.POF0ReadWriter import POF0ReadWriter

containers = {
    # "CCOL": CCOLReadWriter,
    "CCRS": CCRSReadWriter,
    "ENRS": ENRSReadWriter,
    "EOFC": EOFCReadWriter,
    # "HMDL": HMDLReadWriter,
    # "HSHP": HSHPReadWriter,
    # "HTEX": HTEXReadWriter,
    # "IZCA": IZCAReadWriter,
    # "MLX0": MLX0ReadWriter,
    "MXEN": MXENReadWriter,
    "MXEC": MXECReadWriter,
    # "PACT": PACTReadWriter,
    # "PJNT": PJNTReadWriter,
    "POF0": POF0ReadWriter
}