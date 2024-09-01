from tkinter import *
root = Tk()
root.geometry('350x550')
root.title('Calculator')
root.maxsize(350,550)
root.minsize(350,550)
root.configure(bg="dark gray")

def click(event):
    text = event.widget.cget("text")
    print(text,end="")
    if text == "=":
        value = eval(input_text.get())
        print(value)
        input_text.set(value)
        screen.update()
    elif text == "C":
        input_text.set(input_text.get()[:-1])
        screen.update()
    elif text == "AC":
        input_text.set("")
        screen.update()
    else:
        input_text.set(input_text.get() + text)
        screen.update()

input_text = StringVar()
'''input_text.set("")'''
screen = Entry(root,width=36,font=30,justify=RIGHT,textvariable=input_text)
bt1 = Button(root,text="AC",width=8,height=4)
bt1.bind("<Button-1>" , click)

bt2 = Button(root,text="(",width=8,height=4)
bt2.bind("<Button-1>" , click)

bt3 = Button(root,text=")",width=8,height=4)
bt3.bind("<Button-1>" , click)

bt4 = Button(root,text="C",width=8,height=4)
bt4.bind("<Button-1>" , click)

bt5 = Button(root,text="7",width=8,height=4)
bt5.bind("<Button-1>" , click)

bt6 = Button(root,text="8",width=8,height=4)
bt6.bind("<Button-1>" , click)

bt7 = Button(root,text="9",width=8,height=4)
bt7.bind("<Button-1>" , click)

bt8 = Button(root,text="/",width=8,height=4)
bt8.bind("<Button-1>" , click)

bt9 = Button(root,text="4",width=8,height=4)
bt9.bind("<Button-1>" , click)

bt10 = Button(root,text="5",width=8,height=4)
bt10.bind("<Button-1>" , click)

bt11 = Button(root,text="6",width=8,height=4)
bt11.bind("<Button-1>" , click)

bt12 = Button(root,text="*",width=8,height=4)
bt12.bind("<Button-1>" , click)

bt13 = Button(root,text="1",width=8,height=4)
bt13.bind("<Button-1>" , click)

bt14 = Button(root,text="2",width=8,height=4)
bt14.bind("<Button-1>" , click)

bt15 = Button(root,text="3",width=8,height=4)
bt15.bind("<Button-1>" , click)

'''bt16 = Button(root,text="-",width=8,height=4)
bt16.bind("<Button-1>" , click)'''

bt17 = Button(root,text="0",width=8,height=4)
bt17.bind("<Button-1>" , click)

bt18 = Button(root,text=".",width=8,height=4)
bt18.bind("<Button-1>" , click)

bt19 = Button(root,text="-",width=8,height=4)
bt19.bind("<Button-1>" , click)

bt20 = Button(root,text="+",width=8,height=9)
bt20.bind("<Button-1>" , click)

bt21 = Button(root,text="=",width=44,height=4)
bt21.bind("<Button-1>" , click)

screen.grid(row=0,column=0,pady=20,ipady=10,padx=10)
bt1.place(x=15,y=70)
bt2.place(x=100,y=70)
bt3.place(x=185,y=70)
bt4.place(x=270,y=70)

bt5.place(x=15,y=150)
bt6.place(x=100,y=150)
bt7.place(x=185,y=150)
bt8.place(x=270,y=150)

bt9.place(x=15,y=230)
bt10.place(x=100,y=230)
bt11.place(x=185,y=230)
bt12.place(x=270,y=230)

bt13.place(x=15,y=310)
bt14.place(x=100,y=310)
bt15.place(x=185,y=310)
'''bt16.place(x=270,y=310)'''

bt17.place(x=15,y=390)
bt18.place(x=100,y=390)
bt19.place(x=185,y=390)
bt20.place(x=270,y=310)

bt21.place(x=15,y=470)
root.mainloop()