import os
import sys
from utilities.subprocessHelper import subprocessHelper

class pipTool : 
    @staticmethod
    def getInstance() :
        return _instance

    def __init__(self) :
        self._pythonDirectory = None

    @property
    def executionPath(self) :
        return os.path.join(self._pythonDirectory, "Scripts", "pip.exe")

    @property
    def commandInstall(self) :
        return "install" #install packages

    @property
    def commandHelp(self) :
        return "help"

    def addCommandOption(self, options, command) :
        return subprocessHelper.getInstance().addOption(options, command)

    def addInstallPackageOption(self, options, package) :
        return subprocessHelper.getInstance().addOption(options, package)

    def run(self, options, stdoutEncoding) :
        exepath = self.executionPath
        return subprocessHelper.getInstance().run(exepath, options, stdoutEncoding)

    def _autoConfig(self) :
        self._pythonDirectory = self._findPythonInstallDirectory()

    def _findPythonInstallDirectory(self) :
        return self._findPythonInstallDirectoryByExecutionPathImpl()

    def _findPythonInstallDirectoryByExecutionPathImpl(self) :
        executionPath = sys.executable
        pythonDirectory = os.path.dirname(executionPath)
        return pythonDirectory

_instance = pipTool()
_instance._autoConfig() #pylint: disable=protected-access #supress pylint warning for module internal implementation