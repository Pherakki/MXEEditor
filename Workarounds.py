import os

from pyValkLib.containers.MXEN.MXEC.ParameterEntry import param_structs

def is_game_info_sys_param(filename):
    return os.path.splitext(os.path.split(filename)[1])[0] == "game_info_sys_param"
        

def hack_fix_game_info_sys_param(filename):
    if is_game_info_sys_param(filename):
        stct = param_structs["VlMxGeneralCharInfo"]["struct"]
        for param_chunk in stct:
            for pname, ptype in param_chunk.items():
                if ptype[1:] == "utf8_string":
                    param_chunk[pname] = ptype[0] + "sjis_string"

def hack_unfix_game_info_sys_param(filename):
    if is_game_info_sys_param(filename):
        stct = param_structs["VlMxGeneralCharInfo"]["struct"]
        for param_chunk in stct:
            for pname, ptype in param_chunk.items():
                if ptype[1:] == "sjis_string":
                    param_chunk[pname] = ptype[0] + "utf8_string"
