from ..kernel32Dll import *

class processHelper : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def enumProcessIds(self) :
        raise AssertionError("todo:implement")

_instance = processHelper()