import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def handle_signup():
    username_entry = ttk.Entry(root, font=("Arial", 14))
    password_entry = ttk.Entry(root, show="*", font=("Arial", 14))

    if username and password:
        messagebox.showinfo("Success!", f"Account created for {username_entry}!")
    else:
        messagebox.showwarning("Input failed", f"Please fill out all fields.")

root = tk.Tk()
root.geometry("360x640")
root.config(bg="lightpink")
root.title("Mobile App")

title = ttk.Label(
    root,
    text="Period Tracker",
    font=("Arial", 20)
)
title.pack(pady=20)

label = tk.Label(root, text="Welcome! Please sign in! No account? No worries, sign up!", bg="red", fg="white")

label.pack()

username = ttk.Entry(root, font=("Arial", 14))
username.pack(fill="x", padx=20, pady=10)

password = ttk.Entry(root, show="*", font=("Arial", 14))
password.pack(fill="x", padx=20, pady=10)

login_btn = ttk.Button(
    root,
    text="Login"
)
login_btn.pack(fill="x", padx=20, pady=20)

signup_btn = tk.Button(root, text="Sign up!", command=handle_signup, bg="lightpink", fg="white", font=("Arial", 11, "bold"), padx=15, pady=5, cursor="hand2")

signup_btn.pack(pady=15)

root.mainloop()



