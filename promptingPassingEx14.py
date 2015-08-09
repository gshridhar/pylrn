#!/usr/bin/python
# Author: shridhar gadekar
# Date: 10th August 2015
# Subject: Exercises for prompting and passing

from sys import argv

# Along with script, just provide your username
script, user_name, OS = argv
prompt = '> '

# printing the first lines with arguments provided at the command line.
print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "\n"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
And best part is you are running %r on it.
""" % (likes, lives, computer, OS)
