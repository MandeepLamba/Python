from tkinter import *
win = Tk()
win.title("My Window")
win.geometry("500x600")
win.config(bg='lightblue')
w = Canvas(win, width=300, height=500)

# Text
w.create_text(50,50,text="Python")

# Oval
w.create_oval(150,150,80,80,width=2)

# Rectangle
w.create_rectangle(150, 220, 80, 180, width=2)

#Arc
w.create_arc(50, 250, 150, 350, start=0, extent=80, width=2)

#Polygon
point = [50, 300, 110, 400, 260, 500, 240, 450]
w.create_polygon(point, width=2)
w.pack()
mainloop()

# Canvas, Line, Rect, Oval, Arc, Poly, Text