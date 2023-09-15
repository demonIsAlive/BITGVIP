import time
from tkinter import *
from tkinter import messagebox


m = ("Arial",24)

sm = Tk()
sm.geometry("700x500")
sm.title("PythonGuides")
sm.config(bg='#5671A6')

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("20")

hour_mf= Entry(
	sm, 
	width=3, 
	font=m,
	textvariable=hour
	)

hour_mf.place(x=250,y=200)

mins_mf= Entry(
	sm, 
	width=3, 
	font=m,
	textvariable=minute)

mins_mf.place(x=300,y=200)

sec_mf = Entry(
	sm, 
	width=3, 
	font=m,
	textvariable=second)

sec_mf.place(x=350,y=200)


def startCountdown():
	try:
		userinput = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		messagebox.showwarning('', 'Invalid Input!')
	while userinput >-1:
		mins,secs = divmod(userinput,60) 

		hours=0
		if mins >60:
			
		
			hours, mins = divmod(mins, 60)
	
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

	
		sm.update()
		time.sleep(1)

	
		if (userinput == 0):
			messagebox.showinfo("", "Time's Up")
		

		userinput -= 1

start_btn = Button(
	sm, 
	text='START', 
	bd='15',
	command= startCountdown
	)

start_btn.place(x = 300,y = 280)


sm.mainloop()