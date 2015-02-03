from ElectronBeam import ElectronBeam

class PencilBeam(ElectronBeam):
    def __init__(energy_in_GeV, energy_spread, average_current, ):
        ElectronBeam.__init__(self,
                               energy_in_GeV=energy_in_GeV,
                               energy_spread=energy_spread,
                               average_current=average_current,
                               electrons=1)