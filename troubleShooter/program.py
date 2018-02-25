
#set import paths. executed before main methods
import sys
sys.path.append("..")

import loggingAuxiliary
import loggingAuxiliary.loggingConfigger
import applications
import applications.networkDiagnosticsApplication



#main program class
class program : 
    #main method
    def run(self) : 
        self._initializeInfrustructures()
    
    #initialize infrustructures
    def _initializeInfrustructures(self) : 
        loggingAuxiliary.loggingConfigger.instance.configConsoleLogging()

#run program
_instance = program()
_instance.run()