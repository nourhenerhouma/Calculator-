#create a calculator
import tkinter as tk
# create function to press the buttom
def button_press(num):
   global equation_vide
   equation_vide=equation_vide+str(num)
   equation_txt.set(equation_vide)
def equals():
    global equation_vide
    total=str(eval(equation_vide))
    equation_txt.set(total)
    equation_vide=total
def clear():
    pass
window=tk.Tk()
window.title('calculator program')
window.geometry("500x400")
equation_vide=""
equation_txt=tk.StringVar()
label=tk.Label(window,textvariable = equation_txt, font=('consolas',20),bg='white', width=48, height=2)
label.pack()
frame= tk.Frame(window)
frame.pack()
button1=tk.Button(frame,text='1',font=('consolas',35),width=9,height=1,command=lambda:button_press(1))
button1.grid(row=0,column=0)
button2=tk.Button(frame,text='2',font=('consolas',35),width=9,height=1,command=lambda:button_press(2))
button2.grid(row=0,column=1)
button3=tk.Button(frame,text='3',font=('consolas',35),width=9,height=1,command=lambda:button_press(3))
button3.grid(row=0,column=2)
button4=tk.Button(frame,text='4',font=('consolas',35),width=9,height=1,command=lambda:button_press(4))
button4.grid(row=1,column=0)
button5=tk.Button(frame,text='5',font=('consolas',35),width=9,height=1,command=lambda:button_press(5))
button5.grid(row=1,column=1)
button6=tk.Button(frame,text='6',font=('consolas',35),width=9,height=1,command=lambda:button_press(6))
button6.grid(row=1,column=2)
button7=tk.Button(frame,text='7',font=('consolas',35),width=9,height=1,command=lambda:button_press(7))
button7.grid(row=2,column=0)
button8=tk.Button(frame,text='8',font=('consolas',35),width=9,height=1,command=lambda:button_press(8))
button8.grid(row=2,column=1)
button9=tk.Button(frame,text='9',font=('consolas',35),width=9,height=1,command=lambda:button_press(9))
button9.grid(row=2,column=2)
plus=tk.Button(frame,text='+',font=('consolas',35), width=9,height=1,command=lambda: button_press('+'))
plus.grid(row=0,column=3)
multiply=tk.Button(frame, text= '*', font=('consolas',35), width=9,height=1,command=lambda: button_press('*'))
multiply.grid(row=1,column=3)
minus=tk.Button(frame, text= '-', font=('consolas',35), width=9,height=1,command=lambda: button_press('-'))
minus.grid(row=3,column=2)
devisor=tk.Button(frame,text='/',font=('consolas',35),width=9,height=1,command=lambda:button_press('/'))
devisor.grid(row=3,column=3)
decimal=tk.Button(frame, text='.',font=('consolas',35),width=9,height=1,command=lambda:button_press('.'))
decimal.grid(row=3,column=1)
equal=tk.Button(frame,text='=', font=('consolas',35),width=9, height=1, command=equals)
equal.grid(row=2,column=3)
button0=tk.Button(frame,text='0', font=('consolas',35), width=9, height=1, command=lambda:button_press('0'))
button0.grid(row=3,column=0)
clear=tk.Button(window,text='clear',font=('consolas',35),width=9,height=1,command=clear)
clear.pack()
window.mainloop()