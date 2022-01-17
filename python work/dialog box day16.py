#dialog boxes sample
from tkinter import filedialog
import tkinter as tk
def openDialog():
    win.filename=filedialog.askopenfilename(initialdir="/",title="Select file ",filetypes=(("Jpeg files","*.jpg"),("all files","*.*")))
    print(win.filename)
def saveDialog():
    win.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file ",
                                               filetypes=(("Jpeg files", "*.jpg"), ("all files", "*.*")))
    print(win.filename)
def selectdir():
    win.directory = filedialog.askdirectory()
    print(win.directory)


win=tk.Tk()
win.geometry('700x400')
canvas1=tk.Canvas(win,width=600,height=600)
btnopen=tk.Button(win,text='open dialog',command=openDialog,bg='green',fg='white')
canvas1.create_window(50,150,window=btnopen)

btnsave=tk.Button(win,text='save dialog',command=saveDialog,bg='green',fg='white')
canvas1.create_window(150,150,window=btnsave)

btnDir=tk.Button(win,text='open dir',command=selectdir,bg='green',fg='white')
canvas1.create_window(250,100,window=btnopen)
canvas1.pack()
win.mainloop()