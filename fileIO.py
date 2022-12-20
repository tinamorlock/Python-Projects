import os


fName = 'Hello.txt'

fPath = '~/Desktop/A/'

abPath = os.path.join(fPath,fName)

print(abPath)
