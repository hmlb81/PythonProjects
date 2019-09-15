import ctypes
import enum

class systemConstants : 
    @staticmethod
    def getInstance() :
        return _systemConstants
    
    def __init__(self) :
        self._invalidHandleValue = ctypes.c_void_p(-1)
        self._maxPath = 260
    
    @property
    def maxPath(self) :
        return self._maxPath
        
    def isInvalidHandleValue(self, value) :
        if isinstance(value, ctypes.c_void_p) :
            raise AssertionError("todo:implement")
        else :
            return value == self._invalidHandleValue.value #ctypes call always return python interger type

_systemConstants = systemConstants()

class Guid(ctypes.Structure) : 
    _fields_ = [
        ("data1", ctypes.c_ulong),
        ("data2", ctypes.c_ushort),
        ("data3", ctypes.c_ushort),
        ("data4", ctypes.c_ubyte * 8)
    ]
    
class SystemErrorCodes(enum.Enum) : 
    Success = 0 #ERROR_SUCCESS
    NotEnoughMemory = 8 #ERROR_NOT_ENOUGH_MEMORY
    InvalidParameter = 87 #ERROR_INVALID_PARAMETER
    BufferOverflow = 111 #ERROR_BUFFER_OVERFLOW
    NoData = 232 #ERROR_NO_DATA
    AddressNotAssociated = 1228 #ERROR_ADDRESS_NOT_ASSOCIATED
