import tkinter as tk
root = tk.Tk()

root.title('App1')
root.geometry('500x300')

label = tk.Label(root, text='welcome',font=('Vogue Regular',40))
label.pack(padx=10,pady=10)

def on_clicked():
    print("button clicked")

button = tk.Button(root,text='button clicked',command=on_clicked)
button.pack(padx=10,pady=10)
root.mainloop()