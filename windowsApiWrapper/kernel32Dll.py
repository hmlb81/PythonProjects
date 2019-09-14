import ctypes

class kernel32Dll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def __init__(self) :
        self._dll = ctypes.windll.kernel32
        
    def enumProcesses(self, lpidProcesses, cb, lpcbNeeded) :
        return self._dll.EnumProcesses(lpidProcesses, cb, lpcbNeeded)

_instance = kernel32Dll()