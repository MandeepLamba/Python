from tkinter import BooleanVar, Button, Checkbutton, Entry, Label, OptionMenu, Radiobutton, StringVar, Tk, messagebox
import mysql.connector
win = Tk()
win.title("My Window")
win.geometry("500x500")
win.config(bg='#6667aa')

fname = StringVar()
email = StringVar()
gender = StringVar()
country = StringVar()
java = BooleanVar()
python = BooleanVar()

def database():
    try:
        conn = mysql.connector.connect(host = "localhost",user='root',database='python')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student (name TEXT(15),email VARCHAR(20),gender TEXT(1),country TEXT(10),java BOOLEAN, python BOOLEAN)')
        cursor.execute('INSERT INTO Student VALUES(%s,%s,%s,%s,%s,%s)',params=(fname.get(),email.get(),gender.get(),country.get(),java.get(),python.get()))
        print(cursor.rowcount,'rows effected.')
        messagebox.showinfo(title='Info',message= str(cursor.rowcount) + ' rows effected.')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        messagebox.showinfo(title='Info',message=e)
def view():
    try:
        conn = mysql.connector.connect(host = "localhost",user='root',database='python')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Student')
        for (name,email,gender,country,java,python) in cursor:
            print('Name:', name, 'Email:',email,'Gender:',gender,'Country:',country,'Java: ',java,'Python:',python, end='\n\n')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

Label(win, text="Registration form", width=20, font=("bold", 20)).place(x=70, y=53)
Label(win, text="FullName", width=20, font=("bold", 10)).place(x=70, y=130)
Entry(win, textvar=fname).place(x=240, y=130)
Label(win, text="Email", width=20, font=("bold", 10)).place(x=70, y=180)
Entry(win, textvar=email).place(x=240, y=180)
Label(win, text="Gender", width=20, font=("bold", 10)).place(x=70, y=230)
Radiobutton(win, text="Male", padx=5, variable=gender, value='M').place(x=240, y=230)
Radiobutton(win, text="Female", padx=20, variable=gender, value='F').place(x=310, y=230)
Label(win, text="country", width=20, font=("bold", 10)).place(x=70, y=280)
list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa']
droplist = OptionMenu(win, country, *list1)
droplist.config(width=15)
country.set('select your country')
droplist.place(x=240, y=280)
Label(win, text="Programming", width=20, font=("bold", 10)).place(x=70, y=330)
Checkbutton(win, text="java", variable=java).place(x=240, y=330)
Checkbutton(win, text="python", variable=python).place(x=310, y=330)
Button(win, text='Submit', width=15, bg='brown', fg='white',command=database).place(x=70, y=380)
Button(win, text='View All', width=15, bg='brown', fg='white',command=view).place(x=230, y=380)
win.mainloop()