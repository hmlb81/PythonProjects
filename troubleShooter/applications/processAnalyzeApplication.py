import ctypes
from windowsApiWrapper.kernel32Dll import *
from windowsApiWrapper.processAccess.processHelper import *
from windowsApiWrapper.processAccess.toolhelp32SnapshotHandle import *

class analyzingProcess :
    def __init__(self, processID) :
        self._processID = processID
        
    def detectAndFillProcessName(self, thModule) :
        raise AssertionError("todo:implement")

class analyzingProcessModule : 
    @staticmethod
    def prepareAnalyzingProcessModule(analyzingProcess, thModule, analyzingModules) :
        raise AssertionError("todo:implement")
    
    def __init__(self) :
        pass #todo:implement

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
        
        #walk to generate analyzing modules
        analyzingModules = []
        for processId in processIds :
            currentAnalyzingProcess = analyzingProcess(processId)
            snapshotHandle = toolhelp32SnapshotHandle.create(createSnapshotFlags, processId)
            thmodules = snapshotHandle.walkModuleEntry()
            for thmodule in thmodules :
                currentAnalyzingProcess.detectAndFillProcessName(thmodule)
                analyzingProcessModule.prepareAnalyzingProcessModule(processId, thmodule, analyzingModules)
                raise AssertionError("todo:implement")
            
            raise AssertionError("todo:implement")

_instance = processAnalyzeApplication()