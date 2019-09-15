import ctypes
import enum
from .commonDefinitions import *

class toolhelpConstants : 
    @staticmethod
    def getInstance() :
        return _toolhelpConstants
    
    def __init__(self) :
        self._maxModuleName32 = 255
        
    @property
    def maxModuleName32(self) :
        return self._maxModuleName32

_toolhelpConstants = toolhelpConstants()

class toolhelp32CreateSnapshotFlag(enum.Enum) :
    TH32CS_SNAPHEAPLIST = 0x00000001
    TH32CS_SNAPPROCESS = 0x00000002
    TH32CS_SNAPTHREAD = 0x00000004
    TH32CS_SNAPMODULE = 0x00000008
    TH32CS_SNAPMODULE32 = 0x00000010
    TH32CS_SNAPALL = (TH32CS_SNAPHEAPLIST | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD | TH32CS_SNAPMODULE)
    TH32CS_INHERIT = 0x80000000

#MODULEENTRY32W
class moduleEntry32W(ctypes.Structure) : 
    _fields_ = [
        ("_dwSize", ctypes.c_uint32),
        ("th32ModuleID", ctypes.c_uint32),
        ("th32ProcessID", ctypes.c_uint32),
        ("GlblcntUsage", ctypes.c_uint32),
        ("ProccntUsage", ctypes.c_uint32),
        ("modBaseAddr", ctypes.c_void_p), #BYTE*
        ("modBaseSize", ctypes.c_uint32),
        ("hModule", ctypes.c_void_p),
        ("szModule", ctypes.c_wchar * (toolhelpConstants.getInstance().maxModuleName32 + 1)),
        ("szExePath", ctypes.c_wchar * (systemConstants.getInstance().maxPath)),
    ]