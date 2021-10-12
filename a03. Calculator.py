from tkinter import *

root = Tk(screenName="Calculator")
root.title("Calculator by ZiON")
root.iconbitmap('F:/CSE~DIU/ZiON/VisualStudio/Python/Res/calcIco.ico')
root.config(bg='black')
canvas = Canvas(root,background="black",height=420,width=300,borderwidth=50,)
canvas.grid()
frame = Frame(canvas,background="black",height=420,width=300,borderwidth=50)
frame.grid()

monitor = Entry(frame,width=59,borderwidth=8,bg="black",foreground="white")
monitor.grid(row=0,column=0,columnspan=4,pady=40)

first_n = 0
opr = "null"

def takeInp(inp):
    global first_n
    global opr
    if inp == "AC":
        monitor.delete(0,END)
    elif inp == "<<":
        p = monitor.get()
        x = len(str(p))
        monitor.delete(0,END)
        monitor.insert(0,str(p[0:x-1]))
    elif inp == "rem":
        try:
            opr = "rem"
            x = monitor.get()
            monitor.delete(0,END)
            first_n = int(x)
        except:
            monitor.insert(0,"Reminder from float not possible")

    elif inp == "/":
        opr = "div"
        x = monitor.get()
        monitor.delete(0,END)
        first_n = float(x)
    elif inp == ".":
        x = monitor.get()
        ff = str(x)+'.'
        monitor.delete(0,END)
        monitor.insert(0,ff)
    elif inp == "mul":
        opr = "mul"
        x = monitor.get()
        monitor.delete(0,END)
        first_n = float(x)
    elif inp == "-":
        opr = "sub"
        x = monitor.get()
        monitor.delete(0,END)
        first_n = float(x)
    elif inp == "+":
        opr = "add"
        x = monitor.get()
        monitor.delete(0,END)
        first_n = float(x)
    else:
        curr = monitor.get()
        monitor.delete(0,END)
        monitor.insert(0,str(curr)+str(inp))

def equal_cal():
    second_num = monitor.get()
    monitor.delete(0,END)
    if opr == "add":
        monitor.insert(0,first_n + int(second_num))
    elif opr == "sub":
        monitor.insert(0,first_n - int(second_num))
    elif opr == "mul":
        monitor.insert(0,first_n * int(second_num))
    elif opr == "div":
        monitor.insert(0,first_n / int(second_num))
    elif opr == "rem":
        monitor.insert(0,first_n % int(second_num))


btn_1 = Button(frame,text = "1",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(1))
btn_2 = Button(frame,text = "2",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(2))
btn_3 = Button(frame,text = "3",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(3))
btn_4 = Button(frame,text = "4",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(4))
btn_5 = Button(frame,text = "5",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(5))
btn_6 = Button(frame,text = "6",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(6))
btn_7 = Button(frame,text = "7",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(7))
btn_8 = Button(frame,text = "8",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(8))
btn_9 = Button(frame,text = "9",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(9))
btn_0 = Button(frame,text = "0",font = ("Arial",12), padx=30,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp(0))
btn_dot = Button(frame,text = ".",font = ("Arial",12), padx=32,pady=10,bg="black",fg="white",border=8,borderwidth=5, command=lambda: takeInp('.'))
btn_s = Button(frame,text = "+",font = ("Arial",12), padx=30,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp('+'))
btn_m = Button(frame,text = "-",font = ("Arial",12), padx=32,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp('-'))
btn_d = Button(frame,text = "/",font = ("Arial",12), padx=33,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp('/'))
btn_mp = Button(frame,text = "x",font = ("Arial",12), padx=31,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp("mul"))
btn_rem = Button(frame,text = "%",font = ("Arial",12), padx=28,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp("rem"))
btn_back = Button(frame,text = "<<",font = ("Arial",12), padx=27,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp('<<'))
btn_clr = Button(frame,text = "AC",font = ("Arial",12), padx=24,pady=10,bg="black",fg="orange",border=8,borderwidth=5, command=lambda: takeInp('AC'))
btn_eql = Button(frame,text = "=",font = ("Arial",12), padx=30,pady=37,bg="black",fg="orange",border=8,borderwidth=5, command=equal_cal)


btn_clr.grid(row=1,column=0)
btn_back.grid(row=1,column=1)
btn_rem.grid(row=1,column=2)
btn_d.grid(row=1,column=3)

btn_7.grid(row=2,column=0)
btn_8.grid(row=2,column=1)
btn_9.grid(row=2,column=2)
btn_mp.grid(row=2,column=3)

btn_4.grid(row=3,column=0)
btn_5.grid(row=3,column=1)
btn_6.grid(row=3,column=2)
btn_m.grid(row=3,column=3)


btn_1.grid(row=4,column=0)
btn_2.grid(row=4,column=1)
btn_3.grid(row=4,column=2)
btn_eql.grid(row=4,rowspan=2,column=3)

btn_0.grid(row=5,column=0)
btn_dot.grid(row=5,column=1)
btn_s.grid(row=5,column=2)




root.mainloop()

