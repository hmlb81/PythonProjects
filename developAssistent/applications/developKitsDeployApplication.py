from tools.pythonTools.pipTool import pipTool

class developKitsDeployApplication : 
    @staticmethod
    def getInstance() :
        return _instance

    def showPipHelp(self) :
        pip = pipTool.getInstance()
        options = None

        options = pip.addCommandOption(options, pip.commandHelp)
        pip.run(options, None)

    def installPyInstaller(self) :
        pip = pipTool.getInstance()
        options = None

        options = pip.addCommandOption(options, pip.commandInstall)
        options = pip.addInstallPackageOption(options, "pyinstaller")
        pip.run(options, None)

_instance = developKitsDeployApplication()