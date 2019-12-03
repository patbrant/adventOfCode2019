from Opcode import Opcode

class Main:
    inputPath = "day02/input.txt"
    programCode = []

    def calculateValueAtPosition0(self):
        self.readProgramCode()
        self.restoreProgram()
        self.runProgram()
        print("Program code after execution: ", self.programCode)
        return self.programCode[0]

    def readProgramCode(self):
        file = open(self.inputPath, "r")
        programChunks = file.read().split(",")
        #programChunks = "1,1,1,4,99,5,6,0,99".split(",") # test data
        self.programCode = list(map(int, programChunks))

    def restoreProgram(self):
        self.programCode[1] = 12
        self.programCode[2] = 2

    def runProgram(self):
        for x in range(len(self.programCode)):
            if (x % 4 == 0):
                opcode = self.programCode[x]
                if (opcode == Opcode.HALT):
                    return
                self.runInstruction(opcode, x)

    def runInstruction(self, opcode, instructionPointer):
        input1 = self.getValueOfAddressAt(instructionPointer + 1)
        input2 = self.getValueOfAddressAt(instructionPointer + 2)
        outputIndex = self.programCode[instructionPointer + 3]
        if (opcode == Opcode.ADDITION):
            self.add(input1, input2, outputIndex)
        elif (opcode == Opcode.MULTIPLICATION):
            self.multiply(input1, input2, outputIndex)
    
    def add(self, input1, input2, outputIndex):
        self.programCode[outputIndex] = input1 + input2

    def multiply(self, input1, input2, outputIndex):
        self.programCode[outputIndex] = input1 * input2

    def getValueOfAddressAt(self, index):
        return self.programCode[self.programCode[index]]

print("Value at position 0 after execution:", Main().calculateValueAtPosition0())