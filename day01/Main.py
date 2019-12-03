import math

class Main:
    inputPath = "day01/input.txt"

    def calculateFuelSum(self):
        modules = self.readModules()
        resultSum = sum(map(self.calculateFuel, modules))
        return resultSum

    def readModules(self):
        moduleFile = open(self.inputPath, "r")
        moduleList = moduleFile.read().splitlines()
        return map(int, moduleList)

    def calculateFuel(self, mass):
        fuel = math.floor(mass / 3) - 2
        if fuel <= 0:
            return 0
        return fuel + self.calculateFuel(fuel)

print(Main().calculateFuelSum())