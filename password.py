import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 1:
        password_label.config(text="Password length must be at least 1")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)


sm = tk.Tk()
sm.title("Password Generator")
sm.geometry('500x300')
sm.config(bg='#00EEEE')


length_lable = tk.Label(sm, text="Password Length:")
length_lable.place(x=200,y=50)


length_entry = tk.Entry(sm)
length_entry.place(x=200,y=75)


generate_button = tk.Button(sm, text="Generate Password", command=generate_password)
generate_button.place(x=200,y=100)

password_label = tk.Label(sm, text="")
password_label.place(x=200,y=130)


sm.mainloop()