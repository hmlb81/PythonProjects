class wellknownPythonEncodings : 
    @staticmethod
    def getInstance() :
        return _instance

    @property
    def mbcs(self) :
        return "mbcs" #python internal encoding, for windows only

    @property
    def ascii(self) :
        return "ascii"

    @property
    def utf8(self) :
        return "utf_8" #usually alias with "utf-8"

    @property
    def hz(self) :
        return "hz" #Simplified Chinese, contains gb2312

_instance = wellknownPythonEncodings()