#! /usr/bin/python
# Author: Shridhar Gadekar
# Date: 11th August 2015
# Subject: More on functions

# defining a function 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

# calling a function with directly fed values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# declaring and storing variables with values
print "We can just give the function numbers directly:"
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# calling a function with values stored in variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# calling a function with mathematical expression as value
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# calling a function as mathematical expression having numbers and previously defined variables as argument
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

