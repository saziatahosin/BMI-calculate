from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Calculator")
window.geometry("600x300")
window.minsize(600, 300)
window.maxsize(600, 300)

def bmi_calc():
    weight = int(weight_val.get())
    height = int(height_val.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi, 1)
    info(bmi)


def info(bmi):
    if bmi < 18.5:
        messagebox.showinfo('RESULT', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('RESULT', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('RESULT', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('RESULT', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('RESULT', 'ERROR!!!')

e1 = Label(window, text = "BMI Calculator", font = ("Helvetica", 24), fg = "black")

weight_lb = Label(window, text = "Enter Your Weight (kg)", font = ("Roboto", 11))

weight_val = StringVar()
weight = Entry(window, textvariable = weight_val)

height_lb = Label(window, text = "Enter Your Height (cm)", font = ("Roboto", 11))

height_val = StringVar()
height = Entry(window, textvariable = height_val)

calc_btn = Button(window, text = 'CALCULATE', font = ("Roboto", 11, "bold"),
             bg = "yellow", fg = "black",
             command = bmi_calc)


e1.pack()
weight_lb.pack()
weight.pack()
height_lb.pack()
height.pack()
calc_btn.pack()

window.mainloop()