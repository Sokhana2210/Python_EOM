# SokhanaNdzube

from tkinter import *
from tkinter import messagebox as mb
import random


window = Tk()
window.title("LOTTO")
window.geometry("700x350")
window.configure(bg='Yellow')

canvas = Canvas(window, width=321, height=157)
canvas.place(x=350, y=5)
img = PhotoImage(file="images.png")
canvas.create_image(0, 0, anchor=NW, image=img)


# Labels
label1 = Label(window, text="Name: ")
name = Entry(window)


label2 = Label(window, text="Surname:")
surname = Entry(window)

label3 = Label(window, text="Age:")
entry3 = Entry(window)
age = entry3.get()

# Placements
label1.place(x=0, y=0)
label2.place(x=0, y=50)
label3.place(x=0, y=100)

name.place(x=150, y=0)
surname.place(x=150, y=50)
entry3.place(x=150, y=100)


def check():
    f = open('results _file.txt', 'a+')
    nam = name.get()
    usurname = surname.get()
    text = "Name: "+nam + "\nSurname: "+usurname+"\nAge: "+entry3.get()
    f.write(text)
    f.close()
    try:
        ages = int(entry3.get())
        ages = ages
# Error/Exception Handling
        if ages < 18:
            mb.showwarning("Warning", "You too young bro")
        else:
            mb.showinfo("Success", "You are old enough")
            window.destroy()
            window2()
    except ValueError:
        mb.showerror("Value Error", "Please enter only a number")


def window2():
    window2 = Tk()
    window2.title("LOTTO")
    window2.geometry("700x350")
    window2.configure(bg='Yellow')
    frame = Frame(window2)
    frame.pack()

    def lotto_no():

        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        num4 = int(entry4.get())
        num5 = int(entry5.get())
        num6 = int(entry6.get())

        my_list = [num1, num2, num3, num4, num5, num6]

        q = random.randint(1, 49)
        w = random.randint(1, 49)
        e = random.randint(1, 49)
        r = random.randint(1, 49)
        t = random.randint(1, 49)
        y = random.randint(1, 49)
        mylotto_no2 = [q, w, e, r, t, y]
        print(mylotto_no2)

# if,elif,else
        print(my_list)
        count = 0
        for i in my_list:
            if i in mylotto_no2:
                count += 1
        x = "You got" + str(count)+" number(s) correct"
        label1['text'] = str(x) + "\nYou've won R10 000 000"
        if count == 0:
            label1['text'] = str(x) + "\nYou've Lost"
        elif count == 1:
            label1['text'] = str(x) + "\nYou've won R15"
        elif count == 2:
            label1['text'] = str(x) + "\nYou've won R50"
        elif count == 3:
            label1['text'] = str(x) + "\nYou've won R150"
        elif count == 4:
            label1['text'] = str(x) + "\nYou've won R2384"
        elif count == 5:
            label1['text'] = str(x) + "\nYou've won R10 000"
        elif count == 6:
            label1['text'] = str(x) + "\nYou've won R10 000 000"

    var = StringVar()
    var.set("Lotto Numbers Generator")
    frame1 = Frame(window2)
    frame.pack(side=TOP)
    label = Label(frame1, textvariable=var, font=("Arial", 30), width=24)
    label.pack(side=TOP)
    label = Label(frame1, textvariable="", width=24)
    label.pack(side=TOP)
    label = Label(frame1, textvariable="", width=24)
    label.pack(side=TOP)

    frame2 = Frame(window2)
    frame2.pack(side=TOP)
    entry1 = Entry(frame2, bd=15, font=("Arial", 20), justify='center', width=3)
    entry1.pack(side=LEFT)
    entry2 = Entry(frame2, bd=15, font=("Arial", 20), justify='center', width=3)
    entry2.pack(side=LEFT)
    entry3 = Entry(frame2,  bd=15, font=("Arial", 20), justify='center', width=3)
    entry3.pack(side=LEFT)
    entry4 = Entry(frame2, bd=15, font=("Arial", 20), justify='center', width=3)
    entry4.pack(side=LEFT)
    entry5 = Entry(frame2, bd=15, font=("Arial", 20), justify='center', width=3)
    entry5.pack(side=LEFT)
    entry6 = Entry(frame2, bd=15, font=("Arial", 20), justify='center', width=3)
    entry6.pack(side=LEFT)

    frame3 = Frame(window2, bg="yellow")
    frame3.pack(side=TOP)
    button1 = Button(frame3, text="Generate", command=lotto_no)
    button1.pack(side=TOP)
    label1 = Label(frame3, text="You got () numbers correct ", bg="yellow")
    label1.pack(side=LEFT, pady=50)

button1 = Button(window, text="Login", command=check)
button1.place(x=200, y=250)


window.mainloop()
