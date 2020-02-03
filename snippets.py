import struct
from loggingAuxiliary.loggingConfigger import loggingConfigger

class Snippets : 
    def run(self) :
        self._initializeInfrustructures()
    
    def _initializeInfrustructures(self) : 
        loggingConfigger.getInstance().configConsoleLogging()

instance = Snippets()
instance.run()