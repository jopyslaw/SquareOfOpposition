class State:
    def __init__(self, name):
        self.stateName = name
        self.extendState = []
    

    def addExtendState(self, states):
        for i in states:
            self.extendState.append(i)