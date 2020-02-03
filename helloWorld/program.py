import os

#append top level module directory
os.sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from programFrameworks.simpleProgramFramework import simpleProgramBase

class program(simpleProgramBase) :
    def _dorun(self) :
        print("hello world")

_program = program()
_program.run()