"""
Represents a square stop.
"""

from BeamlineComponents.Stop.StopRectangle import StopRectangle

class AperatureSquare(StopRectangle):
    def __init__(self, side_length):
        StopRectangle.__init__(self, side_length, side_length)

    def sideLength(self):
        return self.lengthVertical()
