from tkinter import *
from dotenv import load_dotenv
from os import environ

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
        self.states = [] # tablica przechowująca stany
        self.selectedStates = [] #tablica przechowująca wybory użtykownika dotycząca stanów
        self.selectedStateNumber = IntVar(self.app, 0)
        self.toContinue = True
        self.currentIteration = 0
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
        generatedStates = [self.SaPText + ' & ' + self.SiPText, self.SiPText + ' & ' + self.SoPText, self.SoPText + ' & ' + self.SePText]
        self.states.append(generatedStates)
    

    def userChoice(self):
        self.top = Toplevel(self.master)
        self.top.geometry('500x200')
        self.top.title('Choice option')

        self.newWindow = Frame(self.top)

        main_label = Label(self.newWindow, text = environ.get('PROGRAM_TITLE'))
        main_label.grid(row = 0, column = 0, sticky = N)

        select1 = Radiobutton(self.newWindow, text=self.states[self.currentIteration][0], variable=self.selectedStateNumber, value=0)
        select1.grid(row=1, column=0, sticky=N)

        select2 = Radiobutton(self.newWindow, text=self.states[self.currentIteration][1], variable=self.selectedStateNumber, value=1)
        select2.grid(row=2, column=0, sticky=N)

        select3 = Radiobutton(self.newWindow, text=self.states[self.currentIteration][2], variable=self.selectedStateNumber, value=2)
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
        self.selectedStates.append(self.selectedStateNumber.get())
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

        self.stateMachine = Toplevel(self.master)
        self.stateMachine.geometry('500x200')
        self.stateMachine.title('Choice option')

        self.newWindow2 = Frame(self.stateMachine)

        main_label = Label(self.newWindow2, text = environ.get('STATE_MACHINE'))
        main_label.grid(row = 0, column = 0, sticky = N)


        #print(self.selectedStates)



        reverseStates = self.states.copy()
        reverseUserChoice = self.selectedStates.copy()

        #reverseStates.reverse()
        #reverseUserChoice.reverse()
        Label(self.newWindow2, text='0').grid(row = 1, column=0, sticky=N)
        for (data,index,rowIndex) in zip(reverseStates, reverseUserChoice, range(0,len(reverseUserChoice))):
            Label(self.newWindow2, text=f'{rowIndex+1}. ' + data[index]).grid(row = rowIndex+2, column=0, sticky=N)
        
        self.newWindow2.pack()


    

    