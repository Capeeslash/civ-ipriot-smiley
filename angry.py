import time
from smiley import Smiley


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyebrows(self):
        eyebrows = [10, 13, 18, 19, 20, 21]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [26, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.GREEN if wide_open else self.complexion()

    def blink(self, delay=0.25):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
