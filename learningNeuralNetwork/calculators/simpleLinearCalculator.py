import random

#simple linear relation : y = c * x, given x, y, get c

class simpleLinearGuess :
    def __init__(self) :
        self._c = None #猜测的系数值 
        self._deviation = None #猜测结果，与实际结果之间的偏差

    def __init__(self, c, deviation) :
        self._c = c
        self._deviation = deviation

    def __str__(self) :
        return "(c:{0}, d:{1})".format(self._c, self._deviation)

    def __eq__(self, other) :
        return isinstance(other, simpleLinearGuess) \
            and (self._c == other._c) \
            and (self._deviation == other._deviation)

    @property
    def c(self) :
        return self._c

    @c.setter
    def c(self, value) :
        self._c = value

    @property
    def deviation(self) :
        return self._deviation

    @deviation.setter
    def deviation(self, value) :
        self._deviation = value

    @staticmethod
    def optimizer(a, b) :
        if a is None :
            return b
        elif b is None :
            return a
        elif abs(a._deviation) <= abs(b._deviation) :
            return a
        else :
        	return b

class simpleLinearCalculateStatus :
    def __init__(self) :
        self._c = None #_c = final c result
        self._step = None
        self._bestGuess = None
        
    def guess(self, g) :
        self._bestGuess = simpleLinearGuess.optimizer(g, self._bestGuess)

    @property
    def c(self) :
        return self._c

    @c.setter
    def c(self, value) :
        self._c = value

    @property
    def step(self) :
        return self._step

    @step.setter
    def step(self, value) :
        self._step = value

    @property
    def bestGuess(self) :
        return self._bestGuess


class simpleLinearCalculator :
    def __init__(self) :
        self._tracing = False

    @property
    def tracing(self) :
        return self._tracing

    @tracing.setter
    def tracing(self, value) :
        self._tracing = value

    @staticmethod
    def getInstance() :
        return _instance

    def calculate(self, x, y, precision) :
        status = simpleLinearCalculateStatus()
		
        self._initStatus(status, x, y)
        
        
        #maxGuessCount = 1000000 #max guess count
        #guessCounter = 0
        #exceedGuessCount = False
        #isFinished = False
        #while not isFinished :
            #guessCounter = guessCounter + 1

            ##check
            #checkValue = status.checkGuessValue(x) #验算结果
            #deviation = self._calculateDeviation(y, checkValue)

            # if exceeds max guess count, exit loop
            #exceedGuessCount = exceedGuessCount or (guessCounter > maxGuessCount)
            #if exceedGuessCount :
                #isFinished = True
            
        return status

    def _generateRandomNumber(self) :
        random.seed()
        number = random.random()
        return number

    def _initStatus(self, status, x, y) :
        c = self._generateRandomNumber()
        d = self._calcDeviation(c, x, y)
        g = simpleLinearGuess(c, d)
        status.guess(g)
        
        status.step = self._generateRandomNumber()

        print("g:{0}, step:{1}".format(status.bestGuess, status.step))

    def _calcDeviation(self, c, x, y) :
        v = c * x
		
        #v + deviation = y; deviation = y - v
        d = y - v
        return d

    def _trace(self, message) :
        if self._tracing :
            print(message)

    
_instance = simpleLinearCalculator()
    