# for loops
'''
for i in range (0,10):
    print (i)
    for j in range (0,5):
        print(j,"JJJJ")
'''

import tkinter as tk
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
    total=str(eval(expression))
    equation.set(total)
    expression=""

def clear():
    global expression
    expression=""
    equation.set("")


#this is the beginning of TK inter window definitions
root = tk.Tk()

#setting size and name of window
root.title("calc")
root.geometry("250x250")

#setting some variables
equation= StringVar()
#entry box that shows text
calc_box=Entry(root,textvariable=equation)
calc_box.grid(row=0, column=1)



#create buttons
button7 = tk.Button(root,text="7",fg='black' , bg='yellow' , command=lambda: press(7) )
button8 = tk.Button(root,text="8",fg='black' , bg='yellow' , command=lambda: press(8) )
button9 = tk.Button(root,text="9",fg='black' , bg='yellow' , command=lambda: press(9) )
button6 = tk.Button(root,text="6",fg='black' , bg='yellow' , command=lambda: press(6) )
button5 = tk.Button(root,text="5",fg='black' , bg='yellow' , command=lambda: press(5) )
button4 = tk.Button(root,text="4",fg='black' , bg='yellow' , command=lambda: press(4) )
button3 = tk.Button(root,text="3",fg='black' , bg='yellow' , command=lambda: press(3) )
button2 = tk.Button(root,text="2",fg='black' , bg='yellow' , command=lambda: press(2) )
button1 = tk.Button(root,text="1",fg='black' , bg='yellow' , command=lambda: press(1) )
button0 = tk.Button(root,text="0",fg='black' , bg='yellow' , command=lambda: press(0) )
buttonD = tk.Button(root,text="/",fg='black' , bg='yellow' , command=lambda: press("/"))
buttonM = tk.Button(root,text="x",fg='black' , bg='yellow' , command=lambda: press("*"))
buttonS = tk.Button(root,text="-",fg='black' , bg='yellow' , command=lambda: press("-"))
buttonA = tk.Button(root,text="+",fg='black' , bg='yellow' , command=lambda: press("+"))
buttonP = tk.Button(root,text=".",fg='black' , bg='yellow' , command=lambda: press("."))
buttonE = tk.Button(root,text="Enter",command=equal_press,fg="black", bg='green')
buttonC = tk.Button(root,text="Clear",command=clear, fg='black' , bg='blue')
buttonB = tk.Button(root,text="<-")


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
buttonB.grid(row=1,column=0)


root.mainloop()





