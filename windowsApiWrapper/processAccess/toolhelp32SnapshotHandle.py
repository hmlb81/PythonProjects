import ctypes
from ..commonDefinitions import *
from ..kernel32Dll import *
from ..toolhelpDefinitions import *
from ..windowsErrorCode import *
from utilities.enumHelper import *

class toolhelp32SnapshotHandleModuleEntry : 
    def __init__(self, moduleEntryW) :
        self._winModuleName = moduleEntryW.winModuleName
        self._exePath = moduleEntryW.exePath
    
    def __repr__(self) :
        return self._winModuleName
    
    @property
    def winModuleName(self) :
        return self._winModuleName
    
    @property
    def exePath(self) :
        return self._exePath
    

class toolhelp32SnapshotHandle : 
    @staticmethod
    def create(flags, processID) : #flags : enum values list
        flagsValue = ctypes.c_uint32(enumHelper.getInstance().combine(flags))
        processIDValue = ctypes.c_uint32(processID)
        
        handle = kernel32Dll.getInstance().createToolhelp32Snapshot(flagsValue, processIDValue)
        isInvalidHandle = systemConstants.getInstance().isInvalidHandleValue(handle)
        if (isInvalidHandle) :
            return None
        
        return toolhelp32SnapshotHandle(handle)
    
    def __init__(self, handle) :
        self._handle = handle
        
    def __del__(self) :
        kernel32Dll.getInstance().closeHandle(ctypes.c_void_p(self._handle)) #closeToolhelp32Snapshot only available in win ce
        self._handle = 0
        
    def walkModuleEntry(self) :
        modules = []
        walkNext = self._walkModuleEntryFirst(modules)
        while (walkNext) :
            walkNext = self._walkModuleEntryNext(modules)
            
        return modules
    
    def _walkModuleEntryFirst(self, modules) :
        snapshot = ctypes.c_void_p(self._handle)
        currentModule = moduleEntry32W.createEmptyEntry()
        walkRes = kernel32Dll.getInstance().module32FirstW(snapshot, ctypes.pointer(currentModule))
        error = kernel32Dll.getInstance().getLastError()
        nomoreFiles = error == windowsErrorCode.ERROR_NO_MORE_FILES.value
        isOK = walkRes == 1 #return TRUE when success
        if isOK :
            #debugging codes
            newModule = toolhelp32SnapshotHandleModuleEntry(currentModule)
            modules.append(newModule)
        
        walkNext = isOK and (not nomoreFiles)
        return walkNext
    
    def _walkModuleEntryNext(self, modules) :
        snapshot = ctypes.c_void_p(self._handle)
        currentModule = moduleEntry32W.createEmptyEntry()
        walkRes = kernel32Dll.getInstance().module32NextW(snapshot, ctypes.pointer(currentModule))
        error = kernel32Dll.getInstance().getLastError()
        nomoreFiles = error == windowsErrorCode.ERROR_NO_MORE_FILES.value
        isOK = walkRes == 1 #return TRUE when success
        if isOK :
            newModule = toolhelp32SnapshotHandleModuleEntry(currentModule)
            modules.append(newModule)
        
        walkNext = isOK and (not nomoreFiles)
        return walkNext
        
    
    
    