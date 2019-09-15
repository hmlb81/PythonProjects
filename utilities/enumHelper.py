import enum

class enumHelper : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def combine(self, values) :
        combineResult = 0
        for value in values :
            combineNumber = value.value
            combineResult |= combineNumber
        
        return combineResult

_instance = enumHelper()