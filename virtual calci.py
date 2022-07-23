# virtual calci
import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title('CALCULATOR')
root.resizable(False,False)
operator=''
text_Input=StringVar()
def click_button(numbers):
                global operator
                operator=operator + str(numbers)
                text_Input.set(operator)
def clear_button():
                global operator
                operator=''
                text_Input.set(operator)
def result_button():
                global operator
                sumup=str(eval(operator))
                text_Input.set(sumup)
                
                            
# entry
e1=Entry(root,width=30,bd=15,bg='cyan',font=('Arial',20,'bold'),textvariable=text_Input,insertwidth=3,justify='right')
e1.grid(columnspan=4)

# buttons
b1=Button(root,text='7',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(7))
b1.grid(row=1,column=0)

b2=Button(root,text='8',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(8))
b2.grid(row=1,column=1)

b3=Button(root,text='9',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(9))
b3.grid(row=1,column=2)

b4=Button(root,text='+',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button('+'))
b4.grid(row=1,column=3)

b5=Button(root,text='4',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(4))
b5.grid(row=2,column=0)

b6=Button(root,text='5',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(5))
b6.grid(row=2,column=1)

b7=Button(root,text='6',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(6))
b7.grid(row=2,column=2)

b8=Button(root,text='-',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button('-'))
b8.grid(row=2,column=3)

b9=Button(root,text='1',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(1))
b9.grid(row=3,column=0)

b10=Button(root,text='2',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(2))
b10.grid(row=3,column=1)

b11=Button(root,text='3',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(3))
b11.grid(row=3,column=2)

b12=Button(root,text='*',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button('*'))
b12.grid(row=3,column=3)

b13=Button(root,text='0',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button(0))
b13.grid(row=4,column=0)

b14=Button(root,text='C',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:clear_button())
b14.grid(row=4,column=1)

b15=Button(root,text='=',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:result_button())
b15.grid(row=4,column=2)

b16=Button(root,text='/',padx=30,pady=30,font=('Arial',20,'bold'),relief='ridge',bd=10,command=lambda:click_button('/'))
b16.grid(row=4,column=3)
root.mainloop()

