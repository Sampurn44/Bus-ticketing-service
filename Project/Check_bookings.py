from tkinter import *
import sqlite3
from tkinter import messagebox
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Check Bookings')

Label().grid(row=0,column=0,padx=w/5.5)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=4)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 28 bold').grid(row=1,column=1,columnspan=4)
Label(root,text='Check Your Booking',bg='light green',fg='green',font='calibri 22 bold').grid(row=2,column=1,columnspan=4,pady=h//70)

Label(root,text='Enter Your Mobile No:',font='calibri 14 bold').grid(row=3,column=1)
bookings=Entry(root)
bookings.grid(row=3,column=2,padx=w//100)
c_bookings=''
def checkbooking():
    
    con=sqlite3.Connection('bus_reservation_211b197')
    cur=con.cursor()

    c_bookings=bookings.get()
    if c_bookings=='':
        messagebox.showerror('Error','Please enter Mobile Number')
    else:
        frame=Frame(root,relief='groove',bd=5)
        frame.grid(row=4,column=1,columnspan=5,pady=h//70)
        Label(frame,text='Passengers:',font='calibri 14 bold').grid(row=4,column=1)
        Label(frame,text='Gender:',font='calibri 14 bold').grid(row=4,column=3)
        Label(frame,text='No. of seats:',font='calibri 14 bold').grid(row=5,column=1)
        Label(frame,text='Phone:',font='calibri 14 bold').grid(row=5,column=3)
        Label(frame,text='Age:',font='calibri 14 bold').grid(row=6,column=1)
        Label(frame,text='Fare Rs:',font='calibri 14 bold').grid(row=6,column=3)
        Label(frame,text='Booking Ref.:',font='calibri 14 bold').grid(row=7,column=1)
        Label(frame,text='Bus details:',font='calibri 14 bold').grid(row=7,column=3)
        Label(frame,text='Travel on:',font='calibri 14 bold').grid(row=8,column=1)
        
        cur.execute('''select * from booking_history where mobile=?''',[c_bookings])
        res=cur.fetchall()
        
        for i in res:
            Label(frame,text=i[0],font='calibri 13').grid(row=4,column=2,padx=w//60)
            Label(frame,text=i[1],font='calibri 13').grid(row=4,column=4)
            Label(frame,text=i[7],font='calibri 13').grid(row=5,column=2)
            Label(frame,text=i[3],font='calibri 13').grid(row=5,column=4)
            Label(frame,text=i[2],font='calibri 13').grid(row=6,column=2)
            Label(frame,text=i[8],font='calibri 13').grid(row=6,column=4)
            Label(frame,text=i[9],font='calibri 13').grid(row=7,column=2)
            Label(frame,text=i[4],font='calibri 13').grid(row=7,column=4)
            Label(frame,text=i[5],font='calibri 13').grid(row=8,column=2)
            f=str(i[8])

        Label(frame,text='Total amount of Rs '+f+' to be paid at the time of boarding',font='calibri 12 italic').grid(row=9,column=1,columnspan=4)
        con.commit()
        con.close()
        
Button(root,text='Check Booking',font='calibri 14 bold',command=checkbooking).grid(row=3,column=3)

root.mainloop()
