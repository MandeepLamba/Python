import mysql.connector
from tkinter import *

# create database
conn = mysql.connector.connect(host = "localhost",user='root',database='py')

# create cursor
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS TBL_STOCK (Product_ID VARCHAR(6), Product_Name VARCHAR(20) Unique, Quauntity_On_Hand int, Product_Unit_Price int, ReOrder_Level int, Primary Key (Product_ID))')
cursor.execute('CREATE TABLE IF NOT EXISTS TBL_SALES (Sales_ID VARCHAR(6), Sales_Date DATE, Product_ID VARCHAR(6), Quantity_Sold int, Sales_Price_Per_Unit int, FOREIGN KEY(Product_ID) REFERENCES TBL_STOCK(Product_ID))')

conn.commit()
conn.close()

# Functions


def display_all():
    conn = mysql.connector.connect(host = "localhost",user='root',database='py')
    c = conn.cursor()
    c.execute('SELECT * FROM TBL_STOCK')
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    Label(root, text=print_records).grid(row=6, column=0, columnspan=2)
    conn.commit()
    conn.close()


def insert():
    conn = mysql.connector.connect(host = "localhost",user='root',database='py')
    c = conn.cursor()
    c.execute('INSERT INTO TBL_STOCK VALUES(%s,%s,%s,%s,%s)',params=(Product_ID_TF.get(),Product_Name_TF.get(),QTY_On_Hand_TF.get(),Product_Unit_Price_TF.get(),ReOrder_Level_TF.get()))
    # Erase all the previous data
    Product_ID_TF.delete(0, END)
    Product_Name_TF.delete(0, END)
    QTY_On_Hand_TF.delete(0, END)
    Product_Unit_Price_TF.delete(0, END)
    ReOrder_Level_TF.delete(0, END)
    conn.commit()
    conn.close()


root = Tk()
root.title("My Window")
root.geometry("600x300")
root.config(bg='#f6f7aa')

Product_ID_LBL = Label(root, text='Product ID')
Product_Name_LBL = Label(root, text='Product Name')
QTY_On_Hand_LBL = Label(root, text='Quantity on Hand')
Product_Unit_Price_LBL = Label(root, text='Product Unit Price')
ReOrder_Level_LBL = Label(root, text='ReOrder Level')

Product_ID_LBL.grid(row=0, column=0)
Product_Name_LBL.grid(row=1, column=0)
QTY_On_Hand_LBL.grid(row=2, column=0)
Product_Unit_Price_LBL.grid(row=3, column=0)
ReOrder_Level_LBL.grid(row=4, column=0)


# Entry Fields for stock

Product_ID_TF = Entry(root)
Product_Name_TF = Entry(root)
QTY_On_Hand_TF = Entry(root)
Product_Unit_Price_TF = Entry(root)
ReOrder_Level_TF = Entry(root)

Product_ID_TF.grid(row=0, column=1)
Product_Name_TF.grid(row=1, column=1)
QTY_On_Hand_TF.grid(row=2, column=1)
Product_Unit_Price_TF.grid(row=3, column=1)
ReOrder_Level_TF.grid(row=4, column=1)


# Buttons
view_all_btn = Button(root, text='View all', command=display_all)
insert_btn = Button(root, text='Insert Record', command=insert)
delete_btn = Button(root, text='Delete Record')
cal_profit_btn = Button(root, text='Calculate Profit')

view_all_btn.grid(row=5, column=0)
insert_btn.grid(row=5, column=1)
delete_btn.grid(row=5, column=2)
cal_profit_btn.grid(row=5, column=3)

# infinite loops starts here
root.mainloop()