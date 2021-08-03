from tkinter import *


def Reg():
    global roots

    roots = Tk()

    roots.title('Welcome to Debate')
    Reg_lab = Label(roots, text='Please Selection Your Option\n')
    Reg_lab.grid(row=0, column=0, sticky=E)

    Reg_Button = Button(roots, text='New Debate', command=New_pre)
    Reg_Button.grid(rowspan=1, sticky=W)

    roots.mainloop()

def New_pre():
    roots.destroy()
    New()

def Pre():
    roots = Tk()
    roots.title('Welcome to Debate')
    intruction = Label(roots, text='Please Selection Your Option\n')
    intruction.grid(row=0, column=0, sticky=E)

    Pre_1_Button = Button(rootA, text='Previous Result', command=ret)
    Pre_1_Button.grid(columnspan=2, sticky=W)
    Pre_2_Button = Button(rootA, text='New Debate', command=New_pre)
    Pre_2_Button.grid(columnspan=2, sticky=W)
    rootA.mainloop()

def New():
    global Nme1
    global S_Nme1
    global roots
    global Nme2
    global S_Nme2
    global roots
    global Nme3
    global S_Nme3
    global roots
    global Nme4
    global S_Nme4
    global roots

    roots = Tk()
    roots.resizable(width=FALSE, height=TRUE)
    roots.title('Debater')
    intruction = Label(roots, text='Debaters Detail\n')
    intruction.grid(row=0, column=0, sticky=E)

    Tone = Label(roots, text='First Team')
    Tone.grid(row=1, column=1, sticky=W)

    Nme1L = Label(roots, text='Full Name: ')
    pword1L = Label(roots, text='School Name: ')
    Nme1L.grid(row=2, column=0, sticky=W)
    pword1L.grid(row=3, column=0, sticky=W)
    Nme1 = Entry(roots)
    S_Nme1 = Entry(roots)
    Nme1.grid(row=2, column=1)
    S_Nme1.grid(row=3, column=1)

    Nme2L = Label(roots, text='Full Name: ')
    pword2L = Label(roots, text='School Name: ')
    Nme2L.grid(row=4, column=0, sticky=W)
    pword2L.grid(row=5, column=0, sticky=W)
    Nme2 = Entry(roots)
    S_Nme2 = Entry(roots)
    Nme2.grid(row=4, column=1)
    S_Nme2.grid(row=5, column=1)

    Two = Label(roots, text='Second Team')
    Two.grid(row=1, column=3, sticky=W)

    Nme3L = Label(roots, text='Full Name: ')
    pword3L = Label(roots, text='School Name: ')
    Nme3L.grid(row=2, column=2, sticky=W)
    pword3L.grid(row=3, column=2, sticky=W)
    Nme3 = Entry(roots)
    S_Nme3 = Entry(roots)
    Nme3.grid(row=2, column=3)
    S_Nme3.grid(row=3, column=3)

    Nme4L = Label(roots, text='Full Name: ')
    pword4L = Label(roots, text='School Name: ')
    Nme4L.grid(row=4, column=2, sticky=W)
    pword4L.grid(row=5, column=2, sticky=W)
    Nme4 = Entry(roots)
    S_Nme4 = Entry(roots)
    Nme4.grid(row=4, column=3)
    S_Nme4.grid(row=5, column=3)

    signupButton = Button(roots, text='Next Debater', command=Judges)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()

def Judges():
    global J_Nme_1
    global J_Nme_2
    global J_Nme_3

    roots = Tk()
    roots.title('Judges')
    intruction = Label(roots, text='Judges Name\n')
    intruction.grid(row=0, column=0, sticky=E)

    L_J_Nme1 = Label(roots, text='First Judge')
    L_J_Nme2 = Label(roots, text='Second Judge')
    L_J_Nme3 = Label(roots, text='Third Judge')
    L_J_Nme1.grid(row=1, column=0, sticky=W)
    L_J_Nme2.grid(row=2, column=0, sticky=W)
    L_J_Nme3.grid(row=3, column=0, sticky=W)

    J_Nme_1 = Entry(roots)
    J_Nme_2 = Entry(roots)
    J_Nme_3 = Entry(roots)
    J_Nme_1.grid(row=1, column=1)
    J_Nme_2.grid(row=2, column=1)
    J_Nme_3.grid(row=3, column=1)

    S_Button = Button(roots, text='Debate', command=Round_1)
    S_Button.grid(columnspan=2, sticky=W)
    roots.mainloop()

