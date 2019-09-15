import ctypes
from utilities.enumHelper import *
from windowsApiWrapper.kernel32Dll import *
from windowsApiWrapper.processAccess.processHelper import *

class processAnalyzeApplication : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def scanProcessStrings(self) :
        processIds = processHelper.getInstance().enumProcessIds()
        
        createSnapshotFlags = [
            toolhelp32CreateSnapshotFlag.TH32CS_SNAPMODULE,
            toolhelp32CreateSnapshotFlag.TH32CS_SNAPMODULE32,
        ]
        
        createSnapshotFlagsValue = ctypes.c_uint32(enumHelper.getInstance().combine(createSnapshotFlags))
        for processId in processIds :
            raise AssertionError("todo:implement")

_instance = processAnalyzeApplication()