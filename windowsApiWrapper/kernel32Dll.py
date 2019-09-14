import ctypes

class kernel32Dll : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def __init__(self) :
        self._dll = ctypes.windll.kernel32

_instance = kernel32Dll()