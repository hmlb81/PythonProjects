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
        #set root logger to console
        rootConfig = { 
            "level" : consoleLevel,
            "handlers" : ["console"]
        } 
        
        config = {
            "version" : 1,
            "handlers" : handlersConfig,
            "root" : rootConfig
        }
        
        logging.config.dictConfig(config)
        logging.info("loggingConfigger.configConsoleLogging:finished.")

instance = loggingConfigger()