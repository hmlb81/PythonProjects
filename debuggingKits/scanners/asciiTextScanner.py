import enum

# NONE (meet ascii char) -> UncertainText
# UncertainText (meet ascii char) -> SingleAsciiText
# UncertainText (meet non ascii char) -> NONE(discarding text) : the text could be sense-less
# UncertainText (meet '\0') -> Ucs2TextExpectingAsciiChar : the char met treat as valid ucs-2 char
# SingleAsciiText (meet '\0') -> NONE
# Ucs2TextExpectingAsciiChar (meet ascii char) -> Ucs2TextExpectingNullChar
# Ucs2TextExpectingAsciiChar (meet '\0') -> NONE
# Ucs2TextExpectingNullChar (meet '\0') -> Ucs2TextExpectingAsciiChar
class asciiTextScannerScanningState : 
    NONE = 0 #no ascii text found
    UncertainText = 1
    SingleAsciiText = 2
    Ucs2TextExpectingAsciiChar = 3
    Ucs2TextExpectingNullChar = 4

class asciiTextScanner : 
    def __init__(self) :
        self._state = asciiTextScannerScanningState.NONE
        
    def scan(self, byte, userState) :
        raise AssertionError("todo:implement")
    