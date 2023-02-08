import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.lengthOfFlight = 0

    def setFlight(self):
        self.lengthOfFlight = random.randint(0, 10)

    def getFlight(self):
        return self.lengthOfFlight
