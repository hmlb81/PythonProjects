import ctypes
from debuggingKits.scanners.asciiTextScanner import *
from utilities.collectionsHelper import *
from windowsApiWrapper.comAccess.comHelper import *
from windowsApiWrapper.kernel32Dll import *
from windowsApiWrapper.processAccess.processHelper import *
from windowsApiWrapper.processAccess.toolhelp32SnapshotHandle import *

class analyzingProcess :
    def __init__(self, processID) :
        self._processID = processID
        self._processName = None #init to None, and detect later
        
    def __repr__(self) :
        return "{0}:{1}".format(self._processID, self._processName)
    
    def detectAndFillProcessName(self, thModule) :
        if (self._processName != None) : #already detected
            return 
        
        moduleName = thModule.winModuleName
        isExe = moduleName.lower().endswith(".exe")
        self._processName = moduleName

class analyzingProcessModule : 
    @staticmethod
    def prepareAnalyzingProcessModule(analyzingProcess, thModule, analyzingModules) :
        found = collectionsHelper.getInstance().firstOrDefault(analyzingModules, None, lambda m : m._exePath == thModule.exePath.lower())
        preparingModule = found
        if preparingModule == None :
            newModule = analyzingProcessModule(thModule)
            analyzingModules.append(newModule)
            preparingModule = newModule
            
        preparingModule._relatingProcesses.append(analyzingProcess)
        return preparingModule
    
    def __init__(self, thModule) :
        self._relatingProcesses = []
        self._winModuleName = thModule.winModuleName
        self._exePath = thModule.exePath.lower()
        
    def __repr__(self) :
        return self._winModuleName
    
    def scanAsciiStrings(self) :
        scanner = self._prepareAsciiScanner()
        
        with open(self._exePath, "rb") as moduleFile :
            self._scanAsciiStrings(scanner, moduleFile)
    
    def _scanAsciiStrings(self, scanner, moduleFile) :
        byte = moduleFile.read(1)
        while byte != b'' :
            scanner.scan(byte[0], None)
            byte = moduleFile.read(1)
            
    def _prepareAsciiScanner(self) :
        scanner = asciiTextScanner()
        
        scanner.handlerTextFound = lambda text, userState : print(text)
        return scanner

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
            
        #analyzing modules for ascii strings
        for analyzingModule in analyzingModules :
            analyzingModule.scanAsciiStrings()
        
        #mark suspect strings
        #analyzing suspect module processes
        raise AssertionError("todo:implement")

    def scanDefragComCallers(self) :
        defragClassidStrings = [
            "{d20a3293-3341-4ae8-9aaf-8e397cb63c34}",
            "{d20a3293-3341-4ae8-9aaf-8e397cb63c34}",
        ]
        
        defragClassidValues = [comHelper.getInstance().stringToGuid(t) for t in defragClassidStrings]
        raise AssertionError("todo:implement")
    
_instance = processAnalyzeApplication()