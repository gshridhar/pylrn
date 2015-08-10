#!/usr/bin/python
# Author: shridhar gadekar
# Date: 11th August 2015
# Subject: Exercises for Functions

# Defining function
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Instead of *args, function could be defined as follows as well
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# With only one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# Without any argument
def print_none():
	print "I got nothin'"

print_two("Shridhar", "Gadekar")
print_two_again("Shridhar", "Gadekar")
print_one("Shridhar")
print_none()
