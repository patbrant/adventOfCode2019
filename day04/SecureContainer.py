class SecureContainer:

    matchingCounter = 0

    def run(self):
        startNum = 172851
        endNum = 675869

        for number in range(startNum, endNum):
            self.checkRequirements(number)
        print(self.matchingCounter)

    def checkRequirements(self, number):
        numAsStr = str(number)
        digitWasAdjacent = ""
        digitWasNotAdjacent = []
        for charIndex in range(len(numAsStr) - 1):
            if (numAsStr[charIndex] > numAsStr[charIndex + 1]):
                return
            if (numAsStr[charIndex] in digitWasNotAdjacent):
                continue

            if (numAsStr[charIndex] == numAsStr[charIndex + 1]):
                if (numAsStr[charIndex] in digitWasAdjacent):
                    digitWasAdjacent = digitWasAdjacent[:-1]
                    digitWasNotAdjacent.append(numAsStr[charIndex])
                else:
                    digitWasAdjacent +=  numAsStr[charIndex]

        if (len(digitWasAdjacent) != 0):
            self.matchingCounter += 1
            print("possible passwords", number)


SecureContainer().run()
#SecureContainer().checkRequirements(666999)
#SecureContainer().checkRequirements(699999)
#SecureContainer().checkRequirements(123456)
#SecureContainer().checkRequirements(123334)
#SecureContainer().checkRequirements(233334)
#SecureContainer().checkRequirements(113334)
#SecureContainer().checkRequirements(112233)
#SecureContainer().checkRequirements(123444)
#SecureContainer().checkRequirements(111122)