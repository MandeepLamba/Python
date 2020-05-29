# Create only GUI for registration form(Use all possible widgets)
# from tkinter import *
from tkinter import Button, Checkbutton, Entry, Label, Tk, messagebox
screen = Tk()
screen.title("Register")
screen.geometry('500x600')
screen.config(bg='lightblue')

# lables
Label(screen,fg='white', text='Name', background = 'lightblue', font = ('Arial 20')).grid(row = 0,column = 0)
Label(screen,fg='white', text='Class', background = 'lightblue', font = ('Arial 20')).grid(row = 1,column = 0)

#Entries
Entry(screen).grid(row = 0,column = 1)
Entry(screen).grid(row = 1,column = 1)

#CheckButtons
Checkbutton(screen,text="Male",height=3, width = 10,padx=10,pady=10).grid(row = 3,column = 0)
Checkbutton(screen,text="Female",height=3, width = 10,padx=10,pady=10).grid(row = 3,column = 1)


#buttons
def submit():
    messagebox.showinfo(title='Message',message='Submitted!')
Button(text='Submit',font = ('Arial 14'),command = submit).grid()
screen.mainloop()

