from Tkinter import *
from shutil import *

def CopyFonts():
    copyfile(entry1.get() + ".ttf","ARIALN.ttf")
    copyfile(entry1.get() + ".ttf","MORPHEUS.ttf")
    copyfile(entry1.get() + ".ttf","FRIZQT__.ttf")
    copyfile(entry1.get() + ".ttf","skurri.ttf")
    

fen = Tk()
text1 = Label(fen, text = "Nom de la police:  ")
entry1 = Entry(fen)
button1 = Button(fen,text="Copier",command = CopyFonts)
button2 = Button(fen,text="Quitter", command = fen.quit)

text1.grid(row=0)
entry1.grid(row=1)
button1.grid(row=2,column=1)
button2.grid(row=2,column=2)

text1.pack()
entry1.pack()
button1.pack()
button2.pack()

fen.mainloop()
