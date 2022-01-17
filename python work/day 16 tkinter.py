import tkinter as tk
from tkinter import messagebox
def ExitWindow():
    msgbox=tk.messagebox.askquestion('Exit','Do you want to exit',icon='warning')
    if msgbox=="yes":
        win.destroy()
    else:
        tk.messagebox.askquestion('return','return to the session')
win=tk.Tk()
can1=tk.Canvas(win,width=300,height=300)