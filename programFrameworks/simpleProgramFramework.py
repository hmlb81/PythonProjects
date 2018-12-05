import logging
from loggingAuxiliary.loggingConfigger import *

class simpleProgramBase : 
    def run(self) : 
        self._initializeInfrustrutures()
        
        self._beforeDoRun()
        self._dorun()
        self._afterDoRun()
    
    def _initializeInfrustrutures(self) : 
        self._initializeLogging()
    
    def _initializeLogging(self) : 
        loggingConfigger.getInstance().configConsoleLogging()
    
    def _beforeDoRun(self) : 
        logging.info("begin run.")
    
    def _afterDoRun(self) : 
        logging.info("end run.")
    
    def _dorun(self) : 
        pass #implementating by child classes