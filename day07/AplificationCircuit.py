from IntComputer import IntComputer

class ApplicationCircuit:

    firstAmplifierInput = 0
    phaseSequence = [0, 1, 2, 3, 4]
    solutions = []

    def run(self):
        for p1 in range(0,5):
            for p2 in range(0, 5):
                if (p2 == p1):
                    continue
                for p3 in range(0, 5):
                    if (p3 in [p1, p2]):
                        continue
                    for p4 in range(0, 5):
                        if (p4 in [p1, p2, p3]):
                            continue
                        for p5 in range(0, 5):
                            if (p5 in [p1, p2, p3, p4]):
                                continue
                            self.calcThrustersForCombination([p1, p2, p3, p4, p5])
        
        print("max thruster: ", max(self.solutions))

    def calcThrustersForCombination(self, phaseSequence):
        output1 = self.runAmplifier(phaseSequence[0], self.firstAmplifierInput)
        output2 = self.runAmplifier(phaseSequence[1], output1)
        output3 = self.runAmplifier(phaseSequence[2], output2)
        output4 = self.runAmplifier(phaseSequence[3], output3)
        output5 = self.runAmplifier(phaseSequence[4], output4)
        self.solutions.append(output5)

    def runAmplifier(self, phase, inputSignal):
        outputs = IntComputer("day07/input.txt").calculateOutputValues([phase, inputSignal])
        return outputs[-1]

ApplicationCircuit().run()