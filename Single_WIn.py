from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox

# Expense Entries passed here 
def consol(clicked_name, clicked_cat,  text_amt, text_des):
    created_at = datetime.now()
    name = (clicked_name.get())
    category = (clicked_cat.get())
    Remark = text_des.get()
    Amount = text_amt.get()
    try:
        x = int(Amount)
    except ValueError:
        g = "Entered valid Number"
        messagebox.showinfo(g, "Type Error")

    amt.delete(0, END)
    desc.delete(0, END)
    
    try:
        sql = "INSERT INTO Home_mon (created_at, name, category, Amount, Remark) VALUES (%s, %s, %s, %s, %s)"
        val = (created_at, name, category, Amount, Remark)
        connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
        cursor = connection.cursor()
        cursor.execute("USE My_Home;")
        cursor.execute(sql, val)
        connection.commit()
        nm = cursor.rowcount
        messagebox.showinfo(nm ," Record is updated")
    except:
        sql = "INSERT INTO Home_mon (created_at, name, category, Amount, Remark) VALUES (%s, %s, %s, %s, %s)"
        val = (created_at, name, category, Amount, Remark)
        connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE My_Home;")
        cursor.execute("USE My_Home;")
        cursor.execute("CREATE TABLE Home_mon (S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), category VARCHAR(255), Amount INT, Remark VARCHAR(255));")
        cursor.execute("USE My_Home;")
        cursor.execute(sql, val)
        connection.commit()
        nm = cursor.rowcount        
        messagebox.showinfo(nm ," Record is updated")
    
# from deposit all values are processs here
def sta(options_nm, options_ct,  text_amt, text_rem):
    created_at = datetime.now()
    name = (options_nm.get())
    Source = (options_ct.get())
    Amount = (text_amt.get())
    Remark = text_rem.get()
    try:
        y = int(Amount)
    except ValueError:
        l = "Entered valid Number"
        messagebox.showinfo(l, "Type Error")
    
    d.destroy()

    try:
        sql = "INSERT INTO home_depo(created_at, name, Source, Amount, Remark) VALUES (%s, %s, %s, %s, %s)"
        val = (created_at, name, Source, Amount, Remark)
        connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES;")
        list = cursor.fetchall()
        if ('my_home',) in list:
            cursor.execute("USE My_Home;")
            cursor.execute("show tables;")
            li = cursor.fetchall()
            if ('home_depo',) in li:
                cursor.execute(sql, val)
                connection.commit()
                nm = cursor.rowcount
                messagebox.showinfo(nm ," Record is updated in Deposit")
            else:
                cursor.execute("CREATE TABLE home_depo(S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), Source VARCHAR(255), Amount INT, Remark VARCHAR(255));")
                cursor.execute(sql, val)
                connection.commit()
                nm = cursor.rowcount
                messagebox.showinfo(nm ," Record is updated in Deposit")
            
        else:
            cursor.execute("create database my_home;")
            cursor.execute("USE my_home;")
            cursor.execute("CREATE TABLE home_depo(S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), Source VARCHAR(255), Amount INT, Remark VARCHAR(255));")
            cursor.execute(sql, val)
            connection.commit()
            nm = cursor.rowcount
            messagebox.showinfo(nm ," Record is updated in Deposit")
    except:
        print("I am inside the exept inside sta")

        

