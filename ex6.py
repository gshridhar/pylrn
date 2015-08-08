#!/usr/bin/python
# Author: shridhar gadekar
# Date: 8th August 2015
# Subject: Strings

# variable declaration
x = "There are %d types of people" % 10
binary = "Binary"
do_not = "don't"
y = "Those who know %s and those who %s" %(binary, do_not)

# print variables
print x
print y

# printing the sentence with string
print "I said:%r." % x
print "I also said:%r." % y

# Define and Assign value for variable 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! % r"

# print string with variable 
print joke_evaluation % hilarious

# Defining string
w = "This is the left side of ..."
e = "a string with a right side."

# printing of strings and concatenation
print w + e 
