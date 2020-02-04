from programFrameworks.simpleProgramFramework import simpleProgramBase
from utilities.subprocessHelper import subprocessHelper
from utilities.wellknownPythonEncodings import wellknownPythonEncodings

class riddlesProgram(simpleProgramBase) :
    def _dorun(self) : 
        self._testSubProcessHelperRun()

    def _testSubProcessHelperRun(self) :
        execution = "ping"
        encoding = wellknownPythonEncodings.getInstance().mbcs
        options = None
        options = subprocessHelper.getInstance().addOption(options, ["-n", 1])
        output = subprocessHelper.getInstance().run(execution, options, encoding)
        print(output) #debugging code for eliminating pylint warnings

_program = riddlesProgram()
_program.run()