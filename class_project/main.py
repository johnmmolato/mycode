#!/usr/bin/env python3
"""JMolato | Python class project
   Inventory Management System"""

# Import
from tkinter import *
from class_project import add_user
from class_project import add_item


class Main:
    def __init__(self, master):
        self.master = master

        # mainframe
        main_frame = Frame(self.master)
        main_frame.pack()
        # top frame
        top_frame = Frame(main_frame, width=1200, height=90, bg="#c1f7ef", relief='ridge', borderwidth=2)
        top_frame.pack(side=TOP, fill=X)
        # center frame
        center_frame = Frame(main_frame, width=1200, height=710, bg="#c1e7f7", relief='ridge', borderwidth=2)
        center_frame.pack(side=TOP)
        # add user button
        self.iconuser = PhotoImage(file="icons/adduser.png")
        self.btnuser = Button(top_frame, text="Add User", font="arial 14 bold", padx=20, command=self.add_user)
        self.btnuser.configure(image=self.iconuser, compound=LEFT)
        self.btnuser.pack(side=LEFT, padx=20)
        # inventory button
        self.iconsearch = PhotoImage(file="icons/search.png")
        self.btnsearch = Button(top_frame, text="Inventory", font="arial 14 bold", padx=20, pady=6,
                                command=self.add_inv)
        self.btnsearch.configure(image=self.iconsearch, compound=LEFT)
        self.btnsearch.pack(side=LEFT, padx=50)
        # search bar
        search_entry = Entry(top_frame, width=30, bd=4)
        search_entry.pack(side=LEFT, padx=10)
        search_button = Button(top_frame, text="Search", font="arial 14 bold", bg="#2488ff", width=10, height=2,
                               command=self.search_inv)
        search_button.pack(side=LEFT)
        # inventory list
        self.list_inv = Listbox(width=600, height=150, bd=10, font="arial 14 bold")
        self.scroll_bar = Scrollbar(orient=VERTICAL)
        #self.list_inv.grid(row=0, column=0, sticky=N)
        self.scroll_bar.config(command=self.list_inv.yview())
        self.list_inv.config(yscrollcommand=self.scroll_bar.set)

    def add_user(self):
        user_add = add_user.AddUser()

    def add_inv(self):
        inventory = add_item.AddItem()

    def search_inv(self):
        print("search inventory")

    def search_bar(self):
        print("")

    def list_inventory(self):
        print("Listing inventory")

def main():
    # create a new viewing window
    window = Tk()
    app = Main(window)
    window_title = "Inventory Management System"
    # set title and viewing window
    window.title(window_title)
    window.geometry("1200x800")
    # start window
    window.mainloop()


if __name__ == '__main__':
    main()
