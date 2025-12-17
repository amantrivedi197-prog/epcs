import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql

t=tkinter.Tk()
t.title('staff')
t.geometry('1000x600')
t.resizable(False,False)
def aman():
    t.destroy()
xt=[]
def filldata():
     db=pymysql.connect(host='localhost',user='root',password='Aman@1234',database='epcs')
     cur=db.cursor()
     sql="select staffid from attendencedata"
     cur.execute(sql)
     data=cur.fetchall()
     for res in data:
         xt.append(res[0])
     db.close()
def updatedata():
    db=pymysql.connect(host='localhost',user='root',password='Aman@1234',database='epcs')
    cur=db.cursor()
    xa=int(e1.get())
    xb=int(e2.get())
    xc=e3.get()
    xd=int(e4.get())
    sql = "update attendencedata set dataofpresent=%d,month='%s',status=%d where staffid=%d"%(xb,xc,xd,xa)
    cur.execute(sql)
    db.commit()
    db.close()
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    messagebox.showinfo('hii',"updated")  
def findata() :
    db=pymysql.connect(host='localhost',user='root',password='Aman@1234',database='epcs')
    cur=db.cursor()
    xa=int(e1.get())
    sql="select dataofpresent,month,status from attendencedata where staffid=%d" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e2.insert(0,str(data[0]))
    e3.insert(0,data[1])
    e4.insert(0,str(data[2]))
    db.close()

x=Canvas(t,height=600,width=1000,bg='lightgray')
x.place(x=1,y=1)
  
x1=Canvas(t,height=45,width=1000,bg='darkgray')
x1.place(x=1,y=1)
  
x2=Label(t,text='Staff Updation',font=('arial',20),bg='darkgray')
x2.place(x=450,y=5)
  
x.create_line(10,50,1000,50,width='0', fill='red')
  
x.create_line(50,90,950,90,width='0')
  
x.create_line(50,400,950,400,width='0')
x.create_line(50,90,50,400,width='0')
x.create_line(950,90,950,400,width='0')

a=Label(t,text='Staff Id',font=('arial',15),bg='lightgray')
a.place(x=110,y=100)
e1=ttk.Combobox(t,width=40)
filldata()
e1['values']=xt
e1.place(x=70,y=140)
filldata()

b=Label(t,text='Date of prasent',font=('arial',15),bg='lightgray')
b.place(x=400,y=100)
e2=Entry(t,width=40)
e2.place(x=350,y=140)
 
d=Label(t,text='Month',font=('arial',15),bg='lightgray')
d.place(x=750,y=100)
e3=ttk.Combobox(t,width=40,values=['January','February','March','April','May','June','July','August','September','October','November','December'])
e3.place(x=650,y=140)
  
 
e=Label(t,text='Status',font=('arial',15),bg='lightgray')
e.place(x=435,y=200)
e4=Entry(t,width=60)
e4.place(x=295,y=240)




bt=Button(t,text='Find ',bd=10,font=1,bg='tan',command=findata)
bt.place(x=260,y=450)
 
bt1=Button(t,text='Update ',bd=10,font=1,bg='tan',fg='red',command=updatedata)
bt1.place(x=460,y=450)

bt1=Button(t,text='Exit',bd=10,font=1,bg='tan',fg='red',command=aman)
bt1.place(x=650,y=450)
t.mainloop()