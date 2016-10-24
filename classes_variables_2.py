#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 21 Oct 2016
# Getting started with variables in classes and instance variables

class Employee:
 
   num_of_emp = 0
   raise_amount = 1.04

   def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + "." + last + "@company.com"

      Employee.num_of_emp += 1

   def fullname(self):
      return '{} {}'.format(self.first, self.last)

   def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Shridhar", "Gadekar", 43434343)
emp_2 = Employee("Omi", "ekar", 3434343)


print(Employee.num_of_emp)

