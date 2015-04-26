#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 26th April 2015
# Purpose: Special Pythagorian Triplet

"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for fnum in range(2,1000):
   for snum in range(2,1000):
      product = (((fnum ** 2) + (snum**2 )) ** 0.5)
      if product == int(product) and fnum + snum + product == 1000:
         print fnum*snum*int(product)
         
