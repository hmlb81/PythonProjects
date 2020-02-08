from programFrameworks.simpleProgramFramework import simpleProgramBase
from tools.pythonTools.pipTool import pipTool

class riddlesProgram(simpleProgramBase) :
    def _dorun(self) : 
        self._testPipTool()

    def _testPipTool(self) :
        pip = pipTool.getInstance()
        options = None
        pip.run(options, None)
        
_program = riddlesProgram()
_program.run()