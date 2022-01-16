from tkinter import *
import calendar

def month_calendar():
    month=int(monthspinBox.get())
    year=int(yearspinBox.get())
    data=calendar.month(year,month)
    textfield.delete(0.0,END)
    textfield.insert(INSERT,data)

root=Tk()
root.resizable(0,0)
root.title("AATISH CALENDAR")
root.config(bg='red')

monthLabel=Label(root,text='Month',font=('arial',12,'bold'),bg='red')
monthLabel.grid()

yearLabel=Label(root,text='Year',font=('arial',12,'bold'),bg='red')
yearLabel.grid(row=0,column=1)

monthspinBox=Spinbox(root,from_=1,to=12,width=8,font=('arial',10,'bold'))
monthspinBox.grid(row=1,column=0,padx=10)

yearspinBox=Spinbox(root,from_=1947,to=2057,width=8,font=('arial',10,'bold'))
yearspinBox.grid(row=1,column=1,padx=10)

goButton=Button(root,text='Go',font=('arial',12,'bold'),command=month_calendar)
goButton.grid(row=1,column=2,padx=10)

textfield=Text(root,width=24,height=8,fg='black')
textfield.grid(row=2,column=0,columnspan=3,pady=10)


root.mainloop()