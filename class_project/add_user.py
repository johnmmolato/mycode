"""Add a user helper for main"""
from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

class AddUser(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x600")
        self.title("Add User")
        self.resizable(False, False)
        self.frame = Frame(self, height=500, bg="#a4dbd9")
        self.frame.pack(fill=X)
        # Box entries for adding user
        # first name
        self.first_name = Label(self.frame, text="First Name: ", font="arial 14 bold", relief="ridge")
        self.first_name.place(x=50, y=50)
        self.f_name_entry = Entry(self.frame, width=30, bd=4)
        self.f_name_entry.place(x=150, y=50)
        # last name
        self.last_name = Label(self.frame, text="Last Name: ", font="arial 14 bold", relief="ridge")
        self.last_name.place(x=50, y=100)
        self.l_name_entry = Entry(self.frame, width=30, bd=4)
        self.l_name_entry.place(x=150, y=100)
        # email
        self.email = Label(self.frame, text="Email: ", font="arial 14 bold", relief="ridge")
        self.email.place(x=50, y=150)
        self.email_entry = Entry(self.frame, width=30, bd=4)
        self.email_entry.place(x=150, y=150)
        # phone number
        self.phone_number = Label(self.frame, text="Phone #: ", font="arial 14 bold", relief="ridge")
        self.phone_number.place(x=50, y=200)
        self.phone_number_entry = Entry(self.frame, width=30, bd=4)
        self.phone_number_entry.place(x=150, y=200)
        # add button
        self.button = Button(self.frame, text="Add User", font="arial 14 bold", relief="raised",
                             fg="#63c3f7", command=self.add_user)
        self.button.place(x=250, y=250)

    def add_user(self):
        first_name = self.f_name_entry.get()
        last_name = self.l_name_entry.get()
        email = self.email_entry.get()
        phone_number = self.phone_number_entry.get()

        if first_name and last_name and email and phone_number != "":
            try:
                cursor.execute("INSERT INTO 'users' (first_name, last_name, email, phone_number) VALUES (?,?,?,?)",
                               (first_name, last_name, email, phone_number))
                connection.commit()
                messagebox.showinfo("Successful", "Successfully added to the database", icon="info")
            except Exception as error:
                messagebox.showerror(error, "Failed to add to the database", icon="warning")
        else:
            messagebox.showerror("Fields are required", " Please fill in all fields", icon="warning")
