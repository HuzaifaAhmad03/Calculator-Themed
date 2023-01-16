from tkinter import *
import math

cb,cbf,cbn,cbnf,cbab,cbaf='','','','','',''
def ltheme():
    global cb,cbf,cbn,cbnf,cbab,cbaf
    cb='light sky blue'
    cbf='light steel blue'
    cbn='light sky blue'
    cbnf='black'
    cbab='floral white'
    cbaf='blue'

ltheme()


def calculator():

    
    w=Tk()
    w.geometry('230x230')
    w.configure(bg=cb)
    w.resizable(0,0)
    w.title("Calculator")

    def dtheme():
        global cb,cbf,cbn,cbnf,cbab,cbaf
        cb='black'
        cbf='gray3'
        cbn='black'
        cbnf='royal blue'
        cbab='midnight blue'
        cbaf='yellow'
        w.destroy()
        calculator()
    def ltheme():
        global cb,cbf,cbn,cbnf,cbab,cbaf
        cb='light sky blue'
        cbf='light steel blue'
        cbn='light sky blue'
        cbnf='black'
        cbab='floral white'
        cbaf='blue'
        w.destroy()
        calculator()
    def ftheme():
        global cb,cbf,cbn,cbnf,cbab,cbaf
        cb='red3'
        cbf='black'
        cbn='grey3'
        cbnf='yellow'
        cbab='blue'
        cbaf='yellow'
        w.destroy()
        calculator()
    def gtheme():
        global cb,cbf,cbn,cbnf,cbab,cbaf
        cb='black'
        cbf='gold'
        cbn='gold'
        cbnf='black'
        cbab='black'
        cbaf='yellow'
        w.destroy()
        calculator()
    

    mb=Menubutton(w,text="View")
    mb.menu=Menu(mb)
    mb["menu"]=mb.menu
    mb.grid(row=0,column=0)
    mb.menu.add_command(label='Light theme',command=lambda:ltheme())
    mb.menu.add_command(label='Dark theme',command=lambda:dtheme())
    mb.menu.add_command(label='Fire theme',command=lambda:ftheme())
    mb.menu.add_command(label='Golden theme',command=lambda:gtheme())



    inputs=StringVar()
    global s
    s=''

    def n_click(i):
        global s
        s=s+str(i)
        inputs.set(s)

    def c_click():
        global s
        s=""
        inputs.set("")
    
    def bk_click():
        global s
        s=s-s[-1]
        inputs.set(s)

    def eq_click():
        global s
        s=str(eval(s))
        inputs.set(s)
        s=""




    input_frame = Frame(w, width=156, height=25, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
    input_frame.place(x=40,y=5)
    e1=Entry(w,width=23,textvariable=inputs)
    e1.place(x=45,y=7)



    #add 45 to x axis and y axis
    badd=Button(w,height=2,width=5,text='+',bg=cbf,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda : n_click('+'))
    badd.place(x=30,y=35)

    bsub=Button(w,height=2,width=5,text='-',bg=cbf,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda : n_click('-'))
    bsub.place(x=75,y=35)

    bmult=Button(w,height=2,width=5,text='x',bg=cbf,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda : n_click('*'))
    bmult.place(x=120,y=35)

    bdiv=Button(w,height=2,width=5,text='÷',bg=cbf,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda : n_click('/'))
    bdiv.place(x=165,y=35)

    bequal=Button(w,height=2,width=5,text='=',bg=cbf,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:eq_click())
    bequal.place(x=165,y=120)


    bc=Button(w,height=2,width=5,text='C',bg='crimson',activeforeground=cbaf,activebackground='red',
    borderwidth=0,command=lambda:c_click())
    bc.place(x=165,y=160)

    b0=Button(w,height=2,width=5,text='0',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(0))
    b0.place(x=165,y=80)

    b1=Button(w,height=2,width=5,text='1',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(1))
    b1.place(x=30,y=160)

    b2=Button(w,height=2,width=5,text='2',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(2))
    b2.place(x=75,y=160)

    b3=Button(w,height=2,width=5,text='3',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(3))
    b3.place(x=120,y=160)

    b4=Button(w,height=2,width=5,text='4',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(4))
    b4.place(x=30,y=120)

    b5=Button(w,height=2,width=5,text='5',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(5))
    b5.place(x=75,y=120)

    b6=Button(w,height=2,width=5,text='6',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(6))
    b6.place(x=120,y=120)

    b7=Button(w,height=2,width=5,text='7',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(7))
    b7.place(x=30,y=80)

    b8=Button(w,height=2,width=5,text='8',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(8))
    b8.place(x=75,y=80)

    b9=Button(w,height=2,width=5,text='9',bg=cbn,activeforeground=cbaf,activebackground=cbab,foreground=cbnf,
    borderwidth=0,command=lambda:n_click(9))
    b9.place(x=120,y=80)


    w.mainloop()

calculator()