from tkinter import Frame, Tk

win = Tk()
win.title("My Window")
win.wm_geometry("400x500")
frame1 = Frame(win)
frame1.pack(side = 'left')
frame2 = Frame(win)
frame2.pack(side = 'right')
win.mainloop()
