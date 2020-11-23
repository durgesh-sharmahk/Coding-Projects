from tkinter import*

top = Tk()
top.title("Simple Calculator")

e = Entry(top,bd=5,width=50)
e.grid(row=0,column=0,columnspan=3)

def button_click(number):
    curr = e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(number))
    return

def button_clear():
    e.delete(0,END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num=int(first_number)
    e.delete(0,END)
    return

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_number))
    if math=="Subtract":
        e.insert(0,f_num-int(second_number))
    if math=="Multiply":
        e.insert(0,f_num*int(second_number))
    if math=="Divide":
        e.insert(0,f_num/int(second_number)) 

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "Subtract"
    f_num=int(first_number)
    e.delete(0,END)
    return

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "Multiply"
    f_num=int(first_number)
    e.delete(0,END)
    return

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "Divide"
    f_num=int(first_number)
    e.delete(0,END)
    return

button_1 = Button(top,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(top,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(top,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(top,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(top,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(top,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(top,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(top,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(top,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(top,text="0",padx=40,pady=20,command=lambda: button_click(0))

button_add = Button(top,text="+",padx=39,pady=20,command=button_add)
button_equal = Button(top,text="=",padx=91,pady=20,command=button_equal)
button_clear = Button(top,text="Clear",padx=82,pady=20,command=button_clear)

button_subtract = Button(top,text="-",padx=41,pady=20,command=button_sub)
button_multiply = Button(top,text="*",padx=41,pady=20,command=button_mul)
button_divide = Button(top,text="/",padx=41,pady=20,command=button_div)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

top.mainloop()
