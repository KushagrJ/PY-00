# -*- coding: utf-8 -*-
# Python 3.8.6

agesOfStudents = [16, 19, 20, 18, 18, 19, 17, 19]

print("The ages of different students enrolled in this course are :-\n",
      sep = "", end = "")

for x in agesOfStudents:
    print(x, "\n", sep = "", end = "")
print("\n", sep = "", end = "")

totalNumberOfStudents = len(agesOfStudents)
numberOfEighteenYearOlds = agesOfStudents.count(18)
numberOfNineteenYearOlds = agesOfStudents.count(19)

print("Out of ", totalNumberOfStudents, " students, ",
      numberOfEighteenYearOlds, " are eighteen years old and ",
      numberOfNineteenYearOlds, " are nineteen years old.\n",
      sep = "", end = "")



# /* Trivia
#
#  * len(listName) returns the number of items in a list.
#  * listName.count("Name of Item") returns the number of times an item occurs in a list.
#
#  */