from tkinter import *

class Mygui():
    def __init__(self, master):
        #Stworzenie ramki
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
        self.create_widgets()
    
    def create_widgets(self):
        #Główny tytuł
        self.main_label = Label(self.app, text = "Witaj w programie Trójkąt logiczny")
        self.main_label.grid(row = 0, column = 1, sticky = N)
        #Następny tytuł
        
        self.s_label = Label(self.app, text="Podaj S: ")
        self.s_label.grid(row = 1, column = 0, sticky = N)
        self.s = Entry(self.app)
        self.s.grid(row = 1, column = 1, sticky = W)

        self.affirmation_label = Label(self.app, text="Podaj twierdzenie: ")
        self.affirmation_label.grid(row = 2, column = 0, sticky = N)
        self.affirmation = Entry(self.app)
        self.affirmation.grid(row=2, column=1, sticky=N)

        self.negation_label = Label(self.app, text="Podaj przeczenie: ")
        self.negation_label.grid(row = 3, column = 0, sticky = N)
        self.negation = Entry(self.app)
        self.negation.grid(row=3, column=1, sticky=N)

        self.p_label = Label(self.app, text="Podaj P: ")
        self.p_label.grid(row = 4, column = 0, sticky = N)
        self.p = Entry(self.app)
        self.p.grid(row = 4, column = 1, sticky = N)

        self.p_label = Label(self.app, text="Wybierz typ podanego zdania: ")
        self.p_label.grid(row = 5, column = 0, sticky = N)
        self.typeOfQuestionA = Radiobutton(self.app, text='SaP', variable=self.selectedType, value='a')
        self.typeOfQuestionA.grid(row=6, column=0, sticky=N)

        
        self.typeOfQuestionE = Radiobutton(self.app, text='SeP', variable=self.selectedType, value='e')
        self.typeOfQuestionE.grid(row=7, column=0, sticky=N)

    
        self.typeOfQuestionI = Radiobutton(self.app, text='SiP', variable=self.selectedType, value='i')
        self.typeOfQuestionI.grid(row=8, column=0, sticky=N)

       
        self.typeOfQuestionO = Radiobutton(self.app, text='SoP', variable=self.selectedType, value='o')
        self.typeOfQuestionO.grid(row=9, column=0, sticky=N)

        self.isQuestionTrue = Label(self.app, text="Czy zdanie jest prawdziwe: ")
        self.isQuestionTrue.grid(row=10, column=0, sticky=N)

        self.isQuestionTrue = Radiobutton(self.app, text='True', variable=self.isTrue, value=True)
        self.isQuestionTrue.grid(row=11, column=0, sticky=N)

        self.isQuestionFalse = Radiobutton(self.app, text='False', variable=self.isTrue, value=False)
        self.isQuestionFalse.grid(row=11, column=1, sticky=N)


        #Przycisk do dodania nowych danych
        self.draw_square = Button(self.app, text="Narysuj kwadrat", command=self.show_data)
        self.draw_square.grid(row = 5, column = 3, sticky = E)

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

        match self.selectedType:
            case 'a':
                pass
            case 'i':
                pass

            case 'o':
                pass
            case 'e':
                if(self.isTrue):
                    SiP = False
                    if(SeP == True):
                        SaP == False
                        if(SaP == False):
                            SoP == True
                else:
                    SiP = True

        self.SaPText = 'Każdy ' + s_value + ' ' + self.getValue(SaP) + ' ' + p_value
        self.SiPText = 'Niektóre ' + s_value+ ' ' + self.getValue(SiP) + ' ' + p_value
        self.SePText = 'Żaden ' + s_value + ' ' + self.getValue(SeP) + ' ' + p_value
        self.SoPText = 'Niektóre ' + s_value + ' ' + self.getValue(SaP) + ' ' + p_value

        self.SaP.config(text=self.SaPText)
        self.SiP.config(text=self.SiPText)
        self.SeP.config(text=self.SePText)
        self.SoP.config(text=self.SoPText)

        print(self.SaPText, self.SiPText, self.SePText, self.SoPText)
    
    def getValue(self, value):
        affirmation_value = self.affirmation.get()
        negation_value = self.negation.get()

        if(value):
            return affirmation_value
        else:
            return negation_value




    