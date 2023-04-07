from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img1=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img1).grid(row=0,column=0,columnspan=7)
Label(root,text='Online Bus Booking System',font='Times 18 bold',fg='yellow',bg='red').grid(row=1,column=0,pady=10,padx=w//3,columnspan=7)
Label(root,text='Add New Details To DataBase',font='Times 15 bold',fg='yellow',bg='red').grid(row=2,column=0,columnspan=7)
def opreator():
    root.destroy()
    import add_bus_operator_details
def bus():
    root.destroy()
    import add_bus_running_details
def route():
    root.destroy()
    import add_route_details
Button(root,text='New Operator',font='Times 15 italic',bg='yellow',fg='red',command=opreator).grid(row=3,column=1,columnspan=2)
Button(root,text='New Bus',font='Times 15 italic',bg='yellow',fg='red',command=bus).grid(row=3,column=2,columnspan=2)
Button(root,text='New Route',font='Times 15 italic',bg='yellow',fg='red',command=route).grid(row=3,column=3,columnspan=2)
#Button(root,text='New Run',font='Times 15 italic',bg='yellow',fg='red').grid(row=3,column=4,columnspan=2)
root.mainloop()
