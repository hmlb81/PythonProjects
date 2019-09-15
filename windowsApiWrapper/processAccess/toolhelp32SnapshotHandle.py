import ctypes
from ..commonDefinitions import *
from ..kernel32Dll import *
from utilities.enumHelper import *

class toolhelp32SnapshotHandle : 
    @staticmethod
    def create(flags, processID) : #flags : enum values list
        flagsValue = ctypes.c_uint32(enumHelper.getInstance().combine(flags))
        processIDValue = ctypes.c_uint32(processID)
        
        handle = kernel32Dll.getInstance().createToolhelp32Snapshot(flagsValue, processIDValue)
        isInvalidHandle = systemConstants.getInstance().isInvalidHandleValue(handle)
        if (isInvalidHandle) :
            return None
        
        raise AssertionError("todo:implement")