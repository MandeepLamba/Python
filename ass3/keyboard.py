from tkinter import Canvas, Tk
win = Tk()
win.title("My Window")
win.geometry("500x600")
win.config(bg='lightblue')


w = Canvas(win, width=500, height=600)
x1,y1,x2,y2= 230, 270, 270, 330
w.create_rectangle(x1,y1,x2,y2, width=2)
w.pack()

def key_press(event):
    print("key pressed", event.char, event.keysym, event.keycode)
def uppress(event):
    print("up arrow pressed")
    x1=x1-5
    x2=x2-5
    w.create_rectangle(x1,y1,x2,y2, width=2)
    w.pack()
def downpress(event):
    print("down arrow pressed")
def rightpress(event):
    print("right arrow pressed")
def leftpress(event):
    print("left arrow pressed")

win.bind('<Key>', key_press)
win.bind('<Up>', uppress)
win.bind('<Down>', downpress)
win.bind('<Right>', rightpress)
win.bind('<Left>', leftpress)
win.bind()
win.mainloop()