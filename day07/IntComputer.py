from Opcode import Opcode
from ParameterMode import ParameterMode

class IntComputer:
    inputPath = ""
    programCode = []
    incrementValue = 1
    instructionPointer = 0
    inputValues = []
    inputValuePointer = 0
    outputValues = []

    def __init__(self, inputPath):
        self.inputPath = inputPath

    def calculateOutputValues(self, inputValues):
        self.inputValues = inputValues
        self.readProgramCode()
        self.runProgram()
        return self.outputValues

    def readProgramCode(self):
        file = open(self.inputPath, "r")
        programChunks = file.read().split(",")
        #programChunks = "1,1,1,4,99,5,6,0,99".split(",") # test data
        self.programCode = list(map(int, programChunks))

    def runProgram(self):
        while(True):
            instruction = str(self.programCode[self.instructionPointer])
            opcode = int(instruction[-2:])
            parameterModes = "0000000" + instruction[0:len(instruction) - 2]
            if (opcode == Opcode.HALT):
                break
            self.runInstruction(opcode, parameterModes, self.instructionPointer)
            self.instructionPointer = self.instructionPointer + self.incrementValue

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
            input1 = self.getValueOfAddressAt(instructionPointer + 1, ParameterMode.IMMEDIATE)
            self.getFromAddress(input1)
        elif (opcode == Opcode.SAVE_AT_ADDRESS):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, ParameterMode.IMMEDIATE)
            self.saveAtAddress(input1, self.inputValues[self.inputValuePointer])
            self.inputValuePointer += 1
        elif (opcode == Opcode.JUMP_IF_TRUE):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, int(parameterModes[-1:]))
            input2 = self.getValueOfAddressAt(instructionPointer + 2, int(parameterModes[len(parameterModes) - 2]))
            if (input1 != 0):
                self.incrementValue = 0
                self.instructionPointer = input2
            else:
                self.incrementValue = 3
        elif (opcode == Opcode.JUMP_IF_FALSE):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, int(parameterModes[-1:]))
            input2 = self.getValueOfAddressAt(instructionPointer + 2, int(parameterModes[len(parameterModes) - 2]))
            if (input1 == 0):
                self.incrementValue = 0
                self.instructionPointer = input2
            else:
                self.incrementValue = 3
        elif (opcode == Opcode.LESS_THAN):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, int(parameterModes[-1:]))
            input2 = self.getValueOfAddressAt(instructionPointer + 2, int(parameterModes[len(parameterModes) - 2]))
            outputIndex = self.programCode[instructionPointer + 3]
            if (input1 < input2):
                self.programCode[outputIndex] = 1
            else:
                self.programCode[outputIndex] = 0
            self.incrementValue = 4

        elif (opcode == Opcode.EQUALS):
            input1 = self.getValueOfAddressAt(instructionPointer + 1, int(parameterModes[-1:]))
            input2 = self.getValueOfAddressAt(instructionPointer + 2, int(parameterModes[len(parameterModes) - 2]))
            outputIndex = self.programCode[instructionPointer + 3]
            if (input1 == input2):
                self.programCode[outputIndex] = 1
            else:
                self.programCode[outputIndex] = 0
            self.incrementValue = 4

    
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
        self.outputValues.append(self.programCode[index])
        #print(self.programCode[index])
        self.incrementValue = 2

    def getValueOfAddressAt(self, index, parameterMode):
        if (parameterMode == ParameterMode.IMMEDIATE):
            return self.programCode[index]
        elif (parameterMode == ParameterMode.POSITION):
            return self.programCode[self.programCode[index]]