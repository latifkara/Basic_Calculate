from tkinter import *
import math
import tkinter as tk

class calculator:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root, bg='white', highlightbackground = "#F3F3F7", highlightthickness = 5)
        self.result = 0
        self.is_plus = False
        self.is_minus = False
        self.is_multi = False
        self.is_divede = False
        self.is_power = False
        self.is_mod = False

    def plus(self):
        first_number = int(self.entry.get())
        self.result = first_number
        self.is_plus = True
        self.entry.delete(0, END)


    def minus(self):
        first_number = int(self.entry.get())
        self.result = first_number
        self.is_minus = True
        self.entry.delete(0, END)

    def multiply(self):
        first_number = int(self.entry.get())
        self.result = first_number
        self.is_multi = True
        self.entry.delete(0, END)

    def divde_by(self):
        first_number = int(self.entry.get())
        self.result = first_number
        self.is_divede = True
        self.entry.delete(0, END)

    def power(self):
        first_number = int(self.entry.get())
        self.result = first_number
        self.is_power = True
        self.entry.delete(0, END)

    def mod(self):
        first_number = int(self.entry.get())
        self.result = first_number
        self.is_mod = True
        self.entry.delete(0, END)

    def square_root(self):
        first_number = int(self.entry.get())
        sqrt = math.sqrt(first_number)
        print(sqrt)
        self.entry.delete(0, END)
        self.entry.insert(0, sqrt)

    def divede_by_x(self):
        first_number = int(self.entry.get())
        div_x = 1 / first_number
        self.entry.delete(0, END)
        self.entry.insert(0, div_x)

    def plus_or_minus(self):
        pass

    def euals(self):
        second_number = int(self.entry.get())
        self.entry.delete(0 ,END)
        if self.is_plus:
            self.entry.insert(0, self.result + second_number)
            self.is_plus = False
        elif self.is_minus:
            self.entry.insert(0, self.result - second_number)
            self.is_minus = False
        elif self.is_multi:
            self.entry.insert(0, self.result * second_number)
            self.is_multi = False
        elif self.is_divede:
            if second_number != 0:
                self.entry.insert(0, int(self.result / second_number))
            else:
                print("a number cannot be divided by zero")
            self.is_minus = False
        elif self.is_power:
            self.entry.insert(0, self.result ** second_number)
            self.is_multi = False
        elif self.is_mod:
            self.entry.insert(0, self.result % second_number)
            self.is_mod = False

    def delete(self):
        self.entry.delete(int(len(self.entry.get())) - 1,END)

    def clean(self):
        self.entry.delete(0, END)

    def clear(self):
        self.entry.delete(0, END)

    def create_interface(self):
        self.entry = Entry(self.frame, width= 40,   borderwidth= 5)
        self.entry.grid(row = 0, column = 0, columnspan = 4, ipadx=20, ipady = 20, sticky='ew')

        btn1 = Button(self.frame, text="1", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(1))
        btn1.grid(row=4, column=0, columnspan = 1,sticky='ew')
        btn2 = Button(self.frame, text="2", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(2))
        btn2.grid(row=4, column=1, columnspan = 1, sticky='ew')
        btn3 = Button(self.frame, text="3", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(3))
        btn3.grid(row=4, column=2, columnspan = 1, sticky='ew')
        btn4 = Button(self.frame, text="4", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(4))
        btn4.grid(row=5, column=0, columnspan = 1, sticky='ew')
        btn5 = Button(self.frame, text="5", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(5))
        btn5.grid(row=5, column=1, columnspan = 1, sticky='ew')
        btn6 = Button(self.frame, text="6", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(6))
        btn6.grid(row=5, column=2, columnspan = 1, sticky='ew')
        btn7 = Button(self.frame, text="7", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(7))
        btn7.grid(row=6, column=0, columnspan = 1, sticky='ew')
        btn8 = Button(self.frame, text="8", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(8))
        btn8.grid(row=6, column=1, columnspan = 1, sticky='ew')
        btn9 = Button(self.frame, text="9", padx = 10, pady = 10, bg = "white", command = lambda : self.ButtonAdd(9))
        btn9.grid(row=6, column=2, columnspan = 1, sticky='ew')
        btn0 = Button(self.frame, text="0", padx=10, pady=10, bg = "white", command = lambda : self.ButtonAdd(0))
        btn0.grid(row=7, column=1, columnspan=1, sticky='ew')


        btn_negatif = Button(self.frame, text="+/-", padx=10, pady=10, bg = "white")
        btn_negatif.grid(row=7, column=0, columnspan=1, sticky='ew')
        btn_comma = Button(self.frame, text=",", padx=10, pady=10, bg = "white")
        btn_comma.grid(row=7, column=2, columnspan=1, sticky='ew')
        btn_equal = Button(self.frame, text="=", padx=10, pady=10, bg = "#7EA7F9", command = self.euals)
        btn_equal.grid(row=7, column=3, columnspan=1, sticky='ew')

        btn_plus = Button(self.frame, text="+", padx=10, pady=10, bg = "#EAEAEB", command = self.plus)
        btn_plus.grid(row=6, column=3, columnspan=1, sticky='ew')
        btn_minus = Button(self.frame, text="-", padx=10, pady=10, bg = "#EAEAEB", command = self.minus)
        btn_minus.grid(row=5, column=3, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="x", padx=10, pady=10, bg = "#EAEAEB", command = self.multiply)
        btn_multi.grid(row=4, column=3, columnspan=1, sticky='ew')
        btn_divad = Button(self.frame, text="/", padx=10, pady=10, bg = "#EAEAEB", command = self.divde_by)
        btn_divad.grid(row=3, column=3, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="x^2", padx=10, pady=10, bg = "#EAEAEB", command = self.power)
        btn_multi.grid(row=3, column=2, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="sqrt", padx=10, pady=10, bg = "#EAEAEB", command = self.square_root)
        btn_multi.grid(row=3, column=1, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="1/x", padx=10, pady=10, bg = "#EAEAEB", command = self.divede_by_x)
        btn_multi.grid(row=3, column=0, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="Delete", padx=10, pady=10, bg = "#EAEAEB", command = lambda: self.delete)
        btn_multi.grid(row=2, column=3, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="C", padx=10, pady=10, bg = "#EAEAEB", command = lambda: self.clean)
        btn_multi.grid(row=2, column=2, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="CE", padx=10, pady=10, bg = "#EAEAEB", command = self.clear)
        btn_multi.grid(row=2, column=1, columnspan=1, sticky='ew')
        btn_multi = Button(self.frame, text="%", padx=10, pady=10, bg = "#EAEAEB", command = self.mod)
        btn_multi.grid(row=2, column=0, columnspan=1, sticky='ew')
        self.frame.pack()
    def ButtonAdd(self, number):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0,str(current) +  str(number))

if __name__ == '__main__':
    root = Tk()
    root.title("calculator")
    calc = calculator(root)
    calc.create_interface()
    root.mainloop()