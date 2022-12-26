
#
# Python Ver:   3.11.1
#
# Author:       Tina Morlock, based on Daniel Christie's phonebook app
#
# Purpose:      Student tracking app to submit the following information:
#               first name, last name, ph #, email, current course, submit button,
#               delete button, and can display the list of students.
#
# Tested OS:  This code was written and tested to work with Windows.

# This file runs/controls the parent window for the GUI and sets up some basic design parameters for the main window.


from tkinter import *
import tkinter as tk

# importing other modules so we have access to them

import student_tracking_gui
import student_tracking_func


# this opens the main gui window

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # defines master configuration

        self.master = master
        self.master.minsize(700, 400)            # (Width, Height)
        self.master.maxsize(700, 400)

        # centers app on screen

        student_tracking_func.center_window(self, 500, 300)
        self.master.title("Student Tracking")
        self.master.configure(bg="lightgray")

        # verifies user wants to quit. will confirm. 

        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master

        # functionality loads from an outside python script to simplify the current file

        student_tracking_gui.load_gui(self)
        
        # menu dropdown object
        # menu that that should appear at top of window

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: student_tracking_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Student Tracker")
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
