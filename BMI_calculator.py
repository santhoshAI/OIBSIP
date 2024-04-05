from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+1400+100")
root.resizable(False, False)
root.configure(bg="#ECF8FF")

# BMI
def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m = h/100   # height in meter
    bmi = round(float(w/(m**2)), 1)
    label1.config(text = bmi)
    
    if bmi<18.5:
        label2.config(text="Underweight!")
        label3.config(text="⠀  You have lower weight then\nnormal body!")
        
    elif bmi>=18.5 and bmi<25:
        label2.config(text="Normalweight!")
        label3.config(text="It indicates that you are healthy!")
        
    elif bmi>=25 and bmi<30:
        label2.config(text="Overweight!")
        label3.config(text="It indicates that a person \n slightly overweight! \n A doctor may advise to lose some \n weight for health reasons!")
        
    else:
        label2.config(text="Obese!") 
        label3.config(text="Health may be at risk , if they \n do not lose weigh")   
    


# icon
image_icon = PhotoImage(file="img/icon_with_bg.png")
root.iconphoto(False, image_icon)


# top
top = PhotoImage(file="img/top.png")
img_top = Label(root, image=top, background="#ECF8FF")
img_top.place(x=-10, y=-10)

# bottom box
Label(root, width=72, height=13, bg="lightblue").pack(side=BOTTOM)


# box
box = PhotoImage(file="img/box.png")
Label(root, image=box, background="#D9D9D9").place(x=0, y=72)


# Height and weight Label
Label(root, text="Height in cm", font="arial 18 bold", bg='#ECF8FF', fg="#000").place(x=50, y=108)
Label(root, text="Weight in kg", font="arial 18 bold", bg='#ECF8FF', fg="#000").place(x=280, y=108)


# scale
scale = PhotoImage(file="img/scale.png")
Label(root, image=scale, bg="lightblue").place(x=0, y=277)


# slider 1
curren_value = tk.DoubleVar()

def get_current_value():
    return f"{curren_value.get(): .2f}"

def slider_changed(event):
    Height.set(get_current_value())
    
    size = int(float(get_current_value()))
    img = (Image.open("img/man.png"))
    resized_image = img.resize((50, 60+size))
    photo_man = ImageTk.PhotoImage(resized_image)
    man_image.config(image=photo_man)
    man_image.place(x=70, y=510-size)
    man_image.image = photo_man
    
    
    
style = ttk.Style()
style.configure("TScale", background= "#ECF8FF")
slider = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=slider_changed, variable=curren_value).place(x=72, y=223)


# slider 2
curren_value2 = tk.DoubleVar()

def get_current_value2():
    return f"{curren_value2.get(): .2f}"

def slider_changed2(event):
    Weight.set(get_current_value2())
    
style2 = ttk.Style()
style2.configure("TScale", background= "#ECF8FF")
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale", command=slider_changed2, variable=curren_value2).place(x=300, y=223)


# input box
Height = StringVar()
Weight = StringVar()
height_entry = Entry(root, textvariable=Height, width=5, font="arial 50", bg='#ECF8FF', fg="#000", bd=0, justify=CENTER).place(x=27, y=140)
Height.set(get_current_value()) 

weight_entry = Entry(root, textvariable=Weight, width=5, font="arial 50", bg='#ECF8FF', fg="#000", bd=0, justify=CENTER).place(x=258, y=140) 
Weight.set(get_current_value2())


# man image
man_image = Label(root, background="lightblue")
man_image.place(x=70, y=520)

# Button
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=220, y=360)

# result
label1 = Label(root, font="arial 50 bold", fg="#000000", bg="lightblue")
label1.place(x=220, y=277)

label2 = Label(root, font="arial 20 bold", fg="#000000", bg="lightblue")
label2.place(x=220, y=415)

label3 = Label(root, font="arial 15", fg="#000000", bg="lightblue")
label3.place(x=160, y=450)


root.mainloop()