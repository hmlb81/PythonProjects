import subprocess

class subprocessHelper : 
    @staticmethod
    def getInstance() :
        return _instance

    #run execution [options], stdoutEncoding
    def run(self, execution, options, stdoutEncoding) :
        commandText = execution
        commandText = self._appendOptionsToCommandText(commandText, options)

        processStdout = None
        if (stdoutEncoding is not None) :
            processStdout = subprocess.PIPE

        process = subprocess.Popen(commandText, stdout=processStdout)
        process.wait()
        return self._checkAndReadStdout(process, stdoutEncoding)

    def _appendOptionsToCommandText(self, commandText, options) :
        if (options is None) :
            return commandText

        raise AssertionError("todo:implement")
        return commandText

    def _checkAndReadStdout(self, process, stdoutEncoding) :
        if (stdoutEncoding is None) :
            return None

        raise AssertionError("todo:implement")

_instance = subprocessHelper()