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
    
    def stringFromClsid(self, guid) :
        guidStringPointer = ctypes.c_void_p(0)
        res = ole32Dll.getInstance().stringFromClsid(guid, ctypes.pointer(guidStringPointer))
        isOK = res == hresult.S_OK.value
        if not isOK :
            return None
        
        text = ctypes.wstring_at(guidStringPointer)
        ole32Dll.getInstance().coTaskMemFree(guidStringPointer)
        return text

_instance = comHelper()