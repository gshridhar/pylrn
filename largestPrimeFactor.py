#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 19th April 2015
# Purpose: Largest Prime factor of 600851475143
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
Section 1: Defining functions required
"""

def is_prime(number):
   """
      This function will return whether the number is prime or not from list. Here number is a list
   """
   for i in xrange(2,number + 1):
      if number % i == 0 and number != i:
         break
      elif number % i == 0 and number == i:
         primeList.append(i)
   return primeList


def largest_prime(factor):
   """
      This function will return largest prime number from list
   """
   factor.sort()
   return factor[len(factor) - 1]

"""
start of actual calculation operation
"""

targetNum = 600851475143
factorList = []
primeList = []

for i in xrange(2,targetNum):
   if targetNum % i == 0:
      if factorList.count(i) == 0:
         factorList.append(i)
         factorList.append(targetNum / i)
      else:
         break


for i in range(len(factorList)):
    is_prime(factorList[i])

print "\n\n\t\t\tLargest Prime Factor of %d :  %d\n\n" % (targetNum, largest_prime(primeList))
