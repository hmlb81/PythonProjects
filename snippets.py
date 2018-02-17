import loggingAuxiliary.loggingConfigger

class Snippets : 
    def run(self) :
        self._initializeInfrustructures()
    
    def _initializeInfrustructures(self) : 
        loggingAuxiliary.loggingConfigger.instance.configConsoleLogging()

instance = Snippets()
instance.run()