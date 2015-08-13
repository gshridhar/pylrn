#!/usr/bin/python
# Author: shridhar gadekar
# Date: 14th August 2015
# Subject: Exercises for "while" loop

def myfunction(limit,incrementer):
   i = 0
   numbers = []

   while i < limit:
      print "At the top i is %d" % i
      numbers.append(i)

      i = i+ incrementer
      print "Numbers now: ", numbers
      print "At the bottom i is %d" % i

   print "The numbers: "
   return numbers

callnumber = myfunction(9,2)

for num in callnumber:
   print num
