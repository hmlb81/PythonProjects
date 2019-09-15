import ctypes
from windowsApiWrapper.kernel32Dll import *
from windowsApiWrapper.processAccess.processHelper import *
from windowsApiWrapper.processAccess.toolhelp32SnapshotHandle import *

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
        
        for processId in processIds :
            snapshotHandle = toolhelp32SnapshotHandle.create(createSnapshotFlags, processId)
            raise AssertionError("todo:implement")

_instance = processAnalyzeApplication()