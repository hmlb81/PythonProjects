import pylint
import pylint.lint

class pylintConfigApplication : 
    @staticmethod
    def getInstance() :
        return _application

    def showHelp(self) :
        options = ["--help"]
        pylint.lint.Run(options)

    def generateRcfile(self) :
        options = ["--generate-rcfile"]
        pylint.lint.Run(options)

_application = pylintConfigApplication()