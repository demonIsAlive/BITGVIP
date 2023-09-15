from tkinter import *
import random

sm = Tk()
sm.title('PythonMasters')
sm.geometry('700x500')
sm.config(bg='#00EEEE')

ramSm = random.randint(0, 10)
trys = 5
sar = IntVar()
misp = StringVar()

def check_guess():
    global ranSm
    global trys
    usr_ip = sar.get()
    if trys > 0:
        if usr_ip == ramSm:
            msg = f'You won! {ramSm} is the right answer.'
        elif usr_ip > ramSm:
            trys -= 1
            msg = f'{usr_ip} is greater. You have {trys} attempt left.'
        elif usr_ip < ramSm:
            trys -= 1
            msg = f'{usr_ip} is smaller. You have {trys} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {trys} attempt left.'

    misp.set(msg)


Label(
    sm,
    text='Number Guessing Game',
    font=('Stencil Std', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#BF3EFF'
).pack(pady=(10, 0))

Entry(
    sm,
    textvariable=sar,
    font=('sans-serif', 18)
).pack(pady=(50, 10))

Button(
    sm,
    text='Submit Answer',
    font=('Tekton Pro', 18),
    command=check_guess
).pack()

Label(
    sm,
    textvariable=misp,
    bg='#5671A6',
    font=('Tekton Pro', 14)
).pack(pady=(20,0))


sm.mainloop()