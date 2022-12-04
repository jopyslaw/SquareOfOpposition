import tkinter as tk
from interface import Mygui 

root = tk.Tk()
root.title('Kwadrat logiczny')
root.geometry('800x600')
gui = Mygui(root)
root.mainloop()


'''
#Stworzenie okna
window = tk.Tk()
window.geometry("800x600")

#Input dla użytkownika

S = tk.Entry(window)
P = tk.Entry(window)



#Stworzenie canvy
canvas = tk.Canvas(window, width=400, height=400)

#Zmienne do przechowywania tekstu dla danego przypadku
SaPText = 'SaP'
SiPText = 'SiP'
SePText = 'SeP'
SoPText = 'SoP'

#Zdania kategoryczne
SaP = tk.Label(window, text=SaPText, anchor=tk.W)
SaP.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
SaP_window = canvas.create_window(0,150, anchor=tk.NW, window=SaP)

SeP = tk.Label(window, text=SePText, anchor=tk.W)
SeP.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
SeP_window = canvas.create_window(200,150, anchor=tk.NW, window=SeP)

SiP = tk.Label(window, text=SiPText, anchor=tk.W)
SiP.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
SiP_window = canvas.create_window(0,300, anchor=tk.NW, window=SiP)

SoP = tk.Label(window, text=SoPText, anchor=tk.W)
SoP.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
SoP_window = canvas.create_window(200, 300, anchor=tk.NW, window=SoP)

#Spakowanie canvy
canvas.pack()

#Rysowanie strzałek
canvas.create_line(80,160,180,160, arrow=tk.BOTH) #SaP <-> SeP
canvas.create_line(10,150,10,300, arrow=tk.LAST) #Sap <-> SiP
canvas.create_line(40,180,200,300, arrow=tk.BOTH) #Sap <-> SoP
canvas.create_line(80,310,200,310, arrow=tk.BOTH) #SiP <-> SoP
canvas.create_line(20,300,200,170, arrow=tk.BOTH) #SiP <-> SeP
canvas.create_line(210,180,210,300, arrow=tk.BOTH) #SeP <-> SoP

#Głowna pętla programu
window.mainloop()
'''