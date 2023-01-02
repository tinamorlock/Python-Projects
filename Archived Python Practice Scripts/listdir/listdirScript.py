
### This program will do the following:
###
### 1. Uses Python3 and the OS Module [DONE]
### 2. Uses the os.listdir() method to iterate through all the files in my path [DONE]
### 3. Uses os.path.join() method to concatenate filename to its path, forming the absolute path [DONE]
### 4. Uses os.getmtime() method to find latest date/time file was created or modified [DONE]
### 5. Prints each file ending with a .TXT file extension and its corresponding mtime to the console [DONE]

import os
import time # needed to convert raw time to date/time

# this is the absolute path to a directory on my icloud drive
# that contains the text file we will list with this program

macPath = '/Users/tinamarie/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Python-Projects/listdir/myDir/'



# this function creates a list from all the files and directories that are in a particular directory

def listFiles (fileDir):
    myFileList = os.listdir(fileDir)
    findTXT(myFileList)


# this function will take the list and find all the .TXT files

def findTXT(list_of_files):
    fileExt = '.txt' # to look for .txt in the list
    txtFiles = [] # where we will add .txt files found in the directory
    x = 0 # counter
    while x < len(list_of_files):
        if fileExt in list_of_files[x]:
            txtFiles.append(list_of_files[x])
            x = x+1
        else:
            x = x+1
    # print statement verified the code works so far
    
    findAbPath(txtFiles)


# this function will join the path created earlier with the filenames in a new list

def findAbPath(list_for_txt_files):
    abPathFileList = []
    x = 0 # counter init
    while x < len(list_for_txt_files):
        abPathFileList.append(macPath+list_for_txt_files[x])
        x = x + 1

    # print statement verified the code worked so far
    getModTime(abPathFileList)


# this function will display the time file was modified

def getModTime (file2check):
    x = 0
    numFiles = len(file2check)

    # lists how many TXT files there are
        
    print('\nThere are {} .TXT files in your directory.'.format(numFiles)) 

    while x < numFiles:


        # prints name of file and time last modified, used time.ctime to convert mtime to something that would make sense to a user
        
        print('\n\nFile #{} \n— {} — \nwas last modified at {}.'.format((x+1), file2check[x],time.ctime(os.path.getmtime(file2check[x]))))
        x = x + 1
    



if __name__ == "__main__":
    listFiles(macPath)
