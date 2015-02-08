"""
Represents a circular aperture.
"""

from AperatureEllipse import AperatureEllipse

class AperatureCircle(AperatureEllipse):
    def __init__(self, diameter):
        AperatureEllipse.__init__(self, diameter, diameter)

    def diameter(self):
        return self.axisA()