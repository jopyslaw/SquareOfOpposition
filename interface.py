from tkinter import *
from dotenv import load_dotenv
from os import environ
import graphviz
from LogicalSquare import LogicalSquare
load_dotenv()

class Mygui():
    def __init__(self, master):
        #Stworzenie ramki
        self.master = master
        self.app = Frame(master)
        self.app2 = Frame(master)

        self.app.grid()
        self.SaPText = 'SaP'
        self.SiPText = 'SiP'
        self.SePText = 'SeP'
        self.SoPText = 'SoP'
        self.canvas = Canvas(self.app2, width=250, height=400)
        self.selectedType = StringVar(self.app, 'a')
        self.isTrue = BooleanVar(self.app, True)
        #self.states = [] # tablica przechowująca stany
        #self.selectedStates = [] #tablica przechowująca wybory użtykownika dotycząca stanów
        self.selectedStateNumber = IntVar(self.app, 0)
        self.toContinue = True
        self.currentIteration = 0
        self.selectedStateToDecompose = IntVar(self.app, 0)

        self.squares = []
        self.decomposeStates = []
        self.isTrueDec = BooleanVar(self.app, True)
        self.selectedTypeDec = StringVar(self.app, 'a')


        self.create_widgets()
    
    def create_widgets(self):
        #Główny tytuł
        self.main_label = Label(self.app, text = environ.get('PROGRAM_TITLE'))
        self.main_label.grid(row = 0, column = 1, sticky = N)
        #Następny tytuł
        
        self.s_label = Label(self.app, text = environ.get('SUBJECT'))
        self.s_label.grid(row = 1, column = 0, sticky = N)
        self.s = Entry(self.app)
        self.s.grid(row = 1, column = 1, sticky = W)

        self.affirmation_label = Label(self.app, text=environ.get('THEOREM'))
        self.affirmation_label.grid(row = 2, column = 0, sticky = N)
        self.affirmation = Entry(self.app)
        self.affirmation.grid(row=2, column=1, sticky=N)

        self.negation_label = Label(self.app, text=environ.get('NEGATIVE'))
        self.negation_label.grid(row = 3, column = 0, sticky = N)
        self.negation = Entry(self.app)
        self.negation.grid(row=3, column=1, sticky=N)

        self.p_label = Label(self.app, text=environ.get('PREDICAT'))
        self.p_label.grid(row = 4, column = 0, sticky = N)
        self.p = Entry(self.app)
        self.p.grid(row = 4, column = 1, sticky = N)

        self.p_label = Label(self.app, text=environ.get('CATEGORICAL_SENTENCE'))
        self.p_label.grid(row = 5, column = 0, sticky = N)
        self.typeOfQuestionA = Radiobutton(self.app, text='SaP', variable=self.selectedType, value='a')
        self.typeOfQuestionA.grid(row=6, column=0, sticky=N)

        
        self.typeOfQuestionE = Radiobutton(self.app, text='SeP', variable=self.selectedType, value='e')
        self.typeOfQuestionE.grid(row=7, column=0, sticky=N)

    
        self.typeOfQuestionI = Radiobutton(self.app, text='SiP', variable=self.selectedType, value='i')
        self.typeOfQuestionI.grid(row=8, column=0, sticky=N)

       
        self.typeOfQuestionO = Radiobutton(self.app, text='SoP', variable=self.selectedType, value='o')
        self.typeOfQuestionO.grid(row=9, column=0, sticky=N)

        self.isQuestionTrue = Label(self.app, text=environ.get('SENTENCE_STATE'))
        self.isQuestionTrue.grid(row=10, column=0, sticky=N)

        self.isQuestionTrue = Radiobutton(self.app, text='True', variable=self.isTrue, value=True)
        self.isQuestionTrue.grid(row=11, column=0, sticky=N)

        self.isQuestionFalse = Radiobutton(self.app, text='False', variable=self.isTrue, value=False)
        self.isQuestionFalse.grid(row=11, column=1, sticky=N)


        #Przycisk do dodania nowych danych
        self.draw_square = Button(self.app, text=environ.get('DRAW_SQUARE'), command=self.show_data)
        self.draw_square.grid(row = 5, column = 3, sticky = E)
        self.draw_square = Button(self.app, text=environ.get('SHOW_STATE_MACHINE'), command=self.show_state_machine)
        self.draw_square.grid(row = 6, column = 3, sticky = E)
        self.draw_square = Button(self.app, text=environ.get('DECOMPOSE_STATE'), command=self.decompose)
        self.draw_square.grid(row = 7, column = 3, sticky = E)

        self.draw_square_of_opposition()

        self.app.pack()
        self.app2.pack()
        

    def draw_arrows(self):
        self.canvas.create_line(80,160,180,160, arrow=BOTH) #SaP <-> SeP
        self.canvas.create_line(10,150,10,300, arrow=LAST) #Sap <-> SiP
        self.canvas.create_line(40,180,200,300, arrow=BOTH) #Sap <-> SoP
        self.canvas.create_line(80,310,200,310, arrow=BOTH) #SiP <-> SoP
        self.canvas.create_line(20,300,200,170, arrow=BOTH) #SiP <-> SeP
        self.canvas.create_line(210,180,210,300, arrow=BOTH) #SeP <-> SoP


    def draw_square_of_opposition(self): 
        # Miejsce do wyświetlenia nowych danych
        self.SaP = Label(self.app2, text=self.SaPText, anchor=W)
        self.SaP.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        SaP_window = self.canvas.create_window(0,150, anchor=NW, window=self.SaP)

        self.SeP = Label(self.app2, text=self.SePText, anchor=W)
        self.SeP.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        SeP_window = self.canvas.create_window(200,150, anchor=NW, window=self.SeP)

        self.SiP = Label(self.app2, text=self.SiPText, anchor=W)
        self.SiP.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        SiP_window = self.canvas.create_window(0,300, anchor=NW, window=self.SiP)

        self.SoP = Label(self.app2, text=self.SoPText, anchor=W)
        self.SoP.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        SoP_window = self.canvas.create_window(200, 300, anchor=NW, window=self.SoP)

        self.canvas.pack()

        self.draw_arrows()
    
    def show_data(self): 
        s_value = self.s.get()
        p_value = self.p.get()
        SiP = None
        SeP = None
        SaP = None
        SoP = None

        
        match self.selectedType.get():
            case 'a':
                if(self.isTrue.get()):
                    SaP = True
                    SoP = False
                    SiP = True
                    SeP = False
                else:
                    SaP = False
                    SoP = True
                    SiP = None #nieokreślony
                    SeP = None #nieokreślony
            case 'i':
                if(self.isTrue.get()):
                    SiP = True
                    SeP = False
                    SaP = None
                    SoP = None
                else: 
                    SiP = False
                    SeP = True
                    SaP = False
                    SoP = True
            case 'o':
                if(self.isTrue.get()):
                    SoP = True
                    SaP = False
                    SeP = None
                    SiP = None
                else: 
                    SoP = False
                    SaP = True
                    SeP = False
                    SiP = True
            case 'e':
                if(self.isTrue.get()):
                    SeP = True
                    SiP = False
                    SaP = False
                    SoP = True
                else:
                    SeP = False
                    SiP = True
                    SaP = None
                    SoP = None

        self.SaPText = environ.get('EVERYONE') + s_value + ' ' + self.getValue(SaP) + ' ' + p_value
        self.SiPText = environ.get('SOME') + s_value+ ' ' + self.getValue(SiP) + ' ' + p_value
        self.SePText = environ.get('NO_ONE') + s_value + ' ' + self.getValue(SeP) + ' ' + p_value
        self.SoPText = environ.get('SOME') + s_value + ' ' + self.getValue(SoP) + ' ' + p_value

        self.SaP.config(text=self.SaPText)
        self.SiP.config(text=self.SiPText)
        self.SeP.config(text=self.SePText)
        self.SoP.config(text=self.SoPText)

        #print(self.SaPText,'\n' ,self.SiPText, '\n', self.SePText, '\n' ,self.SoPText)
        #print('SiP', SiP, 'SaP', SaP, 'SoP', SoP, 'SeP', SeP)

        self.generateState()

        #print(self.states)

        self.userChoice()
    
    def getValue(self, value):
        affirmation_value = self.affirmation.get()
        negation_value = self.negation.get()
        undefined_value = '?'

        if(value == True or value == None):
            return affirmation_value
        #elif(value == None):
        #    return negation_value
        else:
            return negation_value


    def generateState(self): 
        self.squares.append(LogicalSquare(self.SaPText, self.SePText, self.SiPText, self.SoPText))
        #generatedStates = [self.SaPText + ' & ' + self.SiPText, self.SiPText + ' & ' + self.SoPText, self.SoPText + ' & ' + self.SePText]
        #self.states.append(generatedStates)
    

    def userChoice(self):
        self.top = Toplevel(self.master)
        self.top.geometry('500x500')
        self.top.title('Choice option')

        self.newWindow = Frame(self.top)

        main_label = Label(self.newWindow, text = environ.get('PROGRAM_TITLE'))
        main_label.grid(row = 0, column = 0, sticky = N)

        select1 = Radiobutton(self.newWindow, text=self.squares[self.currentIteration].generatedStates[0].stateName, variable=self.selectedStateNumber, value=0)
        select1.grid(row=1, column=0, sticky=N)

        select2 = Radiobutton(self.newWindow, text=self.squares[self.currentIteration].generatedStates[1].stateName, variable=self.selectedStateNumber, value=1)
        select2.grid(row=2, column=0, sticky=N)

        select3 = Radiobutton(self.newWindow, text=self.squares[self.currentIteration].generatedStates[2].stateName, variable=self.selectedStateNumber, value=2)
        select3.grid(row=3, column=0, sticky=N)

        accept = Button(self.newWindow, text=environ.get('ACCEPT'), command=self.addToList)
        accept.grid(row = 4, column = 0, sticky = N)

        decline = Button(self.newWindow, text=environ.get('DECLINE'), command=self.stop)
        decline.grid(row = 4, column = 1, sticky = N)

        self.newWindow.pack()
    

    def stop(self): 
        self.toContinue = False
        self.top.destroy()
    
    def addToList(self): 
        self.squares[self.currentIteration].setStateToExtend(self.selectedStateNumber.get())
        #self.selectedStates.append(self.selectedStateNumber.get())
        self.top.destroy()
        self.clearInputs()
        self.currentIteration += 1


    def clearInputs(self): 
        self.s.delete(0, END)
        self.affirmation.delete(0, END)
        self.negation.delete(0, END)
        self.p.delete(0, END)

        self.SaPText = ''
        self.SiPText = ''
        self.SaPText = ''
        self.SePText = ''

    def show_state_machine(self):
        self.genSmb()
        self.stateMachine = Toplevel(self.master)
        self.stateMachine.geometry('500x500')
        self.stateMachine.title('Choice option')

        self.newWindow2 = Frame(self.stateMachine)

        main_label = Label(self.newWindow2, text = environ.get('STATE_MACHINE'))
        main_label.grid(row = 0, column = 0, sticky = N)
        
        img = PhotoImage(file='test.gv.png')
        second_lable = Label(self.newWindow2, image = img)
        second_lable.grid(row = 1, column = 0, sticky=N)
        second_lable.image = img
       
        self.newWindow2.pack()

    def genSmb(self):
        g = graphviz.Digraph('Spanning_tree', filename="test.gv", format='png')
        for (index,square) in enumerate(self.squares):
            for (i,state) in enumerate(square.generatedStates):
                prevSquare = self.squares[index - 1]
                if(index == 0):
                    g.edge('0', state.stateName)
                else:
                    g.edge(prevSquare.generatedStates[prevSquare.stateToExtend].stateName, state.stateName)
                
                if(state.extendState != []):
                    print('extend state',state.extendState)
                    with g.subgraph(name='cluster_' + str(state.stateName)) as c:
                        edges = [(state.extendState[0].stateName, state.extendState[1].stateName), 
                            (state.extendState[1].stateName, state.extendState[2].stateName)
                        ]
                        c.edges(edges)
                        c.attr(label='decompose ' + str(index))
                        c.attr(color='black')
                    g.edge(state.stateName, state.extendState[0].stateName)
                    g.edge(state.extendState[2].stateName, state.stateName)

        g.render(format='png')
    


    def decompose(self):
        self.dec = Toplevel(self.master)
        self.dec.geometry('500x500')
        self.dec.title('Choice option')

        self.newWindow3 = Frame(self.dec)

        main_label = Label(self.newWindow3, text = environ.get('STATE_MACHINE'))
        main_label.grid(row = 0, column = 0, sticky = N)
        self.decpomoseBtn = Button(self.newWindow3, text=environ.get('DECOMPOSE_STATE'), command=self.show_decompose)
        self.decpomoseBtn.grid(row = 0, column = 1, sticky = N)

        
        fieldIndex = 0
        for (index,squares) in enumerate(self.squares):
            Label(self.newWindow3, text=index).grid(row = fieldIndex+1, column=0, sticky=N)
            fieldIndex += 1
            Radiobutton(self.newWindow3, text=squares.generatedStates[0].stateName, variable=self.selectedStateToDecompose, value=int(fieldIndex-1)).grid(row = fieldIndex, column=1, sticky=N)
            fieldIndex += 1
            Radiobutton(self.newWindow3, text=squares.generatedStates[1].stateName, variable=self.selectedStateToDecompose, value=int(fieldIndex-1)).grid(row = fieldIndex, column=1, sticky=N)
            fieldIndex += 1
            Radiobutton(self.newWindow3, text=squares.generatedStates[2].stateName, variable=self.selectedStateToDecompose, value=int(fieldIndex-1)).grid(row = fieldIndex, column=1, sticky=N)
        
        self.newWindow3.pack()
    

    def show_decompose(self):
        self.newWindow3.destroy()
        self.dec.destroy()

        self.addDec = Toplevel(self.master)
        self.addDec.geometry('500x500')
        self.addDec.title('Choice option')

        self.newWindow4 = Frame(self.addDec)

        main_label = Label(self.newWindow4, text = environ.get('DECOMPOSE_STATE'))
        main_label.grid(row = 0, column = 0, sticky = N)
        self.decpomoseBtn = Button(self.newWindow4, text=environ.get('DECOMPOSE_STATE'), command=self.addDecomposeState)
        self.decpomoseBtn.grid(row = 0, column = 1, sticky = N)


        self.s_label_dec = Label(self.newWindow4, text = environ.get('SUBJECT'))
        self.s_label_dec.grid(row = 1, column = 0, sticky = N)
        self.s_dec = Entry(self.newWindow4)
        self.s_dec.grid(row = 1, column = 1, sticky = W)

        self.affirmation_label_dec = Label(self.newWindow4, text=environ.get('THEOREM'))
        self.affirmation_label_dec.grid(row = 2, column = 0, sticky = N)
        self.affirmation_dec = Entry(self.newWindow4)
        self.affirmation_dec.grid(row=2, column=1, sticky=N)

        self.negation_label_dec = Label(self.newWindow4, text=environ.get('NEGATIVE'))
        self.negation_label_dec.grid(row = 3, column = 0, sticky = N)
        self.negation_dec = Entry(self.newWindow4)
        self.negation_dec.grid(row=3, column=1, sticky=N)

        self.p_label_dec = Label(self.newWindow4, text=environ.get('PREDICAT'))
        self.p_label_dec.grid(row = 4, column = 0, sticky = N)
        self.p_dec = Entry(self.newWindow4)
        self.p_dec.grid(row = 4, column = 1, sticky = N)

        self.p_label_dec = Label(self.newWindow4, text=environ.get('CATEGORICAL_SENTENCE'))
        self.p_label_dec.grid(row = 5, column = 0, sticky = N)
        self.typeOfQuestionA_dec = Radiobutton(self.newWindow4, text='SaP', variable=self.selectedTypeDec, value='a')
        self.typeOfQuestionA_dec.grid(row=6, column=0, sticky=N)

        
        self.typeOfQuestionE_dec = Radiobutton(self.newWindow4, text='SeP', variable=self.selectedTypeDec, value='e')
        self.typeOfQuestionE_dec.grid(row=7, column=0, sticky=N)

    
        self.typeOfQuestionI_dec = Radiobutton(self.newWindow4, text='SiP', variable=self.selectedTypeDec, value='i')
        self.typeOfQuestionI_dec.grid(row=8, column=0, sticky=N)

       
        self.typeOfQuestionO_dec = Radiobutton(self.newWindow4, text='SoP', variable=self.selectedTypeDec, value='o')
        self.typeOfQuestionO_dec.grid(row=9, column=0, sticky=N)

        self.isQuestionTrue_dec = Label(self.newWindow4, text=environ.get('SENTENCE_STATE'))
        self.isQuestionTrue_dec.grid(row=10, column=0, sticky=N)

        self.isQuestionTrue_dec = Radiobutton(self.newWindow4, text='True', variable=self.isTrueDec, value=True)
        self.isQuestionTrue_dec.grid(row=11, column=0, sticky=N)

        self.isQuestionFalse_dec = Radiobutton(self.newWindow4, text='False', variable=self.isTrueDec, value=False)
        self.isQuestionFalse_dec.grid(row=11, column=1, sticky=N)



        '''
        

        self.decLab1 = Label(self.newWindow4, text = environ.get('FIRST_STATE'))
        self.decLab1.grid(row = 1, column = 0, sticky = N)
        self.decLab1E = Entry(self.newWindow4)
        self.decLab1E.grid(row = 1, column = 1, sticky = W)

        self.decLab2 = Label(self.newWindow4, text=environ.get('SECOND_STATE'))
        self.decLab2.grid(row = 2, column = 0, sticky = N)
        self.decLab2E = Entry(self.newWindow4)
        self.decLab2E.grid(row=2, column=1, sticky=N)

        self.decLab3 = Label(self.newWindow4, text=environ.get('THIRD_STATE'))
        self.decLab3.grid(row = 3, column = 0, sticky = N)
        self.decLab3E = Entry(self.newWindow4)
        self.decLab3E.grid(row=3, column=1, sticky=N)

        self.decLab4 = Label(self.newWindow4, text=environ.get('FOURTH_STATE'))
        self.decLab4.grid(row = 4, column = 0, sticky = N)
        self.decLab4E = Entry(self.newWindow4)
        self.decLab4E.grid(row = 4, column = 1, sticky = N)'''

        self.newWindow4.pack()

    def addDecomposeState(self):
        squareIndex = 0 #4
        if(self.selectedStateToDecompose.get() % 3 == 0):
            squareIndex = self.selectedStateToDecompose.get()
        elif((self.selectedStateToDecompose.get() - 1) % 3 == 0):
            squareIndex = int((self.selectedStateToDecompose.get() - 1) / 3) 
        elif((self.selectedStateToDecompose.get() + 1) % 3 == 0):
            squareIndex = int((self.selectedStateToDecompose.get() + 1) / 3) 
        
        s_value = self.s_dec.get()
        p_value = self.p_dec.get()
        SiP = None
        SeP = None
        SaP = None
        SoP = None

        match self.selectedTypeDec.get():
            case 'a':
                if(self.isTrueDec.get()):
                    SaP = True
                    SoP = False
                    SiP = True
                    SeP = False
                else:
                    SaP = False
                    SoP = True
                    SiP = None #nieokreślony
                    SeP = None #nieokreślony
            case 'i':
                if(self.isTrueDec.get()):
                    SiP = True
                    SeP = False
                    SaP = None
                    SoP = None
                else: 
                    SiP = False
                    SeP = True
                    SaP = False
                    SoP = True
            case 'o':
                if(self.isTrueDec.get()):
                    SoP = True
                    SaP = False
                    SeP = None
                    SiP = None
                else: 
                    SoP = False
                    SaP = True
                    SeP = False
                    SiP = True
            case 'e':
                if(self.isTrueDec.get()):
                    SeP = True
                    SiP = False
                    SaP = False
                    SoP = True
                else:
                    SeP = False
                    SiP = True
                    SaP = None
                    SoP = None

        SaPText = environ.get('EVERYONE') + s_value + ' ' + self.getValue(SaP) + ' ' + p_value
        SiPText = environ.get('SOME') + s_value+ ' ' + self.getValue(SiP) + ' ' + p_value
        SePText = environ.get('NO_ONE') + s_value + ' ' + self.getValue(SeP) + ' ' + p_value
        SoPText = environ.get('SOME') + s_value + ' ' + self.getValue(SoP) + ' ' + p_value

        square = LogicalSquare(SaPText, SePText, SiPText, SoPText)

        print(self.selectedStateToDecompose.get())

        print(squareIndex)

        selectedIndex = abs((self.selectedStateToDecompose.get() - (squareIndex * 3))) 

        print(selectedIndex)

        self.squares[squareIndex].generatedStates[selectedIndex].addExtendState(square.generatedStates)

        print(self.squares)

        self.newWindow4.destroy()
        self.addDec.destroy()

    
