"""
Represents a square aperture.
"""

from ApertureRectangle import ApertureRectangle

class ApertureSquare(ApertureRectangle):
    def __init__(self, side_length):
        AperatureRectangle.__init__(self, side_length, side_length)

    def sideLength(self):
        return self.lengthVertical()
