import logging
import logging.config

#Logging module configger
class loggingConfigger : 
    #config logging module to console
    def configConsoleLogging(self) :
        consoleHandlerClass = "logging.StreamHandler"
        consoleFormatter = "brief"
        consoleLevel = logging.INFO
        consoleStream = "ext://sys.stdout"
        consoleHandlerConfig = { 
            "class" : consoleHandlerClass,
            "formatter" : consoleFormatter,
            #"level" : consoleLevel,
            #"stream" : consoleStream
        }
        handlersConfig = { "console" : consoleHandlerConfig }
        config = {
            "version" : 1,
            "handlers" : handlersConfig
        }
        print(config) #TODO:debug code, removing later 
        logging.config.dictConfig(config)
        print("loggingConfigger configConsoleLogging called.") #TODO: debug code removing later


instance = loggingConfigger()