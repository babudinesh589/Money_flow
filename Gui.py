from tkinter import *

def home():
        global exp
        a = Tk()
        a.title("Money Flow")
        a.wm_minsize(height=223, width=397)
        a.wm_maxsize(height=223, width=397)
        a.attributes('-alpha',0.9)
        bg = PhotoImage(file = "Home.png")
        lab = Label(a, image = bg).pack()
        exp = Button(a, text = "Expenses", command = exp)
        exp.place(x=100, y=130)
        a.mainloop()

def exp():
        global b
        b = Tk()
        b.title("Expenses")
        b.wm_minsize(height=223, width=220)
        b.wm_maxsize(height=223, width=220)
        b.configure(bg='burlywood2')
        b.attributes('-alpha',0.9)
        Per_exp = Button(b, text="Personal", height = 2, width = 20, command=exp_inp).pack(pady=10)
   
        Hom_exp = Button(b, text="Home", height = 2, width = 20, command=put).pack(pady=10)
 
        Cook_exp = Button(b, text="Cooking", height = 2, width = 20, command=put).pack(pady=10)
  
        b.mainloop()

def exp_inp():
        options = [
                "Dineshkumar",
                "Vimalarani",
                "Chandran"
        ]
        # datatype of menu text
        
  
        # initial menu text
              
        b.destroy()
        c = Tk()
        c.title("Personal")
        c.wm_minsize(height=223, width=220)
        c.wm_maxsize(height=223, width=220)
        clicked = StringVar()
        clicked.set("ksadchvjlh")
        drop = OptionMenu(c, clicked, *options)
        drop.pack()
        button = Button( c , text = "click Me" , command = show).pack()
        c.configure(bg='burlywood2')
        c.attributes('-alpha',0.9)
        c.mainloop()

def show():
        print("I am inside show: ")

def put():
        print("Me mine")

home()