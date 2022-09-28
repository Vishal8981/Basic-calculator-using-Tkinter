from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text") #it is used convert the value in integer
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scentry.get())
            except Exception as e:
                print(e)
                value="ERROR"
            scvalue.set(value)
            scentry.update()
    elif text == "C": #it is used to clear the screen the of the calculator
        scvalue.set("")
        scentry.update()
    else:
        value=scvalue.get()+text
        scvalue.set(value)
        scentry.update()
root=Tk()
root.title("CALCULATOR")
root.geometry("654x950")
root.wm_iconbitmap("1.con.png")

scvalue=StringVar()
scvalue.set("")
scentry=Entry(root,textvar=scvalue,font="lucida 40 bold ")
scentry.pack(fill=X,ipadx=8,pady=10,padx=10)

f1=Frame(root,bg="grey")
f1.pack()
b1=Button(f1,text="9",font="lucida 20 bold",padx=20,pady=22)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="8",font="lucida 20 bold",padx=20,pady=22)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="7",font="lucida 20 bold",padx=20,pady=22)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1=Frame(root,bg="grey")
f1.pack()
b1=Button(f1,text="6",font="lucida 20 bold",padx=20,pady=22)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="5",font="lucida 20 bold",padx=20,pady=22)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="4",font="lucida 20 bold",padx=20,pady=22)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1=Frame(root,bg="grey")
f1.pack()
b1=Button(f1,text="3",font="lucida 20 bold",padx=20,pady=22)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="2",font="lucida 20 bold",padx=20,pady=22)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="1",font="lucida 20 bold",padx=20,pady=22)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1=Frame(root,bg="grey")
f1.pack()
b1=Button(f1,text="0",font="lucida 20 bold",padx=23,pady=22)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="+",font="lucida 20 bold",padx=20,pady=22)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="-",font="lucida 20 bold",padx=19,pady=22)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1=Frame(root,bg="grey")
f1.pack()
b1=Button(f1,text="/",font="lucida 20 bold",padx=21,pady=22)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="*",font="lucida 20 bold",padx=20,pady=22)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="%",font="lucida 20 bold",padx=20,pady=22)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1=Frame(root,bg="grey")
f1.pack()
b1=Button(f1,text="=",font="lucida 20 bold",padx=17,pady=22)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
b2=Button(f1,text="C",font="lucida 20 bold",padx=20,pady=22)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
b3=Button(f1,text="00",font="lucida 16 bold",padx=19,pady=22)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

root.mainloop()