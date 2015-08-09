#!/usr/bin/python
# Author: shridhar gadekar
# Date: 9th August 2015
# Subject: Exercises for string manipulation

# Defining a string 
formatter = "%r %r %r %r"

# printing string with number
print formatter % (1, 2, 3, 4)
# printing string with string
print formatter % ("one", "two", "three", "four")
# printing string with Python keywords 
print formatter % (True, False, False, True)
# printing string having formatter as string itself
print formatter % (formatter, formatter, formatter, formatter)
# printing string with multple sentences in one line. These lines in code are broke into multiple lines
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"so I said goodnight."
)
