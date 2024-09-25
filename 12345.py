# for loops
'''
for i in range (0,10):
    print (i)
    for j in range (0,5):
        print(j,"JJJJ")
'''

import tkinter as tk
from tkinter import*

root = tk.Tk()
root.title("calc")

calc_box=Entry(root)
calc_box.grid(row=0, column=1)
#create 3 buttons
button1 = tk.Button(root,text="7")
button2 = tk.Button(root,text="8")
button3 = tk.Button(root,text="9")
button4 = tk.Button(root,text="6")
button5 = tk.Button(root,text="5")
button6 = tk.Button(root,text="4")
button7 = tk.Button(root,text="3")
button8 = tk.Button(root,text="2")
button9 = tk.Button(root,text="1")
button0 = tk.Button(root,text="0")
buttonD = tk.Button(root,text="/")
buttonM = tk.Button(root,text="x")
buttonS = tk.Button(root,text="-")
buttonA = tk.Button(root,text="+")
buttonP = tk.Button(root,text=".")
buttonE = tk.Button(root,text="Enter")
buttonC = tk.Button(root,text="Clear")
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





