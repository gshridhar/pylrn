#!/uusr/bin/python
# Author: Shridhar Gadekar
# Date: 20th June 2016
# Purpose: Control flow revision

def clinic():
   print "You have just entered the clinic!"
   print "Do you take the door on the left or the right?"
   answer = raw_input("Type left or right and hit the 'Enter'.").lower()
   if answer == "left" or answer == 'l':
      print "This is the Verbal Abuse Room, you heap of parrot droppings!"
   elif answer == "right" or anser == 'r':
      print "Of course this is the Argument Room, I've told you that already!"
   else:
      print "You didn't pick left or right! Try again."
      clinic()
clinic()

