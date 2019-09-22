import enum
from utilities.collectionsHelper import *

# NONE (meet ascii char) -> UncertainText
# UncertainText (meet ascii char) -> SingleAsciiText
# UncertainText (meet non ascii char) -> NONE(discarding text) : the text could be sense-less
# UncertainText (meet '\0') -> Ucs2TextExpectingAsciiChar : the char met treat as valid ucs-2 char
# SingleAsciiText (meet '\0') -> NONE
# SingleAsciiText (meet ascii char) -> SingleAsciiText
# SingleAsciiText (meet non ascii char) -> NONE (text not end with '\0')
# Ucs2TextExpectingAsciiChar (meet ascii char) -> Ucs2TextExpectingNullChar
# Ucs2TextExpectingAsciiChar (meet '\0') -> Ucs2TextExpectingEndingNullByte
# Ucs2TextExpectingEndingNullByte (meet '\0') -> NONE
# Ucs2TextExpectingEndingNullByte (meet not '\0') -> NONE
# Ucs2TextExpectingNullChar (meet '\0') -> Ucs2TextExpectingAsciiChar
# Ucs2TextExpectingNullChar (meet not '\0') -> NONE
class asciiTextScannerScanningState : 
    NONE = 0 #no ascii text found
    UncertainText = 1
    SingleAsciiText = 2
    Ucs2TextExpectingAsciiChar = 3
    Ucs2TextExpectingNullChar = 4
    Ucs2TextExpectingEndingNullByte = 5

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
        elif (self._state == asciiTextScannerScanningState.Ucs2TextExpectingAsciiChar) :
            self._scanWhenUcs2TextExpectingAsciiChar(byte, userState)
        elif (self._state == asciiTextScannerScanningState.Ucs2TextExpectingEndingNullByte) :
            self._scanWhenUcs2TextExpectionEndingNullByte(byte, userState)
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
            return
    
    def _scanWhenUncertainText(self, byte, userState) :
        isNullChar = self._isNullChar(byte)
        isAsciiChar = self._isAsciiChar(byte)
        if isNullChar :
            self._processingBytes.append(byte)
            self._state = asciiTextScannerScanningState.Ucs2TextExpectingAsciiChar #treat text as usc-2 text
            return
        elif isAsciiChar :
            self._processingBytes.append(byte)
            self._state = asciiTextScannerScanningState.SingleAsciiText
            return
        else :
            #single ascii byte, just treat as noisy
            self._resetScanningState()
            return
        
    def _scanWhenSingleAsciiText(self, byte, userState) :
        isNullChar = self._isNullChar(byte)
        isAsciiChar = self._isAsciiChar(byte)
        if isNullChar :
            self._processingBytes.append(byte)
            self._raiseTextFound(True, userState)
            self._resetScanningState()
            return
        elif isAsciiChar :
            self._processingBytes.append(byte)
            return
        else :
            #text not end with '\0', do not append end byte
            self._raiseTextFound(True, userState)
            self._resetScanningState()
            return
    
    def _scanWhenUcs2TextExpectingAsciiChar(self, byte, userState) :
        isNullChar = self._isNullChar(byte)
        if isNullChar :
            self._processingBytes.append(byte)
            self._state = asciiTextScannerScanningState.Ucs2TextExpectingEndingNullByte
            return
        else :
            #text not end with '\0', do not append end byte
            self._raiseTextFound(False, userState)
            self._resetScanningState()
            return
    
    def _scanWhenUcs2TextExpectionEndingNullByte(self, byte, userState) :
        isNullChar = self._isNullChar(byte)
        if isNullChar :
            self._processingBytes.append(byte)
            self._raiseTextFound(False, userState)
            self._resetScanningState()
            return
        else :
            collectionsHelper.getInstance().checkAndPopLastElement(self._processingBytes, None) #remove last '\0' element
            self._raiseTextFound(False, userState)
            self._resetScanningState()
            return
    
    def _raiseTextFound(self, isSingleAsciiText, userState) :
        processingBytesLength = len(self._processingBytes)
        processingText = None
        processingTextLength = 0
        endsWithNullChar = False
        if isSingleAsciiText :
            processingText = self._processingBytes.decode("ascii")
        else :
            processingText = self._processingBytes.decode("utf_16_le")
        
        processingTextLength = processingBytesLength
        endsWithNullChar = processingText.endswith("\0")        
        
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
    