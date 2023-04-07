from tkinter import * 
root =Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.title("Welcome Page")
img=PhotoImage(file='.\\Bus_for_project.png')
def seatbook():
    root.destroy()
    import Journey_details
def check():
    root.destroy()
    import Check_bookings
def busdetail():
    root.destroy()
    import buspage
Label(root,image=img).grid(row=0,column=1)
Label(root,text="Online Bus Booking System",font='Times 30 bold',fg='red',bg='skyblue').grid(row=1,column=1)
Button(root,text="Seat Booking",font="Times 15 bold",fg='yellow',bg='red',command=seatbook).grid(row=2,column=0)
Button(root,text="Check Booked Seat",font="Times 15 bold",fg='yellow',bg='red',command=check).grid(row=2,column=1)
Button(root,text="Add Bus Details",font="Times 15 bold",fg='yellow',bg='red',command=busdetail).grid(row=2,column=2)
Label(root,text="For admin only",font='Times 8 bold',fg='red').grid(row=3,column=2,pady=20)
root.mainloop()
