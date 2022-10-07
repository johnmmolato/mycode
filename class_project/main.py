"""John Molato | Class Project
This is an inventory management system application
with the functionality that allows user to search,
create, update, delete"""

# imported libraries and files
from tkinter import *
from tkinter import messagebox
import database


def main():
    """main method creates window"""
    window = Tk()
    app = LoginWindow(window)
    window.mainloop()


class LoginWindow:
    """login class"""

    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry("1600x1000")
        self.master.config(bg="#c1e7f7")
        self.frame = Frame(self.master, bg="#c1e7f7")
        self.frame.pack()

        # label and fields
        self.user_name = StringVar()
        self.user_password = StringVar()
        self.title_label = Label(self.frame, text="Inventory Login System", font="arial 30 bold"
                                 , bg="#c1e7f7", fg="black")
        self.title_label.grid(row=0, column=0, columnspan=4, pady=50)
        self.login_frame = Frame(self.frame, width=1200, height=400, relief="ridge"
                                 , bg="#71c7f5", bd=10)
        self.login_frame.grid(row=1, column=0)
        self.login_btn_frame = Frame(self.frame, width=1200, height=400
                                     , relief="ridge", bg="#71c7f5", bd=10)
        self.login_btn_frame.grid(row=2, column=0)

        self.user_label = Label(self.login_frame, text="User Name"
                                , font="arial 23 bold", bd=10, bg="#71f5f0")
        self.user_label.grid(row=0, column=0)
        self.user_entry = Entry(self.login_frame, font="arial, 23 bold", relief="ridge"
                                , bd=10, textvariable=self.user_name)
        self.user_entry.grid(row=0, column=1, padx=50)
        self.password_label = Label(self.login_frame, text="User Password"
                                    , font="arial 23 bold", bd=10, bg="#71f5f0")
        self.password_label.grid(row=1, column=0)
        self.password_entry = Entry(self.login_frame, font="arial, 23 bold", relief="ridge"
                                    , bd=10, show="*", textvariable=self.user_password)
        self.password_entry.grid(row=1, column=1)

        # login button
        self.login_btn = Button(self.login_btn_frame, relief="raised", text="Login"
                                , width=20, font="arial 23 bold", command=self.login_cred)
        self.login_btn.grid(row=3, column=0)
        # clear button
        self.clear_btn = Button(self.login_btn_frame, text="Clear", width=20
                                , font="arial 23 bold", command=self.clear_cred)
        self.clear_btn.grid(row=3, column=1)
        # exit button
        self.exit_btn = Button(self.login_btn_frame, text="Exit", width=20
                               , font="arial 23 bold", command=self.exit_login)
        self.exit_btn.grid(row=3, column=2)

    def inv_window(self):
        """helper to switch to main window"""
        self.main_window = Toplevel(self.master)
        self.app = Inventory(self.main_window)

    def exit_login(self):
        """exit when user click yes"""
        self.exit_login = messagebox.askyesno("System", "Are you sure you want\
         to exit?", icon="warning")
        if self.exit_login != 0:
            self.master.destroy()
        else:
            self.inv_window

    def clear_cred(self):
        """clear input fields"""
        self.user_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def login_cred(self):
        """check user credential, if correct proceed and if not give warning and clear the fields"""
        usr = (self.user_name.get())
        passwrd = (self.user_password.get())
        if (usr == str(1234)) and (passwrd == str(1234)):
            self.main_window = Toplevel(self.master)
            self.app = Inventory(self.main_window)
        else:
            messagebox.showerror("System", "Need proper credential to enter", icon="warning")
            self.user_entry.delete(0, END)
            self.password_entry.delete(0, END)


class Inventory:
    """inventory class host"""

    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        self.master.geometry("1600x1000")
        self.master.configure(bg="#c1e7f7")
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
                messagebox.showinfo("Success!", "Item successfully added", icon="info")
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
            self.name_entry.delete(0, END)
            self.name_entry.insert(END, selected_item[1])
            self.price_entry.delete(0, END)
            self.price_entry.insert(END, selected_item[2])
            self.qty_entry.delete(0, END)
            self.qty_entry.insert(END, selected_item[3])
            self.purch_date_entry.delete(0, END)
            self.purch_date_entry.insert(END, selected_item[4])
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
        database.update(selected_item[0], self.name_text.get()
                        , self.price_text.get(), self.qty_text.get(), self.purch_date_text.get())
        self.list_all()

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
        self.list_btn = Button(self.master, text="List all", fg="blue"
                               , width=10, command=self.list_all)
        self.list_btn.grid(row=2, column=3)
        self.search_btn = Button(self.master, text="Search", fg="blue"
                                 , width=10, command=self.search_item)
        self.search_btn.grid(row=3, column=3)
        self.add_btn = Button(self.master, text="Add", width=10, fg="blue", command=self.add_item)
        self.add_btn.grid(row=4, column=3)
        self.update_btn = Button(self.master, text="Update", width=10
                                 , fg="blue", command=self.update_item)
        self.update_btn.grid(row=5, column=3)
        self.delete_btn = Button(self.master, text="Delete", width=10
                                 , fg="blue", command=self.delete_item)
        self.delete_btn.grid(row=6, column=3)


if __name__ == '__main__':
    main()
