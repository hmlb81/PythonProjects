import ctypes
import enum
from .toolhelpDefinitions import *

class kernel32Dll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def __init__(self) :
        self._dll = ctypes.windll.kernel32
        
    def getLastError(self) :
        return self._dll.GetLastError()
        
    def createToolhelp32Snapshot(self, flags, th32ProcessID) :
        return self._dll.CreateToolhelp32Snapshot(flags, th32ProcessID)
    
    def module32FirstW(self, hSnapshot, lpme) :
        return self._dll.Module32FirstW(hSnapshot, lpme)
    
    def closeHandle(self, handle) :
        return self._dll.CloseHandle(handle)
    
    def module32FirstW(self, hsnapshot, lpme) :
        return self._dll.Module32FirstW(hsnapshot, lpme)
    
    def module32NextW(self, hsnapshot, lpme) :
        return self._dll.Module32NextW(hsnapshot, lpme)
    
    def wow64EnableWow64FsRedirection(self, wow64FsEnableRedirection) :
        return self._dll.Wow64EnableWow64FsRedirection(wow64FsEnableRedirection)

_instance = kernel32Dll()