def Round_1():
    global Res_11_1
    global Res_12_1
    global Res_13_1
    global Res_21_1
    global Res_22_1
    global Res_23_1
    global Res_31_1
    global Res_32_1
    global Res_33_1
    global Res_41_1
    global Res_42_1
    global Res_43_1

    roots = Tk()
    roots.title('Score Board')
    Roun_1 = Label(roots, text='Round-1\n')
    Roun_1.grid(row=0, column=2, sticky=E)

    Team_A_1 = Label(roots, text='Team A\n')
    Team_A_1.grid(row=1, column=1, sticky=E)
    Team_B_1 = Label(roots, text='Team B\n')
    Team_B_1.grid(row=1, column=3, sticky=E)

    Nme_g_1_1 = Label(roots, text=Nme1.get())
    Nme_g_1_1.grid(row=2, column=1, sticky=E)
    Nme_g_2_1 = Label(roots, text=Nme2.get())
    Nme_g_2_1.grid(row=2, column=2, sticky=E)
    Nme_g_3_1 = Label(roots, text=Nme3.get())
    Nme_g_3_1.grid(row=2, column=3, sticky=E)
    Nme_g_4_1 = Label(roots, text=Nme4.get())
    Nme_g_4_1.grid(row=2, column=4, sticky=E)

    J_Nme_1_1 = Label(roots, text=J_Nme_1.get())
    J_Nme_1_1.grid(row=3, column=0, sticky=E)
    J_Nme_2_1 = Label(roots, text=J_Nme_2.get())
    J_Nme_2_1.grid(row=4, column=0, sticky=E)
    J_Nme_3_1 = Label(roots, text=J_Nme_3.get())
    J_Nme_3_1.grid(row=5, column=0, sticky=E)

    Res_11_1 = Entry(roots)
    Res_12_1 = Entry(roots)
    Res_13_1 = Entry(roots)
    Res_21_1 = Entry(roots)
    Res_22_1 = Entry(roots)
    Res_23_1 = Entry(roots)
    Res_31_1 = Entry(roots)
    Res_32_1 = Entry(roots)
    Res_33_1 = Entry(roots)
    Res_41_1 = Entry(roots)
    Res_42_1 = Entry(roots)
    Res_43_1 = Entry(roots)

    Res_11_1.grid(row=3, column=1)
    Res_12_1.grid(row=4, column=1)
    Res_13_1.grid(row=5, column=1)
    Res_21_1.grid(row=3, column=2)
    Res_22_1.grid(row=4, column=2)
    Res_23_1.grid(row=5, column=2)
    Res_31_1.grid(row=3, column=3)
    Res_32_1.grid(row=4, column=3)
    Res_33_1.grid(row=5, column=3)
    Res_41_1.grid(row=3, column=4)
    Res_42_1.grid(row=4, column=4)
    Res_43_1.grid(row=5, column=4)

    S_Button = Button(roots, text='Submit',command=Round_2_pre)
    S_Button.grid(columnspan=6, sticky=W)
    roots.mainloop()

def Round_2_pre():
    with open("Round-1.txt", 'w') as f:
        f.write(Nme1.get())
        f.write('\t:')
        f.write(Res_11_1.get())
        f.write(',')
        f.write(Res_12_1.get())
        f.write(',')
        f.write(Res_13_1.get())
        f.write('.\n')

        f.write(Nme2.get())
        f.write('\t:')
        f.write(Res_21_1.get())
        f.write(',')
        f.write(Res_22_1.get())
        f.write(',')
        f.write(Res_23_1.get())
        f.write('.\n')

        f.write(Nme3.get())
        f.write('\t:')
        f.write(Res_31_1.get())
        f.write(',')
        f.write(Res_32_1.get())
        f.write(',')
        f.write(Res_33_1.get())
        f.write('.\n')

        f.write(Nme4.get())
        f.write('\t:')
        f.write(Res_41_1.get())
        f.write(',')
        f.write(Res_42_1.get())
        f.write(',')
        f.write(Res_43_1.get())
        f.write('.\n')

        f.close()

    Round_2()


