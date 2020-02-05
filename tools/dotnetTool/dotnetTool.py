from utilities.subprocessHelper import subprocessHelper 

class dotnetTool : 
    @staticmethod
    def getInstance() :
        return _instance

    def addHelpOption(self, options) :
        return subprocessHelper.getInstance().addOption(options, "--help")

    @property
    def _execution(self) :
        return "dotnet"

    def run(self, options, stdoutEncoding) :
        return subprocessHelper.getInstance().run(self._execution, options, stdoutEncoding)

_instance = dotnetTool()