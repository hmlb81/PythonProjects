import ctypes
import enum
import struct

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

class guid(ctypes.Structure) : 
    _fields_ = [
        ("_data1", ctypes.c_ulong),
        ("_data2", ctypes.c_ushort),
        ("_data3", ctypes.c_ushort),
        ("_data4", ctypes.c_ubyte * 8)
    ]
    
    def pack(self) :
        packResult = struct.pack(
            "LHHBBBBBBBB",
            self._data1,
            self._data2,
            self._data3,
            self._data4[0], self._data4[1], self._data4[2], self._data4[3], self._data4[4], self._data4[5], self._data4[6], self._data4[7]
            )
        return packResult
    
class SystemErrorCodes(enum.Enum) : 
    Success = 0 #ERROR_SUCCESS
    NotEnoughMemory = 8 #ERROR_NOT_ENOUGH_MEMORY
    InvalidParameter = 87 #ERROR_INVALID_PARAMETER
    BufferOverflow = 111 #ERROR_BUFFER_OVERFLOW
    NoData = 232 #ERROR_NO_DATA
    AddressNotAssociated = 1228 #ERROR_ADDRESS_NOT_ASSOCIATED
