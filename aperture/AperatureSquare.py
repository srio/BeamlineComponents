"""
Represents a square aperture.
"""

from AperatureRectangle import AperatureRectangle

class AperatureSquare(AperatureRectangle):
    def __init__(self, side_length):
        AperatureRectangle.__init__(self, side_length, side_length)

    def sideLength(self):
        return self.lengthVertical()