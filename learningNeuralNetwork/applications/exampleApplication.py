from calculators.simpleLinearCalculator import simpleLinearCalculator, simpleLinearCalculateStatus
import logging

#example from "neural network in python"
class exampleApplication : 
    @staticmethod
    def getInstance() :
        return _instance

    def calcKilometerMileRelation(self) :
        calculator = simpleLinearCalculator.getInstance()
        kilometersValue = 100
        milesValue = 62.137
        
        status = calculator.calculate(kilometersValue, milesValue)
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

_instance = exampleApplication()