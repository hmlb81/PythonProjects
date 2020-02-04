from programFrameworks.simpleProgramFramework import simpleProgramBase
from utilities.subprocessHelper import subprocessHelper

class riddlesProgram(simpleProgramBase) :
    def _dorun(self) : 
        self._testSubProcessHelperRun()

    def _testSubProcessHelperRun(self) :
        execution = "ping"
        options = None
        options = subprocessHelper.getInstance().addOption(options, ["-n", 1])
        subprocessHelper.getInstance().run(execution, options, None)

_program = riddlesProgram()
_program.run()