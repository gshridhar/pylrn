#!/usr/bin/python
# Author: Shridhar Gadekar
# Date: 21 March2015
# Purpose: Create a grade book of class students ( check the average of class and assign grade to the class accordingly )

# To get or check the output of this program, define a list containing three students mentioned in program
# Create a dictionary for each student such as follows:

lloyd = {

    "name": "Lloyd",

    "homework": [90.0, 97.0, 75.0, 92.0],

    "quizzes": [88.0, 40.0, 94.0],

    "tests": [75.0, 90.0]

}

alice = {

    "name": "Alice",

    "homework": [100.0, 92.0, 98.0, 100.0],

    "quizzes": [82.0, 83.0, 91.0],

    "tests": [89.0, 97.0]

}

tyler = {

    "name": "Tyler",

    "homework": [0.0, 87.0, 75.0, 22.0],

    "quizzes": [0.0, 75.0, 78.0],

    "tests": [100.0, 100.0]

}


students = [lloyd, alice, tyler]


## write a function to calculate average from list of number. it has nothin to do with above  data of students at this stage
def average(number):
   total = 0
   total = sum(number)
   return (float(total) / len(number))

"""
Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.

    Define a function called get_average that takes one argument called student.
    Make a variable homework that stores the average() of student["homework"].
    Repeat step 2 for "quizzes" and "tests".
    Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.
"""
def get_average(student):
   homework = average(student["homework"])
   quizzes = average(student["quizzes"])
   tests = average(student["tests"])
   total = 0
   total = homework * (10.0 / 100) + quizzes * (30.0 / 100) + tests * (60.0 / 100)
   return total
get_average(alice)


"""

    Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.

    Inside your function, test score using a chain of if: / elif: / else: statements, like so:

    If score is 90 or above: return "A"
    Else if score is 80 or above: return "B"
    Else if score is 70 or above: return "C"
    Else if score is 60 or above: return "D"
    Otherwise: return "F"

    Finally, test your function! Call your get_letter_grade function with the result of get_average(lloyd). Print the resulting letter grade.
"""

""" Following function will check the average of student. Based on this, it will assign grades, rest description is available at top of definition of function """
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"


def get_class_average(students):
   """ This function will return average of all students in the class.
   Instructions: 
   1.  Define a function called get_class_average that has one argument students. You can expect students to be a list containing your three students.
   2.  First, make an empty list called results.
   3.  For each student item in the class list, calculate get_average(student) and then call results.append() with that result.
   4.  Finally, return the result of calling average() with results."""
   results = []
   for student in students:
      results.append(get_average(student))

   print average(results)      # to print average of class
   return average(results)

# To calculate and print grade of class, calling following function
print get_letter_grade(get_class_average(students))  


""" END OF PROGRAME """
