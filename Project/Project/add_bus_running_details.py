from tkinter import *
from tkinter.messagebox import *
import sqlite3
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Add bus running details')

Label().grid(row=0,column=0,padx=w//8)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=13)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 24 bold').grid(row=1,column=1,columnspan=13,pady=h//70)
Label(root,text='Add Bus Running Details',bg='sea green1',fg='Green',font='calibri 19 bold').grid(row=2,column=1,columnspan=13)

Label(root,text='Bus Id',font='calibri 15 bold').grid(row=3,column=1,pady=20,padx=w//100)
e_busid=Entry(root,width='8')
e_busid.grid(row=3,column=2)

Label(root,text='Running Date',font='calibri 15 bold').grid(row=3,column=3,padx=w//100)
e_rdate=Entry(root,width='20')
e_rdate.grid(row=3,column=4)

Label(root,text='Seat Available',font='calibri 15 bold').grid(row=3,column=5,pady=20,padx=w//100)
e_seat=Entry(root,width='15')
e_seat.grid(row=3,column=6)

def check_details():
    if e_busid.get()=='':
        showerror('Error','Please enter Bus Id')
    elif e_rdate.get()=='':
        showerror('Error','Please enter Running date')
    elif e_seat.get()=='':
        showerror('Error','Please enter Seat Available')
    else:
        rbid=e_busid.get()
        rdate=e_rdate.get()
        seat=e_seat.get()
        con=sqlite3.Connection('bus_reservation211b270')
        cur=con.cursor()

        cur.execute('''insert into running_details(RBID,running_date,seat_available) values(?,?,?)''',(rbid,rdate,seat))
        con.commit()
        con.close()
        showinfo('Running bus details','Bus running details added successfully')
Button(root,text='Add Run',font='calibri 14 bold',bg='PaleGreen2',command=check_details).grid(row=3,column=7,padx=w//200)

def delete_details():
    if e_busid.get()=='':
        showerror('Error','Please enter Bus Id')
    elif e_rdate.get()=='':
        showerror('Error','Please enter Running date')
    else:
        rbid=e_busid.get()
        rdate=e_rdate.get()
        con=sqlite3.Connection('bus_reservation211b270')
        cur=con.cursor()

        cur.execute('''delete from running_details where RBID=? and running_date=?''',(rbid,rdate))
        con.commit()
        con.close()
        showinfo('Running details','Bus running details deleted successfully')
Button(root,text='Delete Run',font='calibri 14 bold',bg='PaleGreen2',fg='orange red',command=delete_details).grid(row=3,column=8,padx=w//200)

def home():
    root.destroy()
    import twopage
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=4,column=1,columnspan=13,pady=h//60)

root.mainloop()
