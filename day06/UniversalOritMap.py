
class UniversalOrbitMap:
    inputPath = "day06/input.txt"
    orbitCounter = 0
    directOrbits = []

    def run(self):
        self.readOrbitMap()
        for directOrbit in self.directOrbits:
            self.orbitCounter += 1
            self.checkOrbit(directOrbit[0])
        print(self.orbitCounter)
            
    def readOrbitMap(self):
        file = open(self.inputPath, "r")
        directOrbits = file.read().split("\n")
        for directOrbit in directOrbits:
            orbit = directOrbit.split(")")
            self.directOrbits.append(orbit)


    def checkOrbit(self, orbitToCheck):
        for orbit in self.directOrbits:
            if (orbit[1] == orbitToCheck):
                self.orbitCounter += 1
                self.checkOrbit(orbit[0])

UniversalOrbitMap().run()