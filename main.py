# Simple GUI Calculator
from tkinter import *
from turtle import width
import math
import tkinter.ttk

root = Tk()
root.title("Calculator ")
root.resizable(False, False)
root.propagate(0)
root.config(bg="#1F1F1F")
root.geometry("380x400+300+100")
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
        fr_ans.place_forget()
    except:
        pass

#list to store all operations
historylt={}
forma=0
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
    try:
        a=eval(ex)   #evaluvating the expression
    except:
        a="Invalid"
    global forma
    if isinstance(a, int):
        forma=a
    elif isinstance(a, float):
        forma=format(a, ".3f")
    elif len(a)==0:
        return
    else:
        forma=a
    global fr_ans
    try:
        fr_ans.place_forget()
    except:
        pass
    #showing result on screen
    fr_ans= Frame(root, width=200, height=50, bg='#1F1F1F')
    fr_ans.place(x=0, y=50)
    ans= Label(fr_ans, text=f"= {forma} ", font="ariel 17", fg="blue", bg="#1F1F1F")
    ans.pack()
    historylt[ex.replace("(", "").replace(")", "")]= forma
    if a=="Invalid":
        ans.config(fg="red")

# creating text box
e = Entry(root, width=25, borderwidth=0, font=('ariel', 16), bg="#1F1F1F", fg="white")
e.place(x=5, y=0, height=50)
e.bind("<Return>", equal)
e.bind('<Escape>', clear)
e.focus()

# history
#class for scrollableframe
class ScrollableFrame(tkinter.ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, width=360, height=350, bg="#1F1F1F", highlightthickness=0)
        scrollbar = tkinter.ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#1F1F1F")

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def his_close():
    frame.destroy()
    fr.destroy()
    root.geometry("380x400+300+100")
    root.resizable(False, False)
    try: fr_ans.destroy() 
    except: pass
    his.config(image=his_img, command=history)

def history():
    root.resizable(True, True)
    his.config(image=hisbackimg, command=his_close)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    global frame, fr
    frame= Frame(root, width=375, height=350)
    frame.grid(row=0, column=0, sticky="nsew")
    Grid.rowconfigure(frame, 0, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)
    fr=ScrollableFrame(frame)
    fr.grid(row=0, column=0, sticky="nsew")
    y=0
    for i in historylt:
        l1= Label(fr.scrollable_frame, text=f"{i} = {historylt[i]}", font="airel 16", fg="light blue", bg="#1F1F1F").grid(row=y, column=0)
        y+=1
    his.lift()
his_img= PhotoImage(file=r"history.png")
hisbackimg= PhotoImage(file=r"back.png")
his= Button(root, image=his_img, bg="darkslategrey", highlightthickness=0, activebackground="grey", command=history, cursor="hand2")
his.place(relx=0.84, rely=0)

def ansent(*args, **kwargs):
    clear()
    e.insert(0, forma)

e.bind('<Shift-Escape>', ansent)

# defining buttons
button7 = Button(root, text="7", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(7), bg='black', fg="white", activebackground="#6D6D6F")
button7.place(x=5,y=174)
button8 = Button(root, text="8", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(8), bg='black', fg="white", activebackground="#6D6D6F")
button8.place(x=98,y=174 )
button9 = Button(root, text="9", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(9), bg='black', fg="white", activebackground="#6D6D6F")
button9.place(x=191,y=174)
button4 = Button(root, text="4", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(4), bg='black', fg="white", activebackground="#6D6D6F")
button4.place(x=5,y=231)
button5 = Button(root, text="5", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(5), bg='black', fg="white", activebackground="#6D6D6F")
button5.place(x=98,y=231)
button6 = Button(root, text="6", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(6), bg='black', fg="white", activebackground="#6D6D6F")
button6.place(x=191,y=231)
button1 = Button(root, text="1", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(1), bg='black', fg="white", activebackground="#6D6D6F")
button1.place(x=5,y=288)
button2 = Button(root, text="2", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(2), bg='black', fg="white", activebackground="#6D6D6F")
button2.place(x=98,y=288)
button3 = Button(root, text="3", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(3), bg='black', fg="white", activebackground="#6D6D6F")
button3.place(x=191,y=288)
button0 = Button(root, text="0", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click(0), bg='black', fg="white", activebackground="#6D6D6F")
button0.place(x=98,y=345)
buttondot = Button(root, text=".", padx=34, pady=10,font=('ariel',15), borderwidth=0, command=lambda: click('.'), bg='black', fg="white", activebackground="#6D6D6F")
buttondot.place(x=191,y=345)

buttonClear = Button(root, text="C", font=('ariel', 15), bg="#19191B",padx=32, pady=9, borderwidth=0, command=clear, fg="white", activebackground="#6D6D6F")
buttonClear.place(x=5,y=345)
try:
    img_bac=PhotoImage(file=r"bac2.png")
    buttonbac = Button(root, image=img_bac, borderwidth=0, command=backspace, bg='black', fg="white", activebackground="#6D6D6F")
    buttonbac.place(x=191,y=117, height=50, width=85)
except:
    buttonbac = Button(root, text="<<<", font=('ariel', 15), bg="#19191B",padx=22, pady=9, borderwidth=0, command=backspace, fg="white", activebackground="#6D6D6F")
    buttonbac.place(x=191,y=117)
buttonAnsEnter = Button(root, text="AnsEn", padx=18, pady=11,  command=ansent, bg='black', fg="white", borderwidth=0, font=('ariel', 12), activebackground="#6D6D6F")
buttonAnsEnter.place(x=98,y=117)
buttonEqual = Button(root, text="=", padx=34, pady=10, command=equal, bg='#15456B', fg="white", font=('ariel', 15), activebackground="#0078D7")
buttonEqual.place(x=281,y=345)
buttonAdd = Button(root, text="+", padx=34, pady=10,  command=lambda: click('+'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonAdd.place(x=284,y=117)
buttonSub = Button(root, text="-", padx=36, pady=10,  command=lambda: click('-'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonSub.place(x=284,y=174)
buttonMul = Button(root, text="*", padx=36, pady=10,  command=lambda: click('*'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonMul.place(x=284,y=231)
buttonDiv = Button(root, text="/", padx=37, pady=10,  command=lambda: click('/'), bg='black', fg="white", borderwidth=0, font=('ariel', 15), activebackground="#6D6D6F")
buttonDiv.place(x=284,y=288)

root.mainloop()


# for i in range(len(list)):
#     def on_enter(a):
#         print(a)
#         a['background'] = '#6D6D6F'
#     def on_leave(a):
#         a['background'] = 'black'
#     list[i].bind("<Enter>", lambda *args, **kwargs: on_enter(list[i]))
#     print(i)
#     list[i].bind("<Leave>", lambda *args, **kwargs: on_leave(list[i]))
