import string
import random
from tkinter import *


def generate_password():
    combination = string.ascii_letters + string.digits + string.punctuation
    length = int(length_entry.get())
    password = "".join(random.choices(combination, k=length))
    password_label.config(text=f"Your password is: {password}")

root = Tk()
root.title("Password Generator")

length_label = Label(root, text="Enter the length of the password:", width=50, bg="yellow")
length_label.pack(pady=10)

length_entry = Entry(root)
length_entry.pack(pady=10)

generate_button = Button(root, text="Generate Password", width =50, bg="yellow", command=generate_password)
generate_button.pack(pady=10)

password_label = Label(root, text="")
password_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
