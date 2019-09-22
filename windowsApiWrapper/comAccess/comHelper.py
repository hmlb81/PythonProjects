import ctypes
from ..commonDefinitions import *
from ..hresults import *
from ..ole32Dll import *
from utilities.ctypesHelper import *

class comHelper : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def stringToGuid(self, guidText) :
        guidTextBuffer = ctypes.create_unicode_buffer(guidText)
        guidValue = guid()
        res = ole32Dll.getInstance().iidFromString(ctypes.pointer(guidTextBuffer), ctypes.pointer(guidValue))
        isOK = res == hresult.S_OK.value
        return guidValue

_instance = comHelper()