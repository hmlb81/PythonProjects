from programFrameworks.simpleProgramFramework import simpleProgramBase
from utilities.subprocessHelper import subprocessHelper

class riddlesProgram(simpleProgramBase) :
    def _dorun(self) : 
        self._testSubProcessHelperRun()

    def _testSubProcessHelperRun(self) :
        execution = "ping"
        subprocessHelper.getInstance().run(execution, None, None)

_program = riddlesProgram()
_program.run()