from utilities.subprocessHelper import subprocessHelper 

class dotnetTool : 
    @staticmethod
    def getInstance() :
        return _instance

    @property
    def commandNew(self) :
        return "new"

    @property
    def templateSln(self) :
        return "sln" #solution file

    def addCommandOption(self, options, command) :
        return subprocessHelper.getInstance().addOption(options, command)

    def addNewTemplateOption(self, options, template) :
        return subprocessHelper.getInstance().addOption(options, template)

    def addNewOutputOption(self, options, directory) :
        return subprocessHelper.getInstance().addOption(
            options, 
            [
                "--output", 
                "\"{0}\"".format(directory) #add sourounding quotes
            ]
            )

    def addNewNameOption(self, options, name) :
        return subprocessHelper.getInstance().addOption(options, ["--name", name])
        
    def addHelpOption(self, options) :
        return subprocessHelper.getInstance().addOption(options, "--help")

    @property
    def _execution(self) :
        return "dotnet"

    def run(self, options, stdoutEncoding) :
        return subprocessHelper.getInstance().run(self._execution, options, stdoutEncoding)

_instance = dotnetTool()