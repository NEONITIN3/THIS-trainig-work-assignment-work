from tkinter import filedialog
import tkinter as tk

def openDialog():
    win.filename=filedialog.askopenfile(initialdir="/", title="select File",
                                        filetypes=(("Jpeg file","*.jpg"), ("All files","*.*")))
    print(win.filename)

def saveDialog():
    win.filename = filedialog.asksaveasfile(initialdir="/", title="select File",
                                          filetypes=(("Jpeg file", "*.jpg"), ("All files","*.*")))
    print(win.filename)

def selectdir():
    win.deiconify=filedialog.askdirectory()
    print(win.deiconify)

win=tk.Tk()
win.geometry('700x400')

canvasa1 = tk.Canvas(win,width=600,height=600)

btnopen = tk.Button(win,text='open Dialog', command=openDialog, bg = 'green', fg = 'white')
canvasa1.create_window(50,150,window=btnopen)

btnsave = tk.Button(win,text='save Dialog', command=saveDialog, bg = 'red', fg = 'white')
canvasa1.create_window(150,150,window=btnsave)

btnselect = tk.Button(win,text='select dir', command=selectdir, bg = 'blue', fg = 'white')
canvasa1.create_window(250,150,window=btnselect)

canvasa1.pack()
win.mainloop()