# for deposit starts here to passing values
def depo():
    global d
    d = Tk()
    d.title("Deposit")
    d.geometry("250x200")
    d.configure(bg='#49A')
    d.attributes('-alpha',0.9)

    dep_nm_lab = Label(d, text="Name")
    dep_nm_lab.grid(column=0, row=0, sticky=W+E, padx=5, pady=5)
    dep_nm_lab.configure(bg='#49A')

    options_nm = StringVar(d)
    options_nm.set("Select") 

    om1 =OptionMenu(d, options_nm, "Dineshkumar","Vimalarani", "Chandran")
    om1.grid(column=1, row=0, sticky=EW, padx=5, pady=5)
    
    dep_sr_lab = Label(d, text="Source")
    dep_sr_lab.grid(column=0, row=1, sticky=EW, padx=5, pady=5)
    dep_sr_lab.configure(bg='#49A')

    options_ct = StringVar(d)
    options_ct.set("Select") 

    om1 =OptionMenu(d, options_ct, "Salary","Debit", "Others")
    om1.grid(column=1, row=1, sticky=EW, padx=5, pady=5)
    
    lab_amt = Label(d, text = "Amount")
    lab_amt.grid(column=0, row=2, sticky=EW, padx=5, pady=5)
    lab_amt.configure(bg='#49A')

    text_amt = StringVar(d)
    amt_hm = Entry(d, textvariable = text_amt)
    amt_hm.grid(column=1, row=2, sticky=EW, padx=5, pady=5)

    lab_rem = Label(d, text ="Description")
    lab_rem.grid(column=0, row=3, sticky=EW, padx=5, pady=5)
    lab_rem.configure(bg='#49A')

    text_rem = StringVar(d)
    rem_hm = Entry(d, textvariable = text_rem)
    rem_hm.grid(column=1, row=3, sticky=EW, padx=5, pady=5)

    Sub1 = Button(d, text = "Submit" , command = lambda: sta(options_nm, options_ct,  text_amt, text_rem))
    Sub1.grid(column=0, row=4, sticky=W+E, padx=5, pady=5)

    cls3 = Button(d, text = "Close" ,  command = d.destroy)
    cls3.grid(column=1, row=4, sticky=W+E, padx=5, pady=5)
    d.mainloop()

# This is for the statement from income transaction
def show_state_inc():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
        cursor = connection.cursor()
        cursor.execute("show databases;")
        out_tab = cursor.fetchall()
        if ('my_home',) in out_tab:
            cursor.execute("use my_home;")
            cursor.execute("show tables;")
            tb = cursor.fetchall()
            if ('home_depo',) in tb:
                win = Tk()
                win.title("Statement")
                cursor.execute("Select * from home_depo;")
                mn = cursor.fetchall()
                e = Label(win, width=20, text='S.No', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=0)
                e = Label(win, width=20, text='Date & Time', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=1)
                e = Label(win, width=20, text='Name', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=2)
                e = Label(win, width=20, text='Source', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=3)
                e = Label(win, width=20, text='Amount', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=4)
                e = Label(win, width=20, text='Remark', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=5)
 
                i=1
                for home_depo in mn: 
                    for j in range(len(home_depo)):
                        e = Label(win, width=20, text=home_depo[j], borderwidth=2,relief='ridge', anchor="w") 
                        e.grid(row=i, column=j)     
                    i=i+1
                win.mainloop()
                    
            else:
                cursor.execute("use my_home;")
                cursor.execute("CREATE TABLE home_depo(S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), Source VARCHAR(255), Amount INT, Remark VARCHAR(255));")
                cursor.execute("Select * from home_depo;")
                mn = cursor.fetchall()
                win = Tk()
                win.title("Statement")
                e = Label(win, width=20, text='S.No', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=0)
                e = Label(win, width=20, text='Date & Time', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=1)
                e = Label(win, width=20, text='Name', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=2)
                e = Label(win, width=20, text='Source', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=3)
                e = Label(win, width=20, text='Amount', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=4)
                e = Label(win, width=20, text='Remark', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=5)
 
                i=1
                for home_depo in mn: 
                    for j in range(len(home_depo)):
                        e = Label(win, width=20, text=home_depo[j], borderwidth=2,relief='ridge', anchor="w") 
                        e.grid(row=i, column=j)     
                    i=i+1

                win.mainloop()

        else:
            connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE my_home;")
            cursor.execute("USE my_home;")
            cursor.execute("CREATE TABLE Home_depo(S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), Source VARCHAR(255), Amount INT, Remark VARCHAR(255));")
            cursor.execute("Select * from home_depo;")
            mn = cursor.fetchall()
            win = Tk()
            win.title("Statement")
            e = Label(win, width=20, text='S.No', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=0)
            e = Label(win, width=20, text='Date & Time', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=1)
            e = Label(win, width=20, text='Name', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=2)
            e = Label(win, width=20, text='Source', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=3)
            e = Label(win, width=20, text='Amount', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=4)
            e = Label(win, width=20, text='Remark', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=5)
 
            i=1
            for home_depo in mn:
                for j in range(len(home_depo)):
                    e = Label(win, width=20, text=home_depo[j], borderwidth=2,relief='ridge', anchor="w") 
                    e.grid(row=i, column=j)
                i=i+1
            win.mainloop()

    except:
        a = "Table info"
        messagebox.showinfo(a, "Empty Table in deposit")

