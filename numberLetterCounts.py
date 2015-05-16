#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 12th May 2015
# Purpose: Calculate the number letters in one to one thousand number

"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""
import string
dictionary1 = { 1: 'one', 2: 'two', 3:'three', 4:'four',
                5:'five', 6:'six', 7:'seven', 8:'eight',
		9:'nine', 10: 'ten', 11:'elevan', 12:'twelve',
                13:'thirteen', 14:'fourteen', 15:'fifteen',
                16:'sixteen', 17:'seventeen', 18:'eighteen',
		19:'nineteen', }
dictionary2 = {2: 'twenty', 3:'thirty', 4: 'forty', 5:'fifty', 6:'sixty', 7:'seventy',8: 'eighty', 9:'ninety', 0:'zero'}

counter = 0

"""
Following block will count for 01 to 20
"""
for i in range(1,20):
   print dictionary1[i]
   counter += len(dictionary1[i])
emplist = []
"""
Following block will count for 20 to 99
"""
for i in range(20,100):
   for j in range(len(str(i))):
      emplist.append(str(i)[j])
   if emplist[1] == '0':
      print dictionary2[int(emplist[0])], emplist
      counter +=  len(dictionary2[int(emplist[0])])
   else:
      print dictionary2[int(emplist[0])], dictionary1[int(emplist[1])], emplist
      counter += len(dictionary2[int(emplist[0])]) + len(dictionary1[int(emplist[1])])
   emplist = []

"""
Following block will count for 100 to 999
"""
emplist = []
for i in range(100,1000):
   for j in range(len(str(i))):
      emplist.append(str(i)[j])
   if emplist[2] != '0' and emplist[1] >= '2':
      print dictionary1[int(emplist[0])], 'hundred and', dictionary2[int(emplist[1])], dictionary1[int(emplist[2])], emplist
      counter += len(dictionary1[int(emplist[0])]) + 10 + len(dictionary2[int(emplist[1])]) + len(dictionary1[int(emplist[2])])
   elif emplist[1] == '0'and emplist[2] == '0': 
      print dictionary1[int(emplist[0])], 'hundred', emplist
      counter += len(dictionary1[int(emplist[0])]) + len('hundred') 
   elif emplist[1] == '1'and emplist[2] == '0':                   # for 10 
      print dictionary1[int(emplist[0])], 'hundred and', dictionary1[10], emplist
      counter += len(dictionary1[int(emplist[0])]) + 10 + len( dictionary1[10])
   elif emplist[1] != '0'and emplist[2] == '0':                    # for 20s 30s 40s and so on
      print dictionary1[int(emplist[0])], 'hundred and', dictionary2[int(emplist[1])], emplist
      counter += len(dictionary1[int(emplist[0])]) + 10 + len(dictionary2[int(emplist[1])])
   elif emplist[1] >= '0'and emplist[2] != '0':                     # for first 19 numbers  in any hundred
      print dictionary1[int(emplist[0])], 'hundred and', dictionary1[int(emplist[1]+emplist[2])], emplist
      counter += len(dictionary1[int(emplist[0])]) + 10 + len(dictionary1[int(emplist[1]+emplist[2])])
   emplist = []

print "One Thousand" # for thousandth number
counter += len('onethousand')   #  This one is make up for silly mistake of counting that space between two words
print counter
