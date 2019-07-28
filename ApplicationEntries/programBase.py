from loggingAuxiliary.loggingConfigger import *

class programBase : 
    def run(self) :
        self._initializeInfructures()
        self._dorun()
        self._uninitializeInfructures()
    
    def _initializeInfructures(self) :
        loggingConfigger.getInstance().configConsoleLogging()
    
    def _uninitializeInfructures(self) :
        pass
    
    def _dorun(self):
        pass