def Round_2():
    global Res_11_2
    global Res_12_2
    global Res_13_2
    global Res_21_2
    global Res_22_2
    global Res_23_2
    global Res_31_2
    global Res_32_2
    global Res_33_2
    global Res_41_2
    global Res_42_2
    global Res_43_2

    roots = Tk()
    roots.title('Score Board')
    Roun1 = Label(roots, text='Round-2\n')
    Roun1.grid(row=0, column=2, sticky=E)
    TeamA2 = Label(roots, text='Team A\n')
    TeamA2.grid(row=1, column=1, sticky=E)
    TeamB2 = Label(roots, text='Team B\n')
    TeamB2.grid(row=1, column=3, sticky=E)
    Nmeg12 = Label(roots, text=Nme1.get())
    Nmeg12.grid(row=2, column=1, sticky=E)
    Nmeg22 = Label(roots, text=Nme2.get())
    Nmeg22.grid(row=2, column=2, sticky=E)
    Nmeg32 = Label(roots, text=Nme3.get())
    Nmeg32.grid(row=2, column=3, sticky=E)
    Nmeg42 = Label(roots, text=Nme4.get())
    Nmeg42.grid(row=2, column=4, sticky=E)

    J_Nme_1_2 = Label(roots, text=J_Nme_1.get())
    J_Nme_1_2.grid(row=3, column=0, sticky=E)
    J_Nme_2_2 = Label(roots, text=J_Nme_2.get())
    J_Nme_2_2.grid(row=4, column=0, sticky=E)
    J_Nme_3_2 = Label(roots, text=J_Nme_3.get())
    J_Nme_3_2.grid(row=5, column=0, sticky=E)

    Res_11_2 = Entry(roots)
    Res_12_2 = Entry(roots)
    Res_13_2 = Entry(roots)
    Res_21_2 = Entry(roots)
    Res_22_2 = Entry(roots)
    Res_23_2 = Entry(roots)
    Res_31_2 = Entry(roots)
    Res_32_2 = Entry(roots)
    Res_33_2 = Entry(roots)
    Res_41_2 = Entry(roots)
    Res_42_2 = Entry(roots)
    Res_43_2 = Entry(roots)

    Res_11_2.grid(row=3, column=1)
    Res_12_2.grid(row=4, column=1)
    Res_13_2.grid(row=5, column=1)
    Res_21_2.grid(row=3, column=2)
    Res_22_2.grid(row=4, column=2)
    Res_23_2.grid(row=5, column=2)
    Res_31_2.grid(row=3, column=3)
    Res_32_2.grid(row=4, column=3)
    Res_33_2.grid(row=5, column=3)
    Res_41_2.grid(row=3, column=4)
    Res_42_2.grid(row=4, column=4)
    Res_43_2.grid(row=5, column=4)

    S_Button = Button(roots, text='Submit', command=Save)
    S_Button.grid(columnspan=6, sticky=W)
    roots.mainloop()

