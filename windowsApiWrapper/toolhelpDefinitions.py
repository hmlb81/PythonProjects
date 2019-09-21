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
        ("_th32ModuleID", ctypes.c_uint32),
        ("_th32ProcessID", ctypes.c_uint32),
        ("_GlblcntUsage", ctypes.c_uint32),
        ("_ProccntUsage", ctypes.c_uint32),
        ("_modBaseAddr", ctypes.c_void_p), #BYTE*
        ("_modBaseSize", ctypes.c_uint32),
        ("_hModule", ctypes.c_void_p),
        ("_szModule", ctypes.c_wchar * (toolhelpConstants.getInstance().maxModuleName32 + 1)),
        ("_szExePath", ctypes.c_wchar * (systemConstants.getInstance().maxPath)),
    ]
    
    @staticmethod
    def createEmptyEntry() :
        moduleEntry = moduleEntry32W()
        moduleEntry._dwSize = ctypes.c_uint32(ctypes.sizeof(moduleEntry32W)) #set size to sizeof(MODULEENTRY32W) for input Module32First/Module32Next
        return moduleEntry 
    
    @property
    def winModuleName(self) : #do not name as moduleName(may conflict to python internal property name) 
        return self._szModule
        
    def __repr__(self) :
        return self.winModuleName