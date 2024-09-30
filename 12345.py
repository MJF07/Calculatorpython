# for loops
'''
for i in range (0,10):
    print (i)
    for j in range (0,5):
        print(j,"JJJJ")
'''

import tkinter as tk #importing tkinter as tk so you don't have to list "tkinter" every single time you enter it
from tkinter import*

#this is globally declared expression
expression=""

def press(num):
    #grab global value of expression
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equal_press():
    global expression
    print(expression)
    total=str(eval(expression))
    print(total)
    equation.set(total)
    expression=""
    print(expression)

def clear():
    global expression
    expression=""
    equation.set("")

def backspace():
    global expression
    print(expression)
    equation.set(expression)
    expression=expression[:-1] #this says to show the entire string but subtract one character. each character has different numeric values.
    print(expression)
    equation.set(expression)

#this is the beginning of TK inter window definitions
root = tk.Tk()

#setting size and name of window
root.title("calc")
root.geometry("260x250")

#setting some variables
equation= StringVar()
#entry box that shows text
calc_box=Entry(root,textvariable=equation)
calc_box.grid(columnspan=4, ipadx=70)
calc_box.grid(row=0, column=0,)

#create buttons
button7 = tk.Button(root,text="7",fg='black' , bg='yellow' , command=lambda: press(7) ,height=2, width=8)
button8 = tk.Button(root,text="8",fg='black' , bg='yellow' , command=lambda: press(8),height=2, width=8)
button9 = tk.Button(root,text="9",fg='black' , bg='yellow' , command=lambda: press(9) ,height=2, width=8)
button6 = tk.Button(root,text="6",fg='black' , bg='yellow' , command=lambda: press(6) ,height=2, width=8)
button5 = tk.Button(root,text="5",fg='black' , bg='yellow' , command=lambda: press(5) ,height=2, width=8)
button4 = tk.Button(root,text="4",fg='black' , bg='yellow' , command=lambda: press(4) ,height=2, width=8)
button3 = tk.Button(root,text="3",fg='black' , bg='yellow' , command=lambda: press(3) ,height=2, width=8)
button2 = tk.Button(root,text="2",fg='black' , bg='yellow' , command=lambda: press(2) ,height=2, width=8)
button1 = tk.Button(root,text="1",fg='black' , bg='yellow' , command=lambda: press(1) ,height=2, width=8)
button0 = tk.Button(root,text="0",fg='black' , bg='yellow' , command=lambda: press(0) ,height=2, width=8)
buttonD = tk.Button(root,text="/",fg='black' , bg='yellow' , command=lambda: press("/"),height=2, width=8)
buttonM = tk.Button(root,text="x",fg='black' , bg='yellow' , command=lambda: press("*"),height=2, width=8)
buttonS = tk.Button(root,text="-",fg='black' , bg='yellow' , command=lambda: press("-"),height=2, width=8)
buttonA = tk.Button(root,text="+",fg='black' , bg='yellow' , command=lambda: press("+"),height=2, width=8)
buttonP = tk.Button(root,text=".",fg='black' , bg='yellow' , command=lambda: press("."),height=2, width=8)
buttonE = tk.Button(root,text="Enter",command=equal_press,fg="black", bg='light green',height=2, width=8)
buttonC = tk.Button(root,text="Clear",command=clear, fg='black' , bg='light blue',height=2, width=8)
buttonBS = tk.Button(root,text="del", command=backspace,fg='black', bg='orange',height=2, width=8)


#place buttons vertically
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
buttonM.grid(row=2,column=3)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonS.grid(row=3,column=3)
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)
buttonA.grid(row=4,column=3)
button0.grid(row=5,column=0)
buttonP.grid(row=5,column=1)
buttonE.grid(row=5,column=3)
buttonC.grid(row=1,column=1)
buttonD.grid(row=1,column=3)
buttonBS.grid(row=1,column=0)


root.mainloop()





