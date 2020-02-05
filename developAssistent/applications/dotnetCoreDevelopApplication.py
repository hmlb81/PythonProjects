import os
from tools.dotnetTool.dotnetTool import dotnetTool

class dotnetCoreDevelopApplication : 
    def __init__(self) :
        self._csharpCodeRepositoryDirectory = None
        self._componentLibraries = "ComponentLibraries"
        self._componentTestConsole = "TestConsole"
        self._serviceSupervisior = "ServiceSupervisor"

    @staticmethod
    def getInstance() :
        return _instance

    @property
    def csharpCodeRepositoryDirectory(self) :
        return self._csharpCodeRepositoryDirectory

    @csharpCodeRepositoryDirectory.setter
    def csharpCodeRepositoryDirectory(self, direcoty) :
        self._csharpCodeRepositoryDirectory = direcoty

    @property
    def componentLibrariesDirectory(self) :
        return os.path.join(self._csharpCodeRepositoryDirectory, self._componentLibraries)

    @property
    def componentLibrariesSolutionName(self) :
        return self._componentLibraries

    @property
    def componetTestConsoleDirectory(self) :
        return os.path.join(self.componentLibrariesDirectory, self._componentTestConsole)

    @property
    def componentTestConoleProjectName(self) :
        return self._componentTestConsole

    @property 
    def serviceSupervisorDirectory(self) :
        return os.path.join(self.componentLibrariesDirectory, self._serviceSupervisior)

    @property 
    def serviceSupervisorProjectName(self) :
        return self._serviceSupervisior

    def showDotnetCoreHelp(self) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addHelpOption(options)
        dotnet.run(options, None)   

    def showDotnetCommandNewHelp(self) :
        return self._showDotnetCommandHelp(dotnetTool.getInstance().commandNew)

    def newSolution(self, solutionName, outputDirectory) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, dotnet.commandNew)
        options = dotnet.addNewTemplateOption(options, dotnet.templateSln)
        options = dotnet.addNewNameOption(options, solutionName)
        options = dotnet.addNewOutputOption(options, outputDirectory)
        dotnet.run(options, None)

    def newConsoleProject(self, projectName, outputDirectory) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, dotnet.commandNew)
        options = dotnet.addNewTemplateOption(options, dotnet.templateConsole)
        options = dotnet.addNewNameOption(options, projectName)
        options = dotnet.addNewOutputOption(options, outputDirectory)
        dotnet.run(options, None)

    def newClasslibProject(self, projectName, outputDirectory) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, dotnet.commandNew)
        options = dotnet.addNewTemplateOption(options, dotnet.templateClasslib)
        options = dotnet.addNewNameOption(options, projectName)
        options = dotnet.addNewOutputOption(options, outputDirectory)
        dotnet.run(options, None)

    def _showDotnetCommandHelp(self, command) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, command)
        options = dotnet.addHelpOption(options)
        dotnet.run(options, None)


_instance = dotnetCoreDevelopApplication()