from windowsApiWrapper.processAccess.processHelper import *

class processAnalyzeApplication : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def scanProcessStrings(self) :
        processIds = processHelper.getInstance().enumProcessIds()
        raise AssertionError("todo:implement")

_instance = processAnalyzeApplication()