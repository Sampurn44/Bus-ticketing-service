from tkinter import * 
root =Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.columnconfigure(0,weight=1)
root.title("Welcome Page")
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0)
Label(root,text="Online Bus Booking System",font='Times 30 bold',fg='red',bg='skyblue',).grid(row=1,column=0)
Label(root,text="Name : Sampurn Chouksey",fg="darkblue",font='cosmic 10').grid(row=2,column=0,pady=20)
Label(root,text="Enrollnment Number : 211B270",fg="darkblue",font='cosmic 10').grid(row=3,column=0,pady=20)
Label(root,text="Mobile:7724959230",fg="darkblue",font='cosmic 10').grid(row=4,column=0,pady=20)

Label(root,text="Submitted to : Dr. Mahesh Kumar",font='Times 30 bold',fg='red',bg='skyblue',).grid(row=5,column=0,pady=20)
Label(root,text="Project bases learning",font='Times 20 bold',fg='red').grid(row=6,column=0,pady=20)
def hi(e):
    root.destroy()
    import twopage
root.bind('<Escape>', lambda e:hi(e))
root.mainloop()
