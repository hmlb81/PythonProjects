import logging
import logging.config

#Logging module configger
class loggingConfigger : 
    #config logging module to console
    def configConsoleLogging(self) :
        consoleHandlerClass = "logging.StreamHandler"
        consoleLevel = logging.INFO
        consoleStream = "ext://sys.stdout"
        consoleHandlerConfig = { 
            "class" : consoleHandlerClass,
            "level" : consoleLevel,
            "stream" : consoleStream
        }
        handlersConfig = { "console" : consoleHandlerConfig }
        config = {
            "version" : 1,
            "handlers" : handlersConfig
        }
        
        logging.config.dictConfig(config)
        root = logging.root #TODO: debugging code,removing later
        logging.info("loggingConfigger.configConsoleLogging:finished.")

instance = loggingConfigger()