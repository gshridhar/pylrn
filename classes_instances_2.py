#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 21 Oct 2016
# Getting started with OOP concepts (classes) Importance of __self__method


class Employee:

   def __init__(self, first, last, pay):
      self.first = first
      self.last  = last 
      self.pay = pay
      self.email = first + "." + last + "@company.com"



emp_1 = Employee("Shridhar", "Gadekar", 50000)
emp_2 = Employee("Test", "User", 12344)

print(emp_1.first)
print(emp_2.first)
