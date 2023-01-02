# Author: Tina Morlock
# Python: 3.10
#
# Purpose: 
#
# Creates abstract method and a regular method.
#
# Requires:
#
# 1. one abstract method
# 2. one regular method
# 3. child class that defines implementation of parent method
# 4. create object that uses both parent and child classes
# 5. add comments

from abc import ABC, abstractmethod

class Expense(ABC):
    def expense_amt(self,amount_of_expense):                                # displays expense amount
        print('Your expense amount: ', amount_of_expense)
    @abstractmethod
    def expense_type(self, amount_of_expense):                              # parent abstract method
        pass

class Website(Expense):
    def expense_type(self, amount_of_expense):                                                  # displays expense amount and category of expense
        print('Your website expense added in the amount of {}.'.format(amount_of_expense))      # child method from abstract parent

dec_web = Website()
dec_web.expense_amt('$200')
dec_web.expense_type('$200')

# Output Received:
# 
# Your expense amount:  $200
# Your website expense added in the amount of $200.