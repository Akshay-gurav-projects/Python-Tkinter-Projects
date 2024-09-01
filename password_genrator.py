import string
import random
from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('Password generator')

def generate():
    pass_length = int(spin_box.get())
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print(s)
    random.shuffle(s)
    print(s)
    password = (s[0:pass_length])
    en2.insert(0,password)



choice = IntVar()
lb1 = Label(root,text="Please enter you name",font='cambria 15 bold')
lb1.pack()

en1 = Entry(root)
en1.pack()

lb2 = Label(text="Selcet password type")
lb2.pack()

weak = Radiobutton(root,text="weak",value=1,variable=choice)
weak.pack()

Medium = Radiobutton(root,text="Medium",value=2,variable=choice)
Medium.pack()

Strong = Radiobutton(root,text="Strong",value=3,variable=choice)
Strong.pack()

lb3 = Label(root,text="Password length",font='cambria 15 bold')
lb3.pack()

spin_box = Spinbox(root,from_=5,to=20)
spin_box.pack()

generatebutton = Button(root,text='Generate',command=generate)
generatebutton.pack()

en2 = Entry(root)
en2.pack()

copybutton = Button(root,text='copy')
copybutton.pack()

root.mainloop()