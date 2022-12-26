# Author: Tina Morlock
# Python: 3.10 
# Assignment: Encapsulation
#
# Requirements:
#
# 1. class makes use of private attribute/function - done
# 2. class makes use of a protected attribute/function
# 3. create an object that makes use of protected and private
# 4. add comments


class Admin:
    def __init__ (self):
        self._first_name = 'Johnny' # private, first name of admin
        self._last_name = 'Depp' # private, last name of admin
        self.__pass = 'dkwjkhfgU83ydj?'
    def update_admin_password (self,password): # function uses protected variable for password to make harder to update
        print('This will update the administrator\'s password on record.') # added a confirm element for double protection
        confirm = input('Are you sure you wish to continue? (y/n) >>> ')
        if confirm == 'y':
            self.__pass = password
            print('Password updated! (Current password: {})'.format(self.__pass)) # prints for verification only
        else:
            print('Alright. Password will not update. (Current password: {})'.format(self.__pass)) # prints for verification only

app_admin = Admin()
app_admin._first_name = 'Stacey'
app_admin.last_name = 'Williams'
app_admin.update_admin_password('rxI873$opP')