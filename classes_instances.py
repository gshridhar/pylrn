#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 21 Oct 2016
# Getting started with OOP concepts (classes)

class Employee:
   pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = "Shridhar"
emp_1.last = "Gadekar"
emp_1.email = "shridhar@email.com"
emp_1.pay = 5999999


emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "User@email.com"
emp_2.pay = 999999


print(emp_1.pay)
print(emp_2.pay)
