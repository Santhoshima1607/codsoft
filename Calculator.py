from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("330x350+600+200")
root.resizable(False,False)
root.configure(bg="black")

equation=""

def show(value):
    global equation
    equation=equation+value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation != "":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)         


#GUI

label_result=Label(root,width=25,height=2,text="",font=("arial",30),background="#D0D4CA")
label_result.pack()

Button(root,text="C",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#1640D6",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("/")).place(x=90,y=100)
Button(root,text="%",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("%")).place(x=170,y=100)
Button(root,text="*",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("*")).place(x=250,y=100)

Button(root,text="7",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("7")).place(x=10,y=150)
Button(root,text="8",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("8")).place(x=90,y=150)
Button(root,text="9",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("9")).place(x=170,y=150)
Button(root,text="-",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("-")).place(x=250,y=150)


Button(root,text="4",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("4")).place(x=10,y=200)
Button(root,text="5",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("5")).place(x=90,y=200)
Button(root,text="6",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("6")).place(x=170,y=200)
Button(root,text="+",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("+")).place(x=250,y=200)

Button(root,text="1",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("1")).place(x=10,y=250)
Button(root,text="2",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("2")).place(x=90,y=250)
Button(root,text="3",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("3")).place(x=170,y=250)
Button(root,text="0",width=11,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show("0")).place(x=10,y=300)

Button(root,text=".",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#272829",command=lambda:show(".")).place(x=170,y=300)
Button(root,text="=",width=5,height=3,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#FA7D09",command=lambda:calculate()).place(x=250,y=250)





root.mainloop()
