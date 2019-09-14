
#set import paths. executed before main methods
import sys
sys.path.append("..")

from applications.processAnalyzeApplication import *
from loggingAuxiliary.loggingConfigger import *
from windowsApiWrapper.kernel32Dll import *


#main program class
class program : 
    #main method
    def run(self) : 
        self._initializeInfrustructures()
        
        processAnalyzeApplication.getInstance().scanProcessStrings()
        #applications.networkDiagnosticsApplication.instance.collectNetworkAdaptersInformation()
    
    #initialize infrustructures
    def _initializeInfrustructures(self) : 
        loggingConfigger.getInstance().configConsoleLogging()

#run program
_instance = program()
_instance.run()