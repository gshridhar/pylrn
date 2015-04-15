#!/usr/bin/python
# Name: Shridhar Gadekar
# Date: 16March2015
# Purpose: Write a Pig Latin translator program
#
# Pig Latin translator, moves first character of word to the end of word and suffixes it with 'ay'. For example, Greg will become reggay

pyg = 'ay'
original = raw_input("Enter a word: ")
print original

if len(original) > 0 and original.isalpha():
   print "legitimate word"
   word = original.lower()
   first = original[0]
   new_word = word[1:len(word)] + first + pyg
   print new_word
else:
   print "illegitimate word"

