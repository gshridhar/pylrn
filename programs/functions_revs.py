#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 23rd June 2016
# Purpose: Revision of functions

def clinic():
   print "You have just entered the clinic!"
   print "Do you take the door on the left or the right?"
   answer = raw_input("Type left or right and hit 'Enter'.").lower()
   if answer == 'left' or answer == 'l':
      print "This is the Verbal abuse Room, you heap of parrot droppings!"
   elif answer == 'right' or answer == 'r':
      print "Of course this is the Argument Room, I've told you that already!"
   else:
      print "You didn't pick left or right! Try again."
      clinic()

clinic()
