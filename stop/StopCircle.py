"""
Represents a circular stop.
"""

from StopEllipse import StopEllipse

class StopCircle(StopEllipse):
    def __init__(self, diameter):
        StopEllipse.__init__(self, diameter, diameter)

    def diameter(self):
        return self.axisA()