import random


class Insect:
    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.lengthOfFlight = 0

    def setFlight(self):
        self.lengthOfFlight = random.randint(0, 10)

    def getFlight(self):
        return self.lengthOfFlight

    def getName(self):
        return self.name
