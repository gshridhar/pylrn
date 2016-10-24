#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 21 Oct 2016
# Getting started with variables in classes and instance variables

class Employee:

   raise_amount = 1.04

   def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + "." + last + "@company.com"

   def fullname(self):
      return "{} {}".format(self.first, self.last)

   def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)
#      self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("Shridhar", "Gadekar", 3435554)	
emp_2 = Employee("Test", "User", 4435554)	


#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)

print(emp_2.raise_amount)
