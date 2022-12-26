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

# This file includes all the functions the GUI needs to run in order to make the student tracker work.

import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

# our modules to import

import student_tracking_main
import student_tracking_gui


def center_window(self, w, h):

    # get user's screen width and height

    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    # calculate x and y coordinates to paint the app centered on the user's screen

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
# originally wouldn't run without importing messagebox specifically

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):

        # This closes app

        self.master.destroy()
        os._exit(0)


#=========================================================
def create_db(self):

    # create the student tracking database here if it doesn't already exist

    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student_tracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            student_first TEXT, \
            student_last TEXT, \
            student_full_name TEXT, \
            student_phone TEXT, \
            student_email TEXT, \
            student_current_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

# function adds some dummy info so there is something already in the database when the user first runs it

def first_run(self):
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_student_tracker (student_first,student_last,student_full_name,student_phone,student_email,student_current_course) VALUES (?,?,?,?,?,?)""", ('Alexz','North','Alexz North','808-792-1100','alexz@northink.com','English 101'))
            conn.commit()
    conn.close()

# counting how many records exist in the student tracker table

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
    count = cur.fetchone()[0]
    return cur,count
  
# when the user selects a student, it displays their info on the screen

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT student_first,student_last,student_phone,student_email,student_current_course FROM tbl_student_tracker WHERE student_full_name = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0, END)
            self.txt_course.insert(0, data[4])

# adding an entry into the database

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normailzed names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    var_course = self.txt_course.get().strip()
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('student_tracking.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existence of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(student_full_name) FROM tbl_student_tracker WHERE student_full_name = '{}'""".format(var_fullname))#,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_student_tracker (student_first,student_last,student_full_name,student_phone,student_email,student_current_course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) 
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) 
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

  # have verified the delete button works like it should
  # this will delete a record, as long as it's not the last one there
  # also verifies if the user really means to delete user      

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('student_tracking.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student_tracker WHERE student_full_name = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

# when deleted, we're going to refresh what's displayed in the GUI

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    

def onRefresh(self):

    # puts the info from the database on the GUI
   
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT student_full_name FROM tbl_student_tracker""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be alowed to update changes for phone, emails, and the current course.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect('student_tracking.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(student_phone) FROM tbl_student_tracker WHERE student_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(student_email) FROM tbl_student_tracker WHERE student_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute(
                """SELECT COUNT(student_current_course) FROM tbl_student_tracker WHERE student_current_course = '{}'""".format(var_course))
            count3 = cur.fetchone()[0]
            print(count3)
            if count == 0 or count2 == 0 or count3 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}), ({}), and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_course,var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('student_tracking.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_student_tracker SET student_phone = '{0}',student_email = '{1}',student_current_course = '{2}' WHERE student_full_name = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","({}), ({}), and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email, var_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone, email, or current course information.")
    onClear(self)


if __name__ == "__main__":
    pass                        # file will not run on its own.
