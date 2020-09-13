import os

#append top level module directory
os.sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from applications.exampleApplication import exampleApplication
from programFrameworks.simpleProgramFramework import simpleProgramBase

class program(simpleProgramBase) :
    def _dorun(self) :
        exampleApplication.getInstance().calcKilometerMileRelation()

_instance = program()
_instance.run()