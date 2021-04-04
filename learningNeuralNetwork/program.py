import os

#append top level module directory
_s_file_abs_path = os.path.abspath(__file__)
_s_file_dir = os.path.dirname(_s_file_abs_path)
os.sys.path.append(os.path.join(_s_file_dir, "../"))

from applications.exampleApplication import exampleApplication
from programFrameworks.simpleProgramFramework import simpleProgramBase

class program(simpleProgramBase) :
    def _dorun(self) :
        app = exampleApplication.getInstance()
        app.calcKilometerMileRelation()

_instance = program()
_instance.run()