# This is for the statement from expense transaction
def show_state():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
        cursor = connection.cursor()
        cursor.execute("show databases;")
        out_tab = cursor.fetchall()
        if ('my_home',) in out_tab:
            cursor.execute("use my_home;")
            cursor.execute("show tables;")
            tb = cursor.fetchall()
            if ('home_mon',) in tb:
                cursor.execute("Select * from home_mon;")
                pp = cursor.fetchall()
                win = Tk()
                win.title("Statement")
                e = Label(win, width=20, text='S.No', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=0)
                e = Label(win, width=20, text='Date & Time', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=1)
                e = Label(win, width=20, text='Name', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=2)
                e = Label(win, width=20, text='Category', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=3)
                e = Label(win, width=20, text='Amount', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=4)
                e = Label(win, width=20, text='Remark', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=5)
 
                i=1
                for home_mon in pp: 
                    for j in range(len(home_mon)):
                        e = Label(win, width=20, text=home_mon[j], borderwidth=2,relief='ridge', anchor="w") 
                        e.grid(row=i, column=j)     
                    i=i+1
                win.mainloop()
                    
            else:
                cursor.execute("use my_home;")
                cursor.execute("CREATE TABLE home_mon(S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), category VARCHAR(255), Amount INT, Remark VARCHAR(255));")
                cursor.execute("Select * from home_mon;")
                pp = cursor.fetchall()
                win = Tk()
                win.title("Statement")
                e = Label(win, width=20, text='S.No', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=0)
                e = Label(win, width=20, text='Date & Time', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=1)
                e = Label(win, width=20, text='Name', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=2)
                e = Label(win, width=20, text='Category', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=3)
                e = Label(win, width=20, text='Amount', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=4)
                e = Label(win, width=20, text='Remark', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
                e.grid(row=0,column=5)
 
                i=1
                for home_mon in pp: 
                    for j in range(len(home_mon)):
                        e = Label(win, width=20, text=home_mon[j], borderwidth=2,relief='ridge', anchor="w") 
                        e.grid(row=i, column=j)     
                    i=i+1

                win.mainloop()

        else:
            connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE my_home;")
            cursor.execute("USE my_home;")
            cursor.execute("CREATE TABLE home_mon(S_No INT AUTO_INCREMENT PRIMARY KEY, created_at DATETIME, name VARCHAR(255), category VARCHAR(255), Amount INT, Remark VARCHAR(255));")
            cursor.execute("Select * from home_mon;")
            pp = cursor.fetchall()
            win = Tk()
            win.title("Statement")
            e = Label(win, width=20, text='S.No', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=0)
            e = Label(win, width=20, text='Date & Time', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=1)
            e = Label(win, width=20, text='Name', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=2)
            e = Label(win, width=20, text='Category', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=3)
            e = Label(win, width=20, text='Amount', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=4)
            e = Label(win, width=20, text='Remark', borderwidth=2, relief='ridge',anchor='w', bg='lightgray')
            e.grid(row=0,column=5)
 
            i=1
            for home_mon in pp:
                for j in range(len(home_mon)):
                    e = Label(win, width=20, text=home_mon[j], borderwidth=2,relief='ridge', anchor="w") 
                    e.grid(row=i, column=j)
                i=i+1
            win.mainloop()

    except:
        a = "No recored found"
        messagebox.showinfo(a, "Empty Table in Expense")


# Here Balance Checking process happens        
def bala():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Tamil')
        cursor = connection.cursor()
        cursor.execute("USE my_home;")
        cursor.execute("select sum(Amount) from home_mon;")
        a = cursor.fetchone()
        for rec in a:
            print(rec)
        cursor.execute("select sum(Amount) from home_depo;")
        b = cursor.fetchone()
        for record in b:
            print(record)
        print(rec, "The a value", record, "The b value")
        c = record-rec
        bal = Tk()
        bal.title("Balance Amount")
        bal.geometry("400x200")
        bal.configure(bg='gray16')

        q = "\u20B9", c

        bb = Label(bal, text=q, font=("Arial", 20), bg='gray16', fg='white').pack(padx=5, pady=30)
        ext = Button(bal, text='Close', font=("Arial", 10), width=10, command=bal.destroy).pack(padx=5, pady=20)

        bal.mainloop()
    except:
        ba = Tk()
        ba.title("Balance Amount")
        ba.geometry("400x200")
        ba.configure(bg='gray16')

        p = "Sorry!  No Transaction"

        b = Label(ba, text=p, font=("Arial", 16), bg='gray16', fg='white').pack(padx=5, pady=30)
        ex = Button(ba, text='Close', font=("Arial", 10), width=10, command=ba.destroy).pack(padx=5, pady=20)
    
        ba.mainloop()


# Everything Starts from here
root = Tk() 
root.title("Home Money Management")
root.geometry("510x260")
root.attributes('-alpha',0.9)
root.configure(bg='#49A')
lb = Label(text="Welome to our Home", font=("Arial", 20), bg='#49A')
lb.grid(column=1, row=0, columnspan=2)
lb.anchor('center')

Nm_lab = Label(root, text='Name')
Nm_lab.grid(column=0, row=2, padx=5, pady=5)
Nm_lab.configure(bg='#49A')

Ct_lab = Label(root, text='Category')
Ct_lab.grid(column=1, row=2, padx=5, pady=5)
Ct_lab.configure(bg='#49A')


clicked_name = StringVar()

options = [
    "Dineshkumar",
     "Vimalarani",
      "Chandran"
    ]    
clicked_name.set("Select")
drop = OptionMenu(root , clicked_name, *options)
drop.grid(column=0, row=3, padx=5, pady=5)
drop.configure(bg='darkgrey')
print("Below is from drop")
print (clicked_name.get())


clicked_cat = StringVar()

options = [
    "Food",
     "Home",
      "Personal"
    ]    
clicked_cat.set("Select")
drop1 = OptionMenu(root , clicked_cat, *options)
drop1.grid(column=1, row=3, padx=5, pady=5)
drop1.configure(bg='darkgrey')
print("Below is from drop")
print (clicked_cat.get())

bal = Button(root, text="Balance", command= bala)
bal.grid(column=3, row=3, padx=5, pady=5)
bal.configure(bg='darkgrey')

dep = Button(root, text='Deposit', command = depo)
dep.grid(column=3, row=5, padx=5, pady=5)
dep.configure(bg='darkgrey')

amt_lab = Label(root, text='Amount')
amt_lab.grid(column=0, row=5, padx=5, pady=5)
amt_lab.configure(bg='#49A')

desc_lab = Label(root, text='Description')
desc_lab.grid(column=1, row=5, padx=5, pady=5)
desc_lab.configure(bg='#49A')

text_amt = StringVar()
amt = Entry(root, textvariable=text_amt, width=7)
amt.grid(column=0, row=6, padx=5, pady=5,)
amt.configure(bg='lightgrey')

text_des = StringVar()
desc = Entry(root, textvariable=text_des)
desc.grid(column=1, row=6, sticky=W+E, padx=5, pady=5)
desc.configure(bg='lightgrey')

state = Button(root, text="Expense Statement", command=show_state)
state.grid(column=3, row=6, padx=5, pady=5)
state.configure(bg='darkgrey')

state_inc = Button(root, text="Income Statement", command=show_state_inc)
state_inc.grid(column=3, row=7, padx=5, pady=5)
state_inc.configure(bg='darkgrey')

sub = Button(root, text='Submit', command = lambda: consol(clicked_name, clicked_cat,  text_amt, text_des))
sub.grid(column=0, row=8, columnspan=2, sticky=W+E, padx=5, pady=10)
sub.configure(bg='darkgrey')

cls = Button(root, text='Close', command = root.destroy)
cls.grid(column=2, row=8, columnspan=2, sticky=W+E, padx=5, pady=10)
cls.configure(bg='darkgrey')
 
root.mainloop()