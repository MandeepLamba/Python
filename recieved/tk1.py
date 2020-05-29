from tkinter import Tk

'''Code Shows way to use pack method
  for pacing widgets on window
'''
# from tkinter import *  

parent = Tk()
parent.title("My Window")
parent.geometry("400x500")
# redbutton = Button(parent, text = "Red", fg = "red")  
# redbutton.pack( side = LEFT)  
# greenbutton = Button(parent, text = "Black", fg = "black")  
# greenbutton.pack( side = RIGHT )  
# bluebutton = Button(parent, text = "Blue", fg = "blue")  
# bluebutton.pack( side = TOP )  
# blackbutton = Button(parent, text = "Green", fg = "green")  
# blackbutton.pack( side = BOTTOM)  
parent.mainloop()  

'''Code Shows way to use grid method
   for pacing widgets on window
'''
##from tkinter import *  
##parent = Tk()
###parent.geometry("400x250")  
##name = Label(parent,text = "Name").grid(row = 0, column = 0)  
##e1 = Entry(parent).grid(row = 0, column = 1)  
##password = Label(parent,text = "Password").grid(row = 1, column = 0)  
##e2 = Entry(parent).grid(row = 1, column = 1)  
##submit = Button(parent, text = "Submit").grid(row = 4, column = 0)  
##parent.mainloop() 


'''Code Shows way to use place method
   for pacing widgets on window
'''

##from tkinter import *  
##top = Tk()  
##top.geometry("400x250")  
##name = Label(top, text = "Name").place(x = 30,y = 50)  
##email = Label(top, text = "Email").place(x = 30, y = 90)  
##password = Label(top, text = "Password").place(x = 30, y = 130)  
##e1 = Entry(top).place(x = 80, y = 50)  
##e2 = Entry(top).place(x = 80, y = 90)  
##e3 = Entry(top).place(x = 95, y = 130)  
##top.mainloop()  
