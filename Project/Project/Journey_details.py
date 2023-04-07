from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Journey details')

Label().grid(row=0,column=0,padx=w//9)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=2,columnspan=7)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 24 bold').grid(row=1,column=2,columnspan=7,pady=h//70)
Label(root,text='Enter Journey Details',bg='light green',fg='Green',font='calibri 19 bold').grid(row=2,column=2,columnspan=7)


Label(root,text='To',font='calibri 15 bold').grid(row=3,column=2,pady=h//60)
e_to=Entry(root)
e_to.grid(row=3,column=3)

Label(root,text='From',font='calibri 15 bold').grid(row=3,column=4)
e_from=Entry(root)
e_from.grid(row=3,column=5)

Label(root,text='Journey Date',font='calibri 15 bold').grid(row=3,column=6)
e_jdate=Entry(root)
e_jdate.grid(row=3,column=7)
bus_select=StringVar()
bus_select.set(None)
booked_bus_id=""  
Name=""
Age=""
Gender=""
Seats=""
Mobile=""
Fare=0

def buses():
    Label(root,text='Select Bus',font='calibri 15 bold',fg='Green').grid(row=4,column=2,padx=w//900)
    Label(root,text='Operator',font='calibri 15 bold',fg='Green').grid(row=4,column=3,padx=w//900)
    Label(root,text='Bus Type',font='calibri 15 bold',fg='Green').grid(row=4,column=4,padx=w//900)
    Label(root,text='Available',font='calibri 15 bold',fg='Green').grid(row=4,column=5,padx=w//200)
    Label(root,text='Capacity',font='calibri 15 bold',fg='Green').grid(row=4,column=6,padx=w//200)
    Label(root,text='Fare',font='calibri 15 bold',fg='Green').grid(row=4,column=7,padx=w//900)

    con=sqlite3.Connection('bus_reservation211b270')
    cur=con.cursor()

    to=e_to.get()
    From=e_from.get()
    jdate=e_jdate.get()
    cur.execute('''select op_name,bus_type,seat_available,seat_capacity,fare,BID from bus_details,running_details,route_details as f, route_details as t where f.station_name=? and t.station_name=? and running_date=? and RBID=BID and f.SID<t.SID and f.RID=route_id and t.RID=route_id''',(From,to,jdate))
    res=cur.fetchall()
    num=5
    for i in res:
        r1=Radiobutton(root,text='Select',font='calibri 12 bold',bg='spring green',variable=bus_select,value=i[5],indicator=0)
        r1.grid(row=num,column=2,padx=w//160,pady=h//80)
        
        operator=Label(root, text = i[0], fg = "blue1",font='calibri 12 bold')
        operator.grid(row = num, column=3)
        b_type=Label(root, text = i[1], fg = "blue1",font='calibri 12 bold')
        b_type.grid(row = num, column=4)
        a_seat=Label(root, text = i[2], fg = "blue1",font='calibri 12 bold')
        a_seat.grid(row = num, column=5)
        t_seat=Label(root, text = i[3], fg = "blue1",font='calibri 12 bold')
        t_seat.grid(row = num, column=6)
        fare=Label(root, text = i[4], fg = "blue1",font='calibri 12 bold')
        fare.grid(row = num, column=7)
        num=num+1
    
    con.commit()
    con.close()

    Button(root,text='Proceed to Book',font='calibri 15 bold',bg='spring green',command=details).grid(row=5,column=8,padx=w//300)

def details():
    booked_bus_id=bus_select.get()

    if booked_bus_id=='None':
        showwarning("Warning",'Please select a bus')

    else:
        Label(root,text='Fill Passenger details to book the bus ticket',bg='light blue',fg='red',font='calibri 24 bold').grid(row=20,column=2,columnspan=7,pady=h//30)
        
        Label(root,text='Name',font='calibri 14 bold').grid(row=21,column=1)
        e_name=Entry(root)
        e_name.grid(row=21,column=2)
        
        Label(root,text='Gender',font='calibri 14 bold').grid(row=21,column=3)
        e_gender=StringVar()
        option=('Male','Female','Other')
        e_gender.set('')
        g_menu=OptionMenu(root,e_gender,*option)
        g_menu.grid(row=21,column=4)
        
        Label(root,text='No. of seats',font='calibri 14 bold').grid(row=21,column=5)
        e_nos=Entry(root,width='3')
        e_nos.grid(row=21,column=6)
        
        Label(root,text='Mobile No',font='calibri 14 bold').grid(row=21,column=7)
        e_mob=Entry(root)
        e_mob.grid(row=21,column=8)
        
        Label(root,text='Age',font='calibri 14 bold').grid(row=21,column=9)
        e_age=Entry(root,width='3')
        e_age.grid(row=21,column=10)

        con=sqlite3.connect('bus_reservation211b270')
        cur=con.cursor()
        
        cur.execute('''select fare from bus_details where BID=?''',[booked_bus_id])
        Fare=cur.fetchone()
        fare=int(Fare[0])
        con.commit()
        con.close()


        def confirm():
            n=int(e_nos.get())
            tf=n*fare
            tf=str(tf)
            answer = messagebox.askyesno("Booking Confirmation", "Are you sure you want to book the bus?\n Total Amount to be paid is Rs "+tf)
            if answer:
                name=e_name.get()
                age=e_age.get()
                nos=e_nos.get()
                mob=e_mob.get()
                gender=e_gender.get()
                T_date=e_jdate.get()
                con=sqlite3.connect('bus_reservation211b270')
                cur=con.cursor()
                cur.execute('''select count(*)+1 from booking_history''')
                a=cur.fetchone()
                count=a[0]
                cur.execute('''insert into booking_history (pname,gender,age,mobile,bus,travelling_date,booking_date,no_of_seats,total_fare,booking_ref_number) values (?,?,?,?,?,?,DATE(),?,?,?)''',(name,gender,age,mob,booked_bus_id,T_date,nos,tf,count))

                cur.execute('''update running_details set seat_available=seat_available-? where RBID=? and running_date=?''',(nos,booked_bus_id,T_date))

                con.commit()
                con.close()

                root.destroy()
                import bus_ticket
            
        Button(root,text='Book Seat',font='calibri 15 bold',bg='spring green',command=confirm).grid(row=21,column=11,padx=w//60)
        
    
Button(root,text='Show Bus',font='calibri 15 bold',bg='medium sea green',command=buses).grid(row=3,column=8,padx=w//80)

def home():
    root.destroy()
    import twopage
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=3,column=9)

root.mainloop()
