
#simple linear relation : y = c * x, given x, y, get c

class simpleLinearCalculateStatus :
    def __init__(self) :
        self._c = None #_c = final c result

    @property
    def c(self) :
        return self._c

    @c.setter
    def c(self, value) :
        self._c = value

class simpleLinearCalculator : 
    @staticmethod
    def getInstance() :
        return _instance

    def calculate(self, x, y) :
        status = simpleLinearCalculateStatus()

        #determine initial c
        
        #todo:implement
        
        return status

_instance = simpleLinearCalculator()
    