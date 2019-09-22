import ctypes

class ole32Dll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def __init__(self) :
        self._dll = ctypes.windll.ole32
        
    def iidFromString(self, lpsz, lpiid) :
        return self._dll.IIDFromString(lpsz, lpiid)

_instance = ole32Dll()