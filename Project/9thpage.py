from tkinter import *
root=Tk()
root.geometry('800x800')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img11=PhotoImage(file='.vscode\Project\Bus_for_project.png')
Label(root,image=img11).grid(row=0,column=0,columnspan=7)
img111=PhotoImage(file='.vscode\Project\home.png')
Label(root,image=img111,bg='yellow').grid(row=5,column=4,columnspan=2,pady=60)
Label(root,text='Online Bus Booking System',font='Cosmic 14',fg='yellow',bg='Red').grid(row=1,column=0,pady=20,padx=w//3,columnspan=7)
Label(root,text='Add Bus Running Details',font='Cosmic 14',fg='yellow',bg='Red').grid(row=2,column=0,columnspan=7)
e13=Entry(root)
e13.grid(row=3,column=1)
e14=Entry(root)
e14.grid(row=3,column=2)
e15=Entry(root)
e15.grid(row=3,column=3)
Label(root,text='Bus Id',font='Helvetica 13').grid(row=3,column=0,columnspan=2)
Label(root,text='Running Date',font='Helvetica 13').grid(row=3,column=1,columnspan=2)
Label(root,text='Seat Availability',font='Helvetica 13').grid(row=3,column=2,columnspan=2)
Button(root,text='Add Run',font='Cosmic 14',fg='yellow',bg='Red').grid(row=3,column=4,columnspan=2)
Button(root,text='Delete Run',font='Cosmic 14',fg='yellow',bg='Red').grid(row=3,column=5,columnspan=2)
root.mainloop()