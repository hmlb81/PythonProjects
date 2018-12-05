
#set import paths. executed before main methods
import sys
sys.path.append("..")

import applications
import applications.networkDiagnosticsApplication
from loggingAuxiliary.loggingConfigger import *



#main program class
class program : 
    #main method
    def run(self) : 
        self._initializeInfrustructures()
        applications.networkDiagnosticsApplication.instance.collectNetworkAdaptersInformation()
    
    #initialize infrustructures
    def _initializeInfrustructures(self) : 
        loggingConfigger.getInstance().configConsoleLogging()

#run program
_instance = program()
_instance.run()