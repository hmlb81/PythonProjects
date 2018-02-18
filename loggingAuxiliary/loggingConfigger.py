import logging
import logging.config

#Logging module configger
class loggingConfigger : 
    #config logging module to console
    def configConsoleLogging(self) :
        consoleHandlerClass = logging.StreamHandler
        consoleHandlerConfig = {}
        handlersConfig = { "console" : consoleHandlerConfig }
        config = {
            "version" : 1,
            "handlers" : handlersConfig
        }
        print(config)
        logging.config.dictConfig(config)
        print("loggingConfigger configConsoleLogging called.")


instance = loggingConfigger()