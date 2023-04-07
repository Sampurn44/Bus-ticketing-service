from tkinter import *
from tkinter.messagebox import *
import sqlite3
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Add route details')

Label().grid(row=0,column=0,padx=w//9)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=13)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 24 bold').grid(row=1,column=1,columnspan=13,pady=h//70)
Label(root,text='Add Bus Route Details',bg='sea green1',fg='Green',font='calibri 19 bold').grid(row=2,column=1,columnspan=13)

Label(root,text='Route Id',font='calibri 15 bold').grid(row=3,column=1,pady=h//70,padx=w//100)
e_rid=Entry(root,width='8')
e_rid.grid(row=3,column=2)

Label(root,text='Station Name',font='calibri 15 bold').grid(row=3,column=3,padx=w//100)
e_sname=Entry(root,width='30')
e_sname.grid(row=3,column=4)

Label(root,text='Station Id',font='calibri 15 bold').grid(row=3,column=5,pady=20,padx=w//100)
e_sid=Entry(root,width='15')
e_sid.grid(row=3,column=6)

def check_details():
    if e_rid.get()=='':
        showerror('Error','Please enter Route Id')
    elif e_sname.get()=='':
        showerror('Error','Please enter Station Name')
    elif e_sid.get()=='':
        showerror('Error','Please enter Station Id')
    else:
        rid=e_rid.get()
        sname=e_sname.get()
        sid=e_sid.get()
        con=sqlite3.Connection('bus_reservation_211b197')
        cur=con.cursor()

        cur.execute('''insert into route_details(RID,station_name,SID) values (?,?,?)''',(rid,sname,sid))
        con.commit()
        con.close()
        showinfo('Route entry','Bus route added successfully')
Button(root,text='Add Route',font='calibri 14 bold',bg='PaleGreen2',command=check_details).grid(row=3,column=7,padx=w//200)


def delete_details():
    if e_rid.get()=='':
        showerror('Error','Please enter Route Id')
    elif e_sid.get()=='':
        showerror('Error','Please enter Station Id')
    else:
        rid=e_rid.get()
        sid=e_sid.get()
        con=sqlite3.Connection('bus_reservation_211b197')
        cur=con.cursor()

        cur.execute('''delete from route_details where RID=? and SID=?''',(rid,sid))
        con.commit()
        con.close()
        showinfo('Route deletion','Bus route deleted successfully')
Button(root,text='Delete Route',font='calibri 14 bold',bg='PaleGreen2',fg='orange red',command=delete_details).grid(row=3,column=8,padx=w//200)

def home():
    root.destroy()
    import Home
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=4,column=1,columnspan=13,pady=h//60)

root.mainloop()
