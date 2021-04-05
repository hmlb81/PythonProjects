import random

#simple linear relation : y = c * x, given x, y, get c

class simpleLinearGuess :
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
        elif abs(a.deviation) <= abs(b.deviation) :
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

    def checkAndUseGuess(self, precision) :
        if self._bestGuess is None :
            return

        if abs(self._bestGuess.deviation) > precision :
            return

        self._c = self._bestGuess.c
        return


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
        
        #for until find best guess
        exiting = False
        while not exiting :
            status.checkAndUseGuess(precision)
            hasMatchedGuess = not status.c is None #python 不支持is not写法
            exiting = exiting or hasMatchedGuess
            self._traceif(hasMatchedGuess, "find matched guess {0}".format(status.bestGuess))
            if exiting :
                break #找到答案，提前返回

            #未找到答案，按step更新guess
            self._nextGuess(status, x, y, precision)
            
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

    def _nextGuess(self, status, x, y, precision) :
        deviationOld = status.bestGuess.deviation

        if deviationOld == 0.0 :
            self._trace("之前的guess已足够小，不需要再次guess，这是一条异常路径")
            return

        c = status.bestGuess.c + status.step
        d = self._calcDeviation(c, x, y)
        g = simpleLinearGuess(c, d)
        status.guess(g)

        deviationNew = status.bestGuess.deviation
        
        #调整步长，需要以合适的步长，缩短迭代时长
        changePercent = abs(d) / abs(deviationOld) #注意，此处不能使用deviationNew/deviationOld
        absStep = abs(status.step)
        if abs(deviationNew) >= abs(deviationOld) :#偏差未缩小（本次偏差反而放大），过犹不及，缩小step
            absStep = absStep - absStep * changePercent
        else : #偏差缩小中，不调整step（甚至应该部分放大step，提升收敛的速度）
            absStep = absStep + absStep * changePercent 

        if (absStep <= 0.0) :
            absStep = precision #避免step变为0

        if (d > 0) : #注意，此处使用d，不是deviationNew
            status.step = absStep * 1.0
        else :
            status.step = absStep * -1.0

        self._trace("Guess {0} to {1} stepping {2}".format(g, status.bestGuess, status.step))

    def _trace(self, message) :
        if self._tracing :
            print(message)

    def _traceif(self, condition, message) :
        if condition :
            self._trace(message)

    
_instance = simpleLinearCalculator()
    