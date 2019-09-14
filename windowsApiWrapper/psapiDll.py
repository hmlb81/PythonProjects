import ctypes
import logging

class psapiDll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    @staticmethod
    def _cuint32(value) :
        return ctypes.c_uint32(value) #convert value to c_uint32(python return value must be converted)
    
    def __init__(self) :
        self._dll = ctypes.windll.psapi
        
        self._dll.EnumProcesses.restype = self._cuint32
        
    def enumProcesses(self, lpidProcesses, cb, lpcbNeeded) :
        return self._dll.EnumProcesses(lpidProcesses, cb, lpcbNeeded)
        
_instance = psapiDll()