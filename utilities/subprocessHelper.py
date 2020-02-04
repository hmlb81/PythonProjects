import collections
import subprocess

class subprocessHelper : 
    @staticmethod
    def getInstance() :
        return _instance

    def addOption(self, options, option) :
        if options is None :
            options = []

        options.append(option)
        return options

    #run execution [options], stdoutEncoding
    def run(self, execution, options, stdoutEncoding) :
        commandText = execution
        commandText = self._appendOptionsToCommandText(commandText, options)

        processStdout = None
        if stdoutEncoding is not None :
            processStdout = subprocess.PIPE

        process = subprocess.Popen(commandText, stdout=processStdout)
        process.wait()
        return self._checkAndReadStdout(process, stdoutEncoding)

    def _appendOptionsToCommandText(self, commandText, options) :
        if options is None :
            return commandText

        for option in options :
            commandText = self._appendOptionToCommandText(commandText, option)

        return commandText
    
    def _appendOptionToCommandText(self, commandText, option) :
        isString = isinstance(option, str)
        isIteratable = isinstance(option, collections.Iterable)
        if isString :
            return self._appendSimpleOptionToCommandText(commandText, option) #since string is iteratable, this branch need execute before iteratable
        elif isIteratable :
            return self._appendListOptionToCommandText(commandText, option)
        else :
            return self._appendSimpleOptionToCommandText(commandText, option)
            
    def _appendSimpleOptionToCommandText(self, commandText, option) :
        commandText = commandText + " " #add seperator
        commandText = commandText + "{0}".format(option)
        return commandText
        
    def _appendListOptionToCommandText(self, commandText, option) :
        for optionPart in option :
            commandText = self._appendOptionToCommandText(commandText, optionPart)
        
        return commandText

    def _checkAndReadStdout(self, process, stdoutEncoding) :
        if stdoutEncoding is None :
            return None

        raise AssertionError("todo:implement")

_instance = subprocessHelper()