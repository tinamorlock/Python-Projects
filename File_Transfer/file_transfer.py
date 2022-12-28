import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

# this app will look at a directory and see if any changes have been made to files in the past 24 hours.
# If so, it will transfer the files to a customer directory.

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        # directory to check

        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = Entry(width=75)

        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # where we will move the files if necessary

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15,10))

        self.destination_dir = Entry(width=75)

        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))

        # performs the transfer

        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # closes the program

        self.exit_btn = Button(text="Exit", width=20, comman=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):                                            # allows the user to select the source directory
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):                                              # allows the user to select the destination directory
        selectDestDir = tkinter.filedialog.askdirectory()

        self.destination_dir.delete(0, END)

        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):                                        # main method that determines whether a file should be transferred
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        for i in source_files:                                      # checks each file in the directory, if there are any
            current=datetime.now()
            file_time = datetime.fromtimestamp(os.path.getmtime(source + '/' + i))          # getting the file last updated time/date
            past = current - timedelta(hours=24)                                            # this will be used to check if we should transfer
            
            if past < file_time:                            
                shutil.move(source + '/' + i, destination)                                  # transfers the file in the current loop if meets condition
                print(i + ' was successfully transferred.')
            else:
                print('{} hasn\'t been edited in the past 24 hours.'.format(i))             # if it doesn't transfer, sends a msg to the console

    def exit_program(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
   
