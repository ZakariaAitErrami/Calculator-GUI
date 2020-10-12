import tkinter
from tkinter import ttk 
form = tkinter.Tk()
form.geometry('700x300')
form.title('Calculator')
fnt = 'None 30 bold'
lblnum1 = ttk.Label(form,text='Number 1:',font=fnt)
lblnum2 = ttk.Label(form,text='Number 2:',font=fnt)
sv1 = tkinter.StringVar()
sv2 = tkinter.StringVar()
#if I we used only sv1 for the two Entry if you change the number of number 1 the number 2 will change also
txtnum1 = ttk.Entry(form,font=fnt,textvariable=sv1)
txtnum2 = ttk.Entry(form,font=fnt,textvariable=sv2)
sv1.set('0')
sv2.set('0')
lblnum1.grid(row=0,column=0,pady=1,padx=10)
txtnum1.grid(row=0,column=1)
lblnum2.grid(row=1,column=0,pady=10,padx=10)  #pady=>padding top, padx=>padding left
txtnum2.grid(row=1,column=1)


def calc(ope):
	strn1 = str(txtnum1.get())
	strn2 = str(txtnum2.get())
	n1 = int(strn1)
	n2 = int(strn2)
	r = 0
	if ope=='+':
		r = n1+n2
	elif ope=='-':
		r = n1-n2
	elif ope=='*':
		r= n1*n2
	else:
		if n2==0:
			n2 = 1
		r = n1 / n2
	lblr['text']=('Result: %s %s %s = %s' %(n1,ope,n2,round(r,2))) #2 numbers after the comma

btns = ttk.Style()
btns.configure('TButton',font=fnt,padding=10)
frame = tkinter.Frame(form)
btn_width = 5
btnadd = ttk.Button(frame,text='+',width=btn_width,command=lambda:calc('+'))
btnsub = ttk.Button(frame,text='-',width=btn_width,command=lambda:calc('-'))
btnmul = ttk.Button(frame,text='*',width=btn_width,command=lambda:calc('*'))
btndiv = ttk.Button(frame,text='/',width=btn_width,command=lambda:calc('/'))
frame.grid(row=2,column=0,columnspan=2)
btnadd.grid(row=0,column=0)
btnsub.grid(row=0,column=1)
btnmul.grid(row=0,column=2)
btndiv.grid(row=0,column=3)

lblr = ttk.Label(frame,text='Result:',font=fnt)
lblr.grid(row=1,column=0,columnspan=4,padx=10)

form.mainloop()