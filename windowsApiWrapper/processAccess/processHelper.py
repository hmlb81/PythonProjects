import ctypes
from ..psapiDll import *
from utilities.ctypesHelper import *

class processHelper : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def enumProcessIds(self) :
        singleUint32Size = ctypes.sizeof(ctypes.c_uint32)
        probeProcessCount = 1
        isFinished = False
        while not isFinished :
            processIdsCount = probeProcessCount
            probeProcessCount = probeProcessCount * 2 #grow process buffer count for next try
            
            #try get process ids
            processIds = (ctypes.c_uint32 * processIdsCount)()
            cb = ctypes.c_uint32(processIdsCount * singleUint32Size)
            cbNeeded = ctypes.c_uint32(0)
            enumProcessRes = psapiDll.getInstance().enumProcesses(
                ctypes.pointer(processIds),
                cb,
                ctypes.pointer(cbNeeded)
                )
            
            isOK = enumProcessRes != 0
            if not isOK :
                return None #enum process procedure fail
            
            processCountGot = int(cbNeeded.value / singleUint32Size) #devide got double type value
            exceededBuffer = processIdsCount > processCountGot
            if not exceededBuffer :
                continue #if process buffer full, retry to got more processes
            
            #success & returning results
            validProcessIds = ctypesHelper.getInstance().convertCtypeArrayToList(
                processIds,
                processCountGot,
                lambda pid : pid #do nothing for convert, since python convert c_xx type to python interger
                )
            return validProcessIds 

_instance = processHelper()