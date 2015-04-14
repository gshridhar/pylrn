#!/uusr/bin/python
# Author: Shridhar Gadekar
# Date: 12th April 2015
# Purpose: Game with 21 sticks.


def compTurn(playerPick):
   return 5 - playerPick

#def matchstickRemained(sticks):
#   matchsticks -= sticks

#def winCondition(matchsticks):
#   if matchsticks == 1:
#      print "you lost"


def printsticks(stickpicked):
   print "Sticks remained: ", matchsticks, "\t", "| " * stickpicked 

print "\n\n"
print "\t\t\tWelcome to the  GAME_21 .\n\n\t\tInstructions:jn this game, there are 21 sticks available initially."
print "\n\t\tPlayer will pick any number of sticks between 1 to 4."
print "\n\t\tAfter which computer will pick sticks"
print "\n\t\tThis will go on till only one stick remains. Any player forced to pick last stick will loose the game"
print "\n\t\tPlay in such way that your oppenent is forced to pick last stick\n\n\n"

matchsticks = 21

while matchsticks > 0 :
   printsticks(matchsticks)
   playerPick = input("Pick 1 to 4 sticks from stack: ")
   while playerPick > 4:
      playerPick = input("You dumbfuck idiot, didnt i ask you to pick number between 1 to 4 sticks from stack. Do it again: ")
   matchsticks = matchsticks - playerPick
   if matchsticks == 1:
      print "you won"
      break
   print "Now computer will play"
   compPick = compTurn(playerPick)
   matchsticks = matchsticks - compPick 
   if matchsticks == 1:
      print "you lost"
      break
