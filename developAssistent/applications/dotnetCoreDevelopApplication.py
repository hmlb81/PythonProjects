from tools.dotnetTool.dotnetTool import dotnetTool

class dotnetCoreDevelopApplication : 
    @staticmethod
    def getInstance() :
        return _instance

    def showDotnetCoreHelp(self) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addHelpOption(options)
        dotnet.run(options, None)    


_instance = dotnetCoreDevelopApplication()