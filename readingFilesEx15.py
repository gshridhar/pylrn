#!/usr/bin/python
# Author: shridhar gadekar
# Date: 11th August 2015
# Subject: Exercises for reading files

# Following line will import argv from sys module
from sys import argv

# Following line will get and assign arguments from command line
script, filename = argv

# Following line will open and store the file provided at command prompt in to a variable
txt = open(filename)

# Following line will print name of file entered at command prompt
print "Here's your file %r:" % filename
# Following line will print all contents of file stored in txt
print txt.read()

# Following line will request name of file from user
print "Type the filename again:"
# Following line will read  filename n assign a variable to that file name 
file_again = raw_input("> ")

# Following line will open and store  file contents from file_again variable
txt_again = open(file_again)
# Following line will print the stored contents from txt_again
print txt_again.read()

txt.close()
txt_again.close()
