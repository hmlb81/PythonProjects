import os
from tools.dotnetTool.dotnetTool import dotnetTool

class dotnetCoreDevelopApplication : 
    def __init__(self) :
        self._csharpCodeRepositoryDirectory = None
        self._componentLibraries = "ComponentLibraries"
        self._componentTestConsole = "TestConsole"
        self._serviceCenter = "ServiceCenter"
        self._serviceCenterTest = "ServiceCenterTest"

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
    def componentTestConsoleProjectPath(self) :
        return os.path.join(self.componetTestConsoleDirectory, self.componentTestConoleProjectName + ".csproj")

    @property 
    def serviceCenterDirectory(self) :
        return os.path.join(self.componentLibrariesDirectory, self._serviceCenter)

    @property 
    def serviceCenterProjectName(self) :
        return self._serviceCenter

    @property
    def serviceCenterProjectPath(self) :
        return os.path.join(self.serviceCenterDirectory, self.serviceCenterProjectName + ".csproj")

    @property
    def serviceCenterTestDirectory(self) :
        return os.path.join(self.componentLibrariesDirectory, self._serviceCenterTest)

    @property
    def serviceCenterTestProjectName(self) :
        return self._serviceCenterTest

    @property
    def serviceCenterTestProjectPath(self) :
        return os.path.join(self.serviceCenterTestDirectory, self.serviceCenterTestProjectName + ".csproj")

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
        self._newProject(dotnetTool.getInstance().templateConsole, projectName, outputDirectory)

    def newClasslibProject(self, projectName, outputDirectory) :
        self._newProject(dotnetTool.getInstance().templateClasslib, projectName, outputDirectory)

    def newUnitTestProject(self, projectName, outputDirectory) :
        self._newProject(dotnetTool.getInstance().templateMstest, projectName, outputDirectory)

    #add project file reference to target project
    def addProjectRefrence(self, targetProject, referenceProject) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, dotnet.commandAdd)
        options = dotnet.addAddProjectOption(options, targetProject)
        options = dotnet.addAddReferenceOption(options, referenceProject)
        dotnet.run(options, None)

    def addPackageReference(self, targetProject, package) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, dotnet.commandAdd)
        options = dotnet.addAddProjectOption(options, targetProject)
        options = dotnet.addAddPackageOption(options, package)
        dotnet.run(options, None)

    def _showDotnetCommandHelp(self, command) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, command)
        options = dotnet.addHelpOption(options)
        dotnet.run(options, None)

    def _newProject(self, template, projectName, outputDirectory) :
        dotnet = dotnetTool.getInstance()
        options = None
        options = dotnet.addCommandOption(options, dotnet.commandNew)
        options = dotnet.addNewTemplateOption(options, template)
        options = dotnet.addNewNameOption(options, projectName)
        options = dotnet.addNewOutputOption(options, outputDirectory)
        dotnet.run(options, None)


_instance = dotnetCoreDevelopApplication()