from tkinter import *
from tkinter.messagebox import *
import sqlite3
root = Tk()
con=sqlite3.connect('bus_reservation_211b197')
cur=con.cursor()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Add operator details')

Label().grid(row=0,column=0,padx=w//10)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=13)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 24 bold').grid(row=1,column=1,columnspan=13,pady=h//70)
Label(root,text='Add Bus Operator Details',bg='sea green1',fg='Green',font='calibri 19 bold').grid(row=2,column=1,columnspan=13)

Label(root,text='Operator Id',font='calibri 15 bold').grid(row=3,column=1,pady=20,padx=w//100)
oid=Entry(root,width='10')
oid.grid(row=3,column=2)

Label(root,text='Name',font='calibri 15 bold').grid(row=3,column=3,padx=w//100)
name=Entry(root,width='15')
name.grid(row=3,column=4)

Label(root,text='Address',font='calibri 15 bold').grid(row=3,column=5,padx=w//100)
add=Entry(root)
add.grid(row=3,column=6)

Label(root,text='Phone',font='calibri 15 bold').grid(row=3,column=7,padx=w//100)
phn=Entry(root,width='12')
phn.grid(row=3,column=8)

Label(root,text='Email',font='calibri 15 bold').grid(row=3,column=9,padx=w//100)
email=Entry(root)
email.grid(row=3,column=10)

def check_details():
    oid1=oid.get()
    name1=name.get()
    add1=add.get()
    phn1=phn.get()
    email1=email.get()
    if oid1=='':
        showerror('Error','Please enter Operator Id')
    elif name1=='':
        showerror('Error','Please select Name')
    elif add1=='':
        showerror('Error','Please enter Address')
    elif phn1=='':
        showerror('Error','Please enter Phone number')
    elif email1=='':
        showerror('Error','Please enter Email')
    else:
        cur.execute('''insert into operator_details(operator_name,OID,address,phone_number,Email) values (?,?,?,?,?)''',(name1,oid1,add1,phn1,email1))
        con.commit()
        con.close()
        
        showinfo('Operator entry update','Operator record updated successfully')
Button(root,text='Add',font='calibri 15 bold',bg='PaleGreen2',command=check_details).grid(row=3,column=11,padx=w//200)

def Exit():
    root.destroy()
Button(root,text='Exit',font='calibri 15 bold',bg='PaleGreen2',command=Exit).grid(row=3,column=12,padx=w//200)

def home():
    root.destroy()
    import twopage
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=4,column=6)

root.mainloop()
