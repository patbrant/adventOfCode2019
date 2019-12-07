from Point import Point 
from Mover import Mover

class ManhattenDistance:
    inputPath = "day03/input.txt"
    wire1Path = []
    wire2Path = []
    wire1Points = [Point(0,0)]
    wire2Points = [Point(0,0)]
    crossingPoints = []

    def calculateShortesManhattenDistance(self):
        self.readWirePaths()
        for move in self.wire1Path:
            direction = move[0]
            amount = int(move[1:])

            mover = Mover(self.wire1Points)
            mover.move(direction, amount)

        
        for move in self.wire2Path:
            direction = move[0]
            amount = int(move[1:])
            for i in range(amount):
                mover = Mover(self.wire1Points)
                mover.move(direction, amount)
                self.checkCrossing()
        
        xySums = []
        for crossing in self.crossingPoints:
            print("Crossing Point: [", crossing.x, ",", crossing.y, "]")
            xySums.append(abs(crossing.x) + abs(crossing.y))
        return min(xySums)

    def readWirePaths(self):
        file = open(self.inputPath, "r")
        wires = file.read().split("\n")
        self.wire1Path = wires[0].split(",") #"R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",") # wires[0].split(",")
        self.wire2Path = wires[1].split(",") #"U62,R66,U55,R34,D71,R55,D58,R83".split(",") # wires[1].split(",")

    def checkCrossing(self):
        wire2Point = self.wire2Points[len(self.wire2Points) - 1]
        for wire1Point in self.wire1Points:
            if (wire2Point.x == wire1Point.x and wire2Point.y == wire1Point.y):
                self.crossingPoints.append(wire2Point)

print(ManhattenDistance().calculateShortesManhattenDistance())