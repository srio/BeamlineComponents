from InsertionDevice import InsertionDevice

class Undulator(InsertionDevice):

    def __init__(self, K_vertical, K_horizontal, period_length, periods_number):
        InsertionDevice.__init__(self, K_vertical, K_horizontal, period_length, periods_number)

    def criticalFrequency(self):
        pass

    def criticalWavelength(self):
        pass

    def criticalEnergy(self):
        pass