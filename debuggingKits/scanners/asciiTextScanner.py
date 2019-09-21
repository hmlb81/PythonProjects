import enum

# NONE (meet ascii char) -> UncertainText
# UncertainText (meet ascii char) -> SingleAsciiText
# UncertainText (meet non ascii char) -> NONE(discarding text) : the text could be sense-less
# UncertainText (meet '\0') -> Ucs2TextExpectingAsciiChar : the char met treat as valid ucs-2 char
# SingleAsciiText (meet '\0') -> NONE
# SingleAsciiText (meet ascii char) -> SingleAsciiText
# SingleAsciiText (meet non ascii char) -> NONE (text not end with '\0')
# Ucs2TextExpectingAsciiChar (meet ascii char) -> Ucs2TextExpectingNullChar
# Ucs2TextExpectingAsciiChar (meet '\0') -> NONE
# Ucs2TextExpectingNullChar (meet '\0') -> Ucs2TextExpectingAsciiChar
class asciiTextScannerScanningState : 
    NONE = 0 #no ascii text found
    UncertainText = 1
    SingleAsciiText = 2
    Ucs2TextExpectingAsciiChar = 3
    Ucs2TextExpectingNullChar = 4

import ctypes

class asciiTextScanner : 
    def __init__(self) :
        self._state = asciiTextScannerScanningState.NONE
        self._processingBytes = bytearray()
        self._handlerTextFound = None
    
    @property
    def handlerTextFound(self) :
        return self._handlerTextFound
    
    @handlerTextFound.setter
    def handlerTextFound(self, handler) :
        self._handlerTextFound = handler
        
    def scan(self, byte, userState) :
        if (self._state == asciiTextScannerScanningState.NONE) :
            self._scanWhenNone(byte, userState)
        elif (self._state == asciiTextScannerScanningState.UncertainText) :
            self._scanWhenUncertainText(byte, userState)
        elif (self._state == asciiTextScannerScanningState.SingleAsciiText) :
            self._scanWhenSingleAsciiText(byte, userState)
        else :
            raise AssertionError("Unsupported scanning state")
    
    def _scanWhenNone(self, byte, userState) :
        isNullChar = self._isNullChar(byte)
        isAsciiChar = self._isAsciiChar(byte)
        if isNullChar :
            return
        elif isAsciiChar :
            self._processingBytes.clear()
            self._processingBytes.append(byte)
            self._state = asciiTextScannerScanningState.UncertainText
            return
        else :
            raise AssertionError("todo:implement")
    
    def _scanWhenUncertainText(self, byte, userState) :
        isAsciiChar = self._isAsciiChar(byte)
        if isAsciiChar :
            self._processingBytes.append(byte)
            self._state = asciiTextScannerScanningState.SingleAsciiText
        else :
            raise AssertionError("todo:implement")
        
    def _scanWhenSingleAsciiText(self, byte, userState) :
        isNullChar = self._isNullChar(byte)
        isAsciiChar = self._isAsciiChar(byte)
        if isNullChar :
            raise AssertionError("todo:implement")
        elif isAsciiChar :
            raise AssertionError("todo:implement")
        else :
            #text not end with '\0', do not append end byte
            self._raiseTextFound(True, userState)
            self._resetScanningState()
            return
    
    def _raiseTextFound(self, isSingleAsciiText, userState) :
        processingBytesLength = len(self._processingBytes)
        processingText = None
        processingTextLength = 0
        endsWithNullChar = False
        if isSingleAsciiText :
            processingText = self._processingBytes.decode("ascii")
            processingTextLength = processingBytesLength
            endsWithNullChar = processingText.endswith("\0")
        else :
            raise AssertionError("todo:implement")
        
        #try remove noisy notifications
        validProcessingTextLength = processingTextLength
        if endsWithNullChar :
            validProcessingTextLength -= 1
            
        if validProcessingTextLength <= 1 :
            return #if text length less then 1 character, return 
        
        #notify processing text
        if (self._handlerTextFound != None) :
            self._handlerTextFound(processingText, userState)
    
    def _resetScanningState(self) :
        self._processingBytes.clear()
        self._state = asciiTextScannerScanningState.NONE
        
    def _isNullChar(self, byte) :
        return byte == 0 #0 == '\0'
    
    def _isAsciiChar(self, byte) :
        return (byte > 0) and (byte < 128) #judge character(use simplest implementation)
    