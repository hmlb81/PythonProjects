import os

#append top level module directory
os.sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from applications.developKitsDeployApplication import developKitsDeployApplication
from applications.dotnetCoreDevelopApplication import dotnetCoreDevelopApplication
from applications.packagingApplication import packagingApplication
from programFrameworks.simpleProgramFramework import simpleProgramBase

#program entry
class program(simpleProgramBase) : 
    def _dorun(self) :
        #self._operateDotnetSolution()
        #self._deployDevelopKits()
        self._pack()
        
    def _initializeInfrustrutures(self) :
        super()._initializeInfrustrutures()

        dotnetCoreDevelopApplication.getInstance().csharpCodeRepositoryDirectory = "D:\\GitHub\\CsharpProjects\\"

    def _operateDotnetSolution(self) :
        dotnetApp = dotnetCoreDevelopApplication.getInstance()
        print(dotnetApp.serviceCenterTestProjectPath) #debugging codes

        #dotnetApp.newUnitTestProject(dotnetApp.serviceCenterTestProjectName, dotnetApp.serviceCenterTestDirectory)
    
    def _deployDevelopKits(self) :
        app = developKitsDeployApplication.getInstance()
        app.showPipHelp()

        #app.installPyInstaller()

    def _pack(self) :
        app = packagingApplication.getInstance()
        filepath = os.path.abspath(__file__)
        targetFilePath = os.path.join(os.path.dirname(filepath), "..\\HelloWorld\\program.py")
        print(targetFilePath) #debugging codes for elimate warning
        app.printDescription() #debugging code for elimate warning
        #packagingApplication.getInstance().pack("HelloWorld", targetFilePath)

_program = program()
_program.run()