def Save():
    with open("Round-2.txt", 'w') as f:
        f.write(Nme1.get())
        f.write('\t:')
        f.write(Res_11_2.get())
        f.write(',')
        f.write(Res_12_2.get())
        f.write(',')
        f.write(Res_13_2.get())
        f.write('.\n')

        f.write(Nme2.get())
        f.write('\t:')
        f.write(Res_21_2.get())
        f.write(',')
        f.write(Res_22_2.get())
        f.write(',')
        f.write(Res_23_2.get())
        f.write('.\n')

        f.write(Nme3.get())
        f.write('\t:')
        f.write(Res_31_2.get())
        f.write(',')
        f.write(Res_32_2.get())
        f.write(',')
        f.write(Res_33_2.get())
        f.write('.\n')

        f.write(Nme4.get())
        f.write('\t:')
        f.write(Res_41_2.get())
        f.write(',')
        f.write(Res_42_2.get())
        f.write(',')
        f.write(Res_43_2.get())
        f.write('.\n')

        f.close()

    global Team_A
    global Team_B
    global Pat_1
    global Pat_2
    global Pat_3
    global Pat_4
    global Pat_11
    global Pat_12
    global Pat_21
    global Pat_22
    global Pat_31
    global Pat_32
    global Pat_41
    global Pat_42

    deb_01 = int(Res_11_1.get())
    deb_02 = int(Res_12_1.get())
    deb_03 = int(Res_13_1.get())
    deb_04 = int(Res_21_1.get())
    deb_05 = int(Res_22_1.get())
    deb_06 = int(Res_23_1.get())
    deb_07 = int(Res_31_1.get())
    deb_08 = int(Res_32_1.get())
    deb_09 = int(Res_33_1.get())
    deb_10 = int(Res_41_1.get())
    deb_11 = int(Res_42_1.get())
    deb_12 = int(Res_43_1.get())
    deb_13 = int(Res_11_2.get())
    deb_14 = int(Res_12_2.get())
    deb_15 = int(Res_13_2.get())
    deb_16 = int(Res_21_2.get())
    deb_17 = int(Res_22_2.get())
    deb_18 = int(Res_23_2.get())
    deb_19 = int(Res_31_2.get())
    deb_20 = int(Res_32_2.get())
    deb_21 = int(Res_33_2.get())
    deb_22 = int(Res_41_2.get())
    deb_23 = int(Res_42_2.get())
    deb_24 = int(Res_43_2.get())

    Team_A = deb_01 + deb_02 + deb_03 + deb_04 + deb_05 + deb_06 + deb_13 + deb_14 + deb_15 + deb_16 + deb_17 + deb_18
    Team_B = deb_07 + deb_08 + deb_09 + deb_10 + deb_11 + deb_12 + deb_19 + deb_20 + deb_21 + deb_22 + deb_23 + deb_24

    Pat_11 = deb_01 + deb_02 + deb_03
    Pat_12 = deb_13 + deb_14 + deb_15

    Pat_1 = Pat_11 + Pat_12

    Pat_21 = deb_04 + deb_05 + deb_06
    Pat_22 = deb_16 + deb_17 + deb_18

    Pat_2 = Pat_21 + Pat_22

    Pat_31 = deb_07 + deb_08 + deb_09
    Pat_32 = deb_19 + deb_20 + deb_21

    Pat_3 = Pat_31 + Pat_32

    Pat_41 = deb_10 + deb_11 + deb_12
    Pat_42 = deb_22 + deb_23 + deb_24

    Pat_4 = Pat_41 + Pat_42

    with open("Final Result.txt", 'w') as f:
        f.write('The Final Result of the Debate Competition')
        f.write('.\n')
        f.write('\n')
        f.write('The Team Score are:')
        f.write('\n')
        f.write('Team A:')
        f.write('\t')
        f.write("%s" % Team_A)
        f.write('\n')
        f.write('Team B:')
        f.write('\t')
        f.write("%s" % Team_B)
        f.write('\n')
        f.write('The Individual Score are:\n')
        f.write(Nme1.get())
        f.write(':')
        f.write("%s" % Pat_1)
        f.write('\n')
        f.write(Nme2.get())
        f.write(':')
        f.write("%s" % Pat_2)
        f.write('\n')
        f.write(Nme3.get())
        f.write(':')
        f.write("%s" % Pat_3)
        f.write('\n')
        f.write(Nme4.get())
        f.write(':')
        f.write("%s" % Pat_4)
        f.write('\n')
        f.close()

    if Team_A > Team_B:
        print('The Winning team is Team A')
        rootA = Tk()  # This now makes a new window.
        rootA.title('Final Result')  # This makes the window title 'login'
        intruction = Label(rootA, text='Team A is The Winner\n')  # More labels to tell us what they do
        intruction.grid(sticky=E)

        rootA.mainloop()

    else :
        print('The Winning team is Team B')
        rootA = Tk()  # This now makes a new window.
        rootA.title('Final Result')  # This makes the window title 'login'
        intruction = Label(rootA, text='Team B is The Winner\n')  # More labels to tell us what they do
        intruction.grid(sticky=E)

        rootA.mainloop()

Reg()