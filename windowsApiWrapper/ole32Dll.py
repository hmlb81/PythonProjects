import ctypes

class ole32Dll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def __init__(self) :
        self._dll = ctypes.windll.ole32
        
    def iidFromString(self, lpsz, lpiid) :
        return self._dll.IIDFromString(lpsz, lpiid)
    
    def stringFromClsid(self, rclsid, lplpsz) :
        return self._dll.StringFromCLSID(rclsid, lplpsz)
    
    def coTaskMemFree(self, pv) :
        self._dll.CoTaskMemFree(pv)

_instance = ole32Dll()