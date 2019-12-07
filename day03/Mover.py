from Point import Point

class Mover:
    wirePath = []

    def __init__(self, wirePath):
        self.wirePath = wirePath

    def getWirePath(self):
        return self.wirePath

    def move(self, direction, amount):
        for i in range(amount):
            if (direction == "R"):
                self.right()
            elif (direction == "D"):
                self.down()
            elif (direction == "L"):
                self.left()
            elif (direction == "U"):
                self.up()

    def right(self):
        lastPoint = self.wirePath[len(self.wirePath) - 1]
        self.wirePath.append(Point(lastPoint.x + 1, lastPoint.y))
        
    def down(self):
        lastPoint = self.wirePath[len(self.wirePath) - 1]
        self.wirePath.append(Point(lastPoint.x, lastPoint.y - 1))

    def left(self):
        lastPoint = self.wirePath[len(self.wirePath) - 1]
        self.wirePath.append(Point(lastPoint.x - 1, lastPoint.y))

    def up(self):
        lastPoint = self.wirePath[len(self.wirePath) - 1]
        self.wirePath.append(Point(lastPoint.x, lastPoint.y + 1))