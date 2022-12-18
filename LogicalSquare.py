from State import State

class LogicalSquare:
    def __init__(self, A, E, I, O):
        self.a = A
        self.e = E
        self.i = I
        self.o = O
        self.generatedStates = self.generateStates()#wygenerowane stany
        self.stateToExtend = None #stan wybrany do roszerzenia
    
    def generateStates(self):
        return [State(self.a + ' & ' + self.i), State(self.i + ' & ' + self.o), State(self.o + ' & ' + self.e)]
    
    def setStateToExtend(self, stateNumber):
        self.stateToExtend = stateNumber