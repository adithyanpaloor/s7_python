import tkinter as tk
from tkinter import messagebox

from gui_i import button

root = tk.Tk()
root.title('Login')
root.geometry('300x300')


label = tk.Label(root,text='LOGIN',font=('Arial',20,'bold'))
label.pack(padx=10,pady=20)

username = tk.Label(root,text='USERNAME')
username.pack(padx=10,pady=5)
username_entry = tk.Entry(root,width=40)
username_entry.pack(padx=10,pady=2)

password = tk.Label(root,text='PASSWORD')
password.pack(padx=10,pady=5)
password_entry = tk.Entry(root,width=40)
password_entry.pack(padx=10,pady=2)

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'adithyan' and password == '123':
        print('Login Successful')
        messagebox.showinfo('Login Successful','Login Successful')
    else:
        messagebox.showerror('Login Failed','Login Failed')

button = tk.Button(root,text='login',command=login)
button.pack(padx=10,pady=10)

root.mainloop()