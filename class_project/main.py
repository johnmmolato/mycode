#!/usr/bin/env python3
"""JMolato | Python class project
   Inventory Management System"""

# Import
from tkinter import *


class Main():
    def __init__(self, master):
        self.master = master

        # mainframe
        main_frame = Frame(self.master)
        main_frame.pack()
        # top frame
        top_frame = Frame(main_frame, width=1200, height=90, bg="#c1f7ef", relief=RIDGE, borderwidth=2)
        top_frame.pack(side=TOP, fill=X)
        # center frame
        center_frame = Frame(main_frame, width=1200, height=710, bg="#c1e7f7", relief=SUNKEN, borderwidth=2)
        center_frame.pack(side=TOP)
        # add user button
        self.iconuser = PhotoImage(file="icons/adduser.png")
        self.btnuser = Button(top_frame, text="Add User", font="arial 12 bold", padx=20)
        self.btnuser.configure(image=self.iconuser, compound=LEFT)
        self.btnuser.pack(side=LEFT, padx=20)
        # search button
        self.iconsearch = PhotoImage(file="icons/search.png")
        self.btnsearch = Button(top_frame, text="Search", font="arial 12 bold", padx=20, pady=6)
        self.btnsearch.configure(image=self.iconsearch, compound=LEFT)
        self.btnsearch.pack(side=LEFT, padx=20)


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
