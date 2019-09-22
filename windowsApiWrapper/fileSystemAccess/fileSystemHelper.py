import ctypes
from ..kernel32Dll import *

class fileSystemHelper : 
    @staticmethod 
    def getInstance() :
        return _instance

_instance = fileSystemHelper()