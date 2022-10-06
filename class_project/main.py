"""John Molato | Class Project
This is an inventory management system application
with the functionality that allows user to search,
create, update, delete"""

# imported libraries and files
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database


class Inventory:
    def __init__(self, master):
        self.master = master
        self.widget()
        self.list_all()

    def list_all(self):
        """grabbing data from the database and list it"""
        self.list_area.delete(0, END)
        for item in database.view():
            self.list_area.insert(END, item)

    def search_item(self):
        """search item from the database"""
        self.list_area.delete(0, END)

        for item in database.search(self.name_text.get(), self.price_text.get(),
                                    self.qty_text.get(), self.purch_date_text.get()):
            self.list_area.insert(END, item)

        self.clear_field()

    def add_item(self):
        """add item to the list"""
        name = self.name_text.get()
        price = self.price_text.get()
        qty = self.qty_text.get()
        purch_date = self.purch_date_text.get()

        if name and price and qty and purch_date != "":
            try:
                database.insert(name, price, qty, purch_date)
                self.list_area.delete(0, END)
                self.list_area.insert(END, (name, price, qty, purch_date))
                self.clear_field()
                messagebox.showinfo("Success!", "Item is successfully added to the database", icon="info")
            except Exception as err:
                messagebox.showerror(err, "Failed to add to the database", icon="warning")
        else:
            messagebox.showerror("Fields are required", "Please fill in all fields", icon="warning")

    def clear_field(self):
        """clear the input fields"""
        self.name_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.qty_entry.delete(0, END)
        self.purch_date_entry.delete(0, END)

    def get_selected_item(self, event):
        """return the selected item chosen by the user"""
        try:
            global selected_item
            index = self.list_area.curselection()[0]
            selected_item = self.list_area.get(index)
            return selected_item
        except IndexError:
            pass

    def delete_item(self):
        """delete the selected item"""
        try:
            database.delete(selected_item[0])
            self.list_all()
        except:
            pass

    def update_item(self):
        """update field selected by the user"""
        try:
            database.update(selected_item[0], self.name_text.get(), self.price_text.get(), self.qty_text.get(),
                            self.purch_date_text.get())
            self.list_all()
        except:
            pass

    def widget(self):
        """different widget component for the app"""
        # name
        self.name = Label(self.master, text="Name")
        self.name.grid(row=0, column=0)
        self.name_text = StringVar()
        self.name_entry = Entry(self.master, textvariable=self.name_text)
        self.name_entry.grid(row=0, column=1)

        # price
        self.price = Label(self.master, text="Price")
        self.price.grid(row=0, column=2)
        self.price_text = StringVar()
        self.price_entry = Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=0, column=3)

        # quantity
        self.qty = Label(self.master, text="Quantity")
        self.qty.grid(row=1, column=0)
        self.qty_text = StringVar()
        self.qty_entry = Entry(self.master, textvariable=self.qty_text)
        self.qty_entry.grid(row=1, column=1)

        # purchase date
        self.purch_date = Label(self.master, text="Purchase Date")
        self.purch_date.grid(row=1, column=2)
        self.purch_date_text = StringVar()
        self.purch_date_entry = Entry(self.master, textvariable=self.purch_date_text)
        self.purch_date_entry.grid(row=1, column=3)

        # list area
        self.list_area = Listbox(self.master, height=20, width=50)
        self.list_area.grid(row=2, column=0, rowspan=6, columnspan=2)

        # scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=2, column=2, rowspan=6)
        self.list_area.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.list_area.yview)
        self.list_area.bind('<<ListboxSelect>>', self.get_selected_item)

        # buttons
        self.list_btn = Button(self.master, text="List all", fg="blue", bg="blue", relief="raised", width=10,
                               command=self.list_all)
        self.list_btn.grid(row=2, column=3)
        self.search_btn = Button(self.master, text="Search", width=10, command=self.search_item)
        self.search_btn.grid(row=3, column=3)
        self.add_btn = Button(self.master, text="Add", width=10, command=self.add_item)
        self.add_btn.grid(row=4, column=3)
        self.update_btn = Button(self.master, text="Update", width=10, command=self.update_item)
        self.update_btn.grid(row=5, column=3)
        self.delete_btn = Button(self.master, text="Delete", width=10, command=self.delete_item)
        self.delete_btn.grid(row=6, column=3)


def main():
    window = Tk()
    app = Inventory(window)
    window.title("Inventory Management System")
    window.geometry("800x400")
    window.configure(bg="#c1e7f7")
    window.mainloop()


if __name__ == '__main__':
    main()
