"""Add a user helper for main"""
from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

class AddItem(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x600")
        self.title("Add Item")
        self.resizable(False, False)
        self.frame = Frame(self, height=500, bg="#a4dbd9")
        self.frame.pack(fill=X)
        # Box entries for adding item
        # item ID
        self.item_id = Label(self.frame, text="ID: ", font="arial 14 bold", relief="ridge")
        self.item_id.place(x=50, y=50)
        self.item_id_entry = Entry(self.frame, width=30, bd=4)
        self.item_id_entry.place(x=150, y=50)
        # item brand
        self.item_brand = Label(self.frame, text="Brand: ", font="arial 14 bold", relief="ridge")
        self.item_brand.place(x=50, y=100)
        self.item_brand_entry = Entry(self.frame, width=30, bd=4)
        self.item_brand_entry.place(x=150, y=100)
        # item name
        self.item_name = Label(self.frame, text="Name: ", font="arial 14 bold", relief="ridge")
        self.item_name.place(x=50, y=150)
        self.item_name_entry = Entry(self.frame, width=30, bd=4)
        self.item_name_entry.place(x=150, y=150)
        # item quantity
        self.item_qty = Label(self.frame, text="Quantity: ", font="arial 14 bold", relief="ridge")
        self.item_qty.place(x=50, y=200)
        self.item_qty_entry = Entry(self.frame, width=30, bd=4)
        self.item_qty_entry.place(x=150, y=200)
        # add button
        self.button = Button(self.frame, text="Add Item", font="arial 14 bold", relief="raised",
                             fg="#63c3f7", command=self.add_inv)
        self.button.place(x=250, y=250)

    def add_inv(self):
        id = self.item_id_entry.get()
        brand = self.item_brand_entry.get()
        name = self.item_name_entry.get()
        qty = self.item_qty_entry.get()

        if id and brand and name and qty != "":
            try:
                cursor.execute("INSERT INTO 'items' (item_id, item_brand, item_name, item_qty) VALUES (?,?,?,?)",
                               (id, brand, name, qty))
                connection.commit()
                messagebox.showinfo("Successful", "Successfully added to the database", icon="info")
            except Exception as error:
                messagebox.showerror(error, "Failed to add to the database", icon="warning")
        else:
            messagebox.showerror("Fields are required", " Please fill in all fields", icon="warning")
