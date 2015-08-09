#!/usr/bin/python
# Author: shridhar gadekar
# Date: 9th August 2015
# Subject: Escape single quote and double quotes

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

"""
When %r is used then it prints out the raw representation of what I typed, which is goint to include the original escape sequences. Use %s instead. Always remember this: %r is for debugging, %s is for displaying.
"""
print "%r" % tabby_cat
print '%r' % persian_cat
print backslash_cat
print '%r' % fat_cat
print "%r" % fat_cat2
