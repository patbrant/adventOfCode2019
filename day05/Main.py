from Opcode import Opcode
from ParameterMode import ParameterMode

class Main:
    inputPath = "day05/input.txt"
    programCode = []
    incrementValue = 1

    def calculateValueAtPosition0(self):
        self.readProgramCode()
        self.runProgram()
        print("Program code after execution: ", self.programCode)
        return self.programCode[0]

    def readProgramCode(self):
        file = open(self.inputPath, "r")
        programChunks = file.read().split(",")
        #programChunks = "1,1,1,4,99,5,6,0,99".split(",") # test data
        self.programCode = list(map(int, programChunks))

    def runProgram(self):
        x = 0
        while(True):
            instruction = str(self.programCode[x])
            opcode = int(instruction[-2:])
            parameterModes = "0000000" + instruction[0:len(instruction) - 2]
            if (opcode == Opcode.HALT):
                break
            self.runInstruction(opcode, parameterModes, x)
            x = x + self.incrementValue

    def runInstruction(self, opcode, parameterModes, instructionPointer):
        if (opcode == Opcode.ADDITION):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, int(parameterModes[-1:]))
            input2 = self.getValueOfAddressAt(instructionPointer + 2, int(parameterModes[len(parameterModes) - 2]))
            outputIndex = self.programCode[instructionPointer + 3]
            self.add(input1, input2, outputIndex)
        elif (opcode == Opcode.MULTIPLICATION):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, int(parameterModes[-1:]))
            input2 = self.getValueOfAddressAt(instructionPointer + 2, int(parameterModes[len(parameterModes) - 2]))
            outputIndex = self.programCode[instructionPointer + 3]
            self.multiply(input1, input2, outputIndex)
        elif (opcode == Opcode.GET_FROM_ADDRESS):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, 1)
            self.getFromAddress(input1)
        elif (opcode == Opcode.SAVE_AT_ADDRESS):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, 1)
            self.saveAtAddress(input1, 1)
    
    def add(self, input1, input2, outputIndex):
        self.programCode[outputIndex] = input1 + input2
        self.incrementValue = 4

    def multiply(self, input1, input2, outputIndex):
        self.programCode[outputIndex] = input1 * input2
        self.incrementValue = 4

    def saveAtAddress(self, index, value):
        self.programCode[index] = value
        self.incrementValue = 2

    def getFromAddress(self, index):
        print(self.programCode[index])
        self.incrementValue = 2

    def getValueOfAddressAt(self, index, parameterMode):
        if (parameterMode == ParameterMode.IMMEDIATE):
            return self.programCode[index]
        elif (parameterMode == ParameterMode.POSITION):
            return self.programCode[self.programCode[index]]

Main().calculateValueAtPosition0()