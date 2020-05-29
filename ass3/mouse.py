from tkinter import Button, Frame, Tk

win = Tk()
win.geometry("400x500")
win.title("My Window")
Frame(win,cursor='heart',height=100,width=100,bg='#9999aa').grid(row=0,column=0)
Frame(win,cursor='spider',height=100,width=100,bg='#bb9999').grid(row=0,column=1)
Frame(win,cursor='plus',height=100,width=100,bg='#99cc99').grid(row=0,column=2)

Button(win,cursor='cross',height=5,width=10,bg='#39cc99',text='Button 1').grid(row=1,column=0)
Button(win,cursor='star',height=5,width=10,bg='#c95c39',text='Button 2').grid(row=1,column=2)

win.mainloop()