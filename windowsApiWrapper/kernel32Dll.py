import ctypes
import enum

class toolhelp32CreateSnapshotFlag(enum.Enum) :
    TH32CS_SNAPHEAPLIST = 0x00000001
    TH32CS_SNAPPROCESS = 0x00000002
    TH32CS_SNAPTHREAD = 0x00000004
    TH32CS_SNAPMODULE = 0x00000008
    TH32CS_SNAPMODULE32 = 0x00000010
    TH32CS_SNAPALL = (TH32CS_SNAPHEAPLIST | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD | TH32CS_SNAPMODULE)
    TH32CS_INHERIT = 0x80000000

class kernel32Dll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def __init__(self) :
        self._dll = ctypes.windll.kernel32
        
    def createToolhelp32Snapshot(self, flags, th32ProcessID) :
        return self._dll.CreateToolhelp32Snapshot(flags, th32ProcessID)
    
    def closeHandle(self, handle) :
        return self._dll.CloseHandle(handle)

_instance = kernel32Dll()