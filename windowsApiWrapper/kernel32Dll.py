import ctypes
import enum
from .toolhelpDefinitions import *

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