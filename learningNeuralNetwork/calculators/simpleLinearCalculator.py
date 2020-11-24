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

    def getLastGuessValue(self) :
        length = len(self._ccollection)
        if (length <= 0) :
            return None

        return self._ccollection[length - 1]

    def checkGuessValue(self, x) :
        guessValue = self.getLastGuessValue()
        if guessValue == None :
            return None
        
        return x * guessValue

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
        
        maxGuessCount = 1000000 #max guess count
        guessCounter = 0
        exceedGuessCount = False
        isFinished = False
        while not isFinished :
            guessCounter = guessCounter + 1

            #check
            checkValue = status.getLastGuessValue() #验算结果

            # if exceeds max guess count, exit loop
            exceedGuessCount = exceedGuessCount or (guessCounter > maxGuessCount)
            if (exceedGuessCount) :
                isFinished = True
            
        return status

    def _determineInitialC(self, status) :
        random.seed()

        initialc = random.random() #intial c in [0, 1]
        status.guess(initialc)

    

_instance = simpleLinearCalculator()
    