#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 12th May 2015
# Purpose: Calculate the lattice paths in 20 x 20 grid


"""
Lattice paths
Problem 15

Starting in the top left corner of a 2x2 grid and only able to move to to the right and down, there are exactly 6 routs to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""
"""
Answer:

Here are some diagrams that represent the possible paths of length 2n from one corner of an n-by-n grid to the opposite corner. The number of paths are the central binomial coefficients

Binomial[2n, n] or (2n)!/(n!)^2,
"""
def factorial(x):
   y = 1
   while x > 1:
      y *= x
      x = x-1

   return y


num1 =  factorial(2 * 20)
num2 = factorial(20)
print num1 / (num2 ** 2)
