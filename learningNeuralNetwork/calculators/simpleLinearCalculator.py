import random

#simple linear relation : y = c * x, given x, y, get c

class simpleLinearCalculateStatus :
    def __init__(self) :
        self._c = None #_c = final c result
        self._maxCcollectionSize = 10
        self._ccollection = []

    def guess(self, c) :
        self._ccollection.append(c)
        self._maintainCcollection()

    @property
    def c(self) :
        return self._c

    @c.setter
    def c(self, value) :
        self._c = value

    def _maintainCcollection(self) :
        length = len(self._ccollection)
        if length < self._maxCcollectionSize :
            return
            
        self._ccollection.pop(0)

class simpleLinearCalculator : 
    @staticmethod
    def getInstance() :
        return _instance

    def calculate(self, x, y) :
        status = simpleLinearCalculateStatus()

        self._determineInitialC(status) #determine initial c
        
        #todo:implement
        
        return status

    def _determineInitialC(self, status) :
        random.seed()

        initialc = random.random() #intial c in [0, 1]
        status.guess(initialc)

    

_instance = simpleLinearCalculator()
    