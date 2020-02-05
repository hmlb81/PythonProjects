import os

#append top level module directory
os.sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from applications.dotnetCoreDevelopApplication import dotnetCoreDevelopApplication
from programFrameworks.simpleProgramFramework import simpleProgramBase

#program entry
class program(simpleProgramBase) : 
    def _dorun(self) :
        dotnetApp = dotnetCoreDevelopApplication.getInstance()
        print(dotnetApp.serviceSupervisorProjectPath) #debugging codes
        #dotnetApp.addProjectRefrence(dotnetApp.componentTestConsoleProjectPath, dotnetApp.serviceSupervisorProjectPath)
 
    def _initializeInfrustrutures(self) :
        super()._initializeInfrustrutures()

        dotnetCoreDevelopApplication.getInstance().csharpCodeRepositoryDirectory = "D:\\GitHub\\CsharpProjects\\"

_program = program()
_program.run()