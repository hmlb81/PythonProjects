import ctypes
import enum

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
