#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 26th April 2015
# Purpose: sum of prime numbers in 2million

"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
def is_prime(number):
   for i in range(2, int(number ** 0.5) + 1):
      if number % i == 0:
         break
   else:
         return number

sum = 5
for num in xrange(4,2000000):
   if is_prime(num) == num:
      sum += num

