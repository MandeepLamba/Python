from tkinter import *
scr = Tk()
scr.title("Button - Tkinter Widgetes")
def helloworld():
      print("Hello GUI")
btn = Button(scr, text ="Hello", fg="#FF0000", padx=10, pady=10, command = helloworld)
btn.pack()
scr.mainloop()
