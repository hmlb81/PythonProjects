import os

#append top level module directory
os.sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from programFrameworks.simpleProgramFramework import simpleProgramBase

class program(simpleProgramBase) : pass

_program = program()
_program.run()