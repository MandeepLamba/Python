from tkinter import Canvas, Tk
win = Tk()
win.title("My Window")
win.geometry("500x600")
win.config(bg='lightblue')

def key_press(event):
    print("key pressed", event.char, event.keysym, event.keycode)
def uppress(event):
    print("up arrow pressed")
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