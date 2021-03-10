# -*- coding: utf-8 -*-
# Python 3.8.6

agesOfStudents = [16, 19, 20, 18, 18, 19, 17, 19]


print("The ages of the students enrolled in this course are :-")

for x in agesOfStudents:
    print(x)

print()


numberOfStudents = len(agesOfStudents)
numberOfEighteenYearOlds = agesOfStudents.count(18)
numberOfNineteenYearOlds = agesOfStudents.count(19)

print("Out of the", numberOfStudents, "students,",
      numberOfEighteenYearOlds, "are eighteen years old and",
      numberOfNineteenYearOlds, "are nineteen years old.")





# /* Trivia
#
#  * len(listName) returns the number of items in a list.
#  * listName.count("Name of Item") returns the number of times an item occurs in a list.
#  * listName.index("Name of Item") returns the index of an item.
#
#  */