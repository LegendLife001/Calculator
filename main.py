# Simple GUI Calculator
from tkinter import *
from turtle import width
import math

root = Tk()
root.title("Calculator ")
root.resizable(False, False)
root.propagate(0)
root.config(bg="#1F1F1F")
root.geometry("380x350+300+100")
try:
    root.wm_iconbitmap("cal.ico")
except:
    pass

def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def backspace(*args, **kwargs):
    e.delete(e.index("end") - 1)

def clear(*args, **kwargs):
    e.delete(0, END)
    try:
        fr.place_forget()
    except:
        pass

def equal(*args, **kwargs):
    pre=["+", "-", "*", "/"]
    x=e.get()
    if "(" not in x and ")" not in x:   #if bracket is already included we shouldn't defined brackets
        ex=''
        #definiting the expression with proper brackets 
        hold=1
        for i in x:
            if i in pre:
                hold+=1
        ex="("*hold
        for i in x:
            if i in pre:
                ex+=")"+i
            else:
                ex+=i
        ex+=")"
        
    elif "(" in x and ")" in x:
        ex=x
    else:
        ex=0
        a="Invalid"
    print(ex)
    try:
        a=eval(ex)   #evaluvating the expression
    except:
        a="Invalid"
    if isinstance(a, int):
        forma=a
    elif isinstance(a, float):
        forma=format(a, ".3f")
    elif len(a)==0:
        return
    else:
        forma=a
    global fr
    try:
        fr.place_forget()
    except:
        pass
    #showing result on screen
    fr= Frame(root, width=170, height=50, bg='#1F1F1F')
    fr.place(x=0, y=40)
    ans= Label(fr, text=f'= {forma}', font="ariel 17", fg="blue", bg="#1F1F1F")
    ans.pack()
    if a=="Invalid":
        ans.config(fg="red")

# creating text box
e = Entry(root, width=25, borderwidth=0, font=('ariel', 16), bg="#1F1F1F", fg="white")
e.place(x=5, y=0, height=50)
e.bind("<Return>", equal)
e.focus()
# defining buttons
button7 = Button(root, text="7", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(7), bg='black', fg="white", activebackground="#6D6D6F")
button7.place(x=5,y=117)
button8 = Button(root, text="8", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(8), bg='black', fg="white", activebackground="#6D6D6F")
button8.place(x=98,y=117)
button9 = Button(root, text="9", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(9), bg='black', fg="white", activebackground="#6D6D6F")
button9.place(x=191,y=117)
button4 = Button(root, text="4", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(4), bg='black', fg="white", activebackground="#6D6D6F")
button4.place(x=5,y=174)
button5 = Button(root, text="5", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(5), bg='black', fg="white", activebackground="#6D6D6F")
button5.place(x=98,y=174)
button6 = Button(root, text="6", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(6), bg='black', fg="white", activebackground="#6D6D6F")
button6.place(x=191,y=174)
button1 = Button(root, text="1", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(1), bg='black', fg="white", activebackground="#6D6D6F")
button1.place(x=5,y=231)
button2 = Button(root, text="2", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(2), bg='black', fg="white", activebackground="#6D6D6F")
button2.place(x=98,y=231)
button3 = Button(root, text="3", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(3), bg='black', fg="white", activebackground="#6D6D6F")
button3.place(x=191,y=231)
button0 = Button(root, text="0", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(0), bg='black', fg="white", activebackground="#6D6D6F")
button0.place(x=98,y=288)
buttondot = Button(root, text=".", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click('.'), bg='black', fg="white", activebackground="#6D6D6F")
buttondot.place(x=191,y=288)

buttonClear = Button(root, text="C", font=('ariel', 15), bg="#19191B",padx=32, pady=9, borderwidth=0, command=clear, fg="white", activebackground="#6D6D6F")
buttonClear.place(x=5,y=288)
try:
    img_bac=PhotoImage(file=r"bac2.png")
    buttonbac = Button(root, image=img_bac, font=('ariel', 14), borderwidth=0, command=backspace, bg='black', fg="white", activebackground="#6D6D6F")
    buttonbac.place(x=191,y=60, height=55, width=90)
except:
    buttonbac = Button(root, text="<<<", font=('ariel', 15), bg="#19191B",padx=22, pady=9, borderwidth=0, command=backspace, fg="white", activebackground="#6D6D6F")
    buttonbac.place(x=191,y=60)
buttonEqual = Button(root, text="=", padx=34, pady=10, command=equal, bg='#15456B', fg="white", font=('ariel', 15), activebackground="#0078D7")
buttonEqual.place(x=281,y=288)
buttonAdd = Button(root, text="+", padx=34, pady=10,  command=lambda: click('+'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonAdd.place(x=284,y=60)
buttonSub = Button(root, text="-", padx=36, pady=10,  command=lambda: click('-'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonSub.place(x=284,y=117)
buttonMul = Button(root, text="*", padx=36, pady=10,  command=lambda: click('*'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonMul.place(x=284,y=174)
buttonDiv = Button(root, text="/", padx=37, pady=10,  command=lambda: click('/'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonDiv.place(x=284,y=231)

root.mainloop()
