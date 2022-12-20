#############################################################################################
### db_assignment.py
###
### iterates through a list of filenames and adds the .txt files to its own database, 
### then prints the results
###
### Using Python 3.11.0
###
### Author: Tina Morlock
###
### Date: 12.20.22
#############################################################################################
### REQUIRES:
###
### 1) Use Python3 and sqlite3 module [DONE]
### 2) DB requires 2 fields:
###     field with auto-increment primary integer and
###     a field with the data type "string" [DONE]
### 3) Read from supplied list of filenames and determine
###     only the files that end with .txt [DONE]
###         fileList = ('information.docx', 'Hello.txt', 'myImage.png',
###         'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jgp')
### 4) Script should add filenames from the list that end with .txt
###         to the database? [DONE]
### 5) Print .txt files to the console [DONE]
### 6) Comments throughout your code [DONE]
#############################################################################################



import sqlite3

## this is the file list that needs to be iterated through

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jgp')

# creates the database with two fields and the tables needed

def createDB():

    # initializing connect variable for the DB file

    conn = sqlite3.connect('fileDB2.db')

    with conn:
        cur = conn.cursor()

        # creating table and fields if they do not already exist
        # fileName will hold any .txt files found in the list
        
        cur.execute('CREATE TABLE IF NOT EXISTS TXTfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fileName TEXT \
            )')
        conn.commit()
    conn.close()


# iterates through fileList to find the .txt files

def findTXT(forTXTfiles):
    fileExt = '.txt' # to look for .txt in the list
    txtFiles = [] # where we will add .txt files found in the list
    x = 0 # counter for loop
    while x < len(forTXTfiles):
        if fileExt in forTXTfiles[x]:
            txtFiles.append(forTXTfiles[x]) # add to list so we can add to DB later
            x = x + 1
        else: # if not .txt
            x = x + 1 # just increment so we can check the next one
    add2DB(txtFiles)


# takes the list of .txt files and adds them into the database

def add2DB(txt2DB):
    x = 0 # counter for loop
    numTXT = len(txt2DB) # this defines how many items will be added to the database

    # connects to db

    conn = sqlite3.connect('fileDB2.db')

    # while loop will execute as long as there's another .txt file to add to the database

    while x < numTXT:
        tempTXT = txt2DB[x]
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO TXTfiles (fileName) VALUES (?)', \
                        (tempTXT,)) # adds to database
            conn.commit()
            x = x + 1
    conn.close()
    
# queries the database and prints results

def printQuery():
    conn = sqlite3.connect('fileDB2.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT fileName from TXTfiles')
        varFiles = cur.fetchall()
        msg = ''
        for item in varFiles:
            msg = msg + '\nFile Name: {}'.format(item[0]) # added index to strip away tuple formatting
        print('\nI found the following .TXT files:')
        print(msg)
    conn.close()

if __name__ == "__main__":
    createDB()
    findTXT(fileList)
    printQuery()
