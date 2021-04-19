
class Resident:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature
        self.location = False

    def getName(self):
        return self.name

    def getTemperature(self):
        return self.temperature

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def __str__(self):
        if(self.location):
            return self.name+" is inside the house, the preferred tempurature is: "+ str(self.temperature)
        else:
            return self.name + " is ouside the house, the preferred tempurature is: " + str(self.temperature)