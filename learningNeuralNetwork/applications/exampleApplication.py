from calculators.simpleLinearCalculator import simpleLinearCalculator, simpleLinearCalculateStatus, simpleLinearGuess
import logging

#example from "neural network in python"
class exampleApplication : 
    @staticmethod
    def getInstance() :
        return _instance

    def test(self) :
        gn = None
        g1 = simpleLinearGuess(1, 0.1) 
        g2 = simpleLinearGuess(2, 0.2)

        self._testGuessEqual() #相等比较
        self._testGuessOptimizer()

    def calcKilometerMileRelation(self) :
        calculator = simpleLinearCalculator.getInstance()
        kilometersValue = 100
        milesValue = 62.137
        precision = 0.001
        
        calculator.tracing = True
        status = calculator.calculate(kilometersValue, milesValue, precision)
        self._dumpSimpleLinearRelation("kilometer", "mile", status)

    def _dumpSimpleLinearRelation(self, xname, yname, status) :
        #get c
        c = None
        if (status is None) :
            pass #do nothing
        else :
            c = status.c

        if (c is None) :
            logging.info("failed to get relation between {0}, {1}".format(xname, yname))
        else :
            logging.info("{0} = {1} * {2}".format(xname, c, yname))

    def _testGuessOptimizer(self) :
        gn = None
        g1 = simpleLinearGuess(1, 0.1) 
        g2 = simpleLinearGuess(2, 0.2)
        
        testcases = [
            [gn, gn],
            [g1, g1],
            [g2, g2],
            [g1, g2],
        ]

        for tc in testcases:
            g1 = tc[0]
            g2 = tc[1]
            print("o({0}, {1} is {2})".format(g1, g2, simpleLinearGuess.optimizer(g1, g2)))
            print("o({0}, {1} is {2})".format(g2, g1, simpleLinearGuess.optimizer(g2, g1)))
            pass

    def _testGuessEqual(self) :
        gn = None
        g1 = simpleLinearGuess(1, 0.1) 
        g2 = simpleLinearGuess(2, 0.2)

        print("g1==None:{0}".format(g1 == gn))
        print("g1!=Nont:{0}".format(g1 != gn))
        print("None==g1:{0}".format(gn == g1))
        print("None!=g1:{0}".format(gn != g1))
        print("g1==g1:{0}".format(g1 == g1))
        print("g1!=g1:{0}".format(g1 != g1))
        print("g1==g2:{0}".format(g1==g2))
        print("g1!=g2:{0}".format(g1!=g2))


_instance = exampleApplication()