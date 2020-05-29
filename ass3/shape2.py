from tkinter import *
win = Tk()
win.title("My Window")
win.wm_geometry("300x500")
win.config(bg='lightblue')

Button(text='Red',font = ('Arial 14'),command = lambda : win.config(bg='red')).grid()
Button(text='Blue',font = ('Arial 14'),command = lambda : win.config(bg='blue')).grid()
Button(text='Gray',font = ('Arial 14'),command = lambda : win.config(bg='gray')).grid()
Button(text='White',font = ('Arial 14'),command = lambda : win.config(bg='white')).grid()
Button(text='Yellow',font = ('Arial 14'),command = lambda : win.config(bg='yellow')).grid()

mainloop()