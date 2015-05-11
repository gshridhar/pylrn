#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 12th May 2015
# Purpose: Calculate the Power digit sum


"""
Power digit sum
Problem 16

2** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 **1000?

"""

power = 1000
num = 2
sum = 0
for i in range(len(str(num ** power))):
   sum += int(str(num ** power)[i])

print sum
