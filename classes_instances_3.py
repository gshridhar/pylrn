#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 21 Oct 2016
# Getting started with OOP concepts (classes)

class Employee:

   def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + "." + last + '@company.com'

   def fullname(self):
      return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Shridhar", "Gadekar", 50000)
emp_2 = Employee("User", "Test", 30000)
print(emp_1.email)
print(emp_2.pay)

print(emp_2.fullname())

print emp_1.fullname()
print(Employee.fullname(emp_1))
