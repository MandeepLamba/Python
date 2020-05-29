from tkinter import *   
from tkinter import messagebox 
top = Tk()  
  
top.geometry("300x300")  
  
def fun():
        messagebox.showinfo("Hello Red Button clicked")  
  
  
b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
  
b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10,fg="green",bg="blue")  
  
b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
  
b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = LEFT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)
##b1.pack()  
##  
##b2.pack()  
##  
##b3.pack()  
##  
##b4.pack() 
  
top.mainloop()  
