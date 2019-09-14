import ctypes

class ctypesHelper : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def convertCtypeArrayToList(self, ctypesArray, validElementCount, convertor) :
        elementIndex = 0
        convertResult = list()
        while elementIndex < validElementCount :
            currentElementIndex = elementIndex
            elementIndex = elementIndex + 1
            
            #handle currentElement
            currentElement = ctypesArray[currentElementIndex]
            convertElement = convertor(currentElement)
            convertResult.append(convertElement)
        
        return convertResult

_instance = ctypesHelper()