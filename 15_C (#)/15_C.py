# -*- coding: utf-8 -*-
# Python 3.8.6

def main():

    numberOfStudents = get_the_number_of_students_from_user()

    if numberOfStudents > 0:
        listOfNames = get_the_list_of_names_from_user(numberOfStudents)
        marksObtained = get_the_list_of_marks_obtained_from_user(listOfNames)
        print_the_names_after_sorting(numberOfStudents, listOfNames)
        print_the_marks_obtained_after_sorting(numberOfStudents, marksObtained)
    else:
        print("The number of students should be greater than 0!")



def get_the_number_of_students_from_user():

    numberOfStudents = int(input("Enter the number of students enrolled in "
                                 "this course: "))

    print()

    return numberOfStudents



def get_the_list_of_names_from_user(numberOfStudents):

    listOfNames = []

    for x in range(numberOfStudents):
        print("Enter the name of student no. ", x+1, ": ", sep = "", end = "")
        dummyVariable1 = input()
        listOfNames.append(dummyVariable1)

    print()

    return listOfNames



def get_the_list_of_marks_obtained_from_user(listOfNames):

    marksObtained = []

    for y in listOfNames:
        print("Enter the marks obtained by ", y, ": ", sep = "", end = "")
        dummyVariable2 = int(input())
        marksObtained.append(dummyVariable2)

    print()

    return marksObtained



def print_the_names_after_sorting(numberOfStudents, listOfNames):


    print("The name(s) of the student(s) enrolled in this course is(are) :-")


    listOfNames.sort()

    # To print the list like a, b, c & d instead of like ['a', 'b', 'c', 'd'].
    for z in range(numberOfStudents):
        if z+1 == numberOfStudents:
            print(listOfNames[z], end = " ")
        elif z+2 == numberOfStudents:
            print(listOfNames[z], end = " & ")
        else:
            print(listOfNames[z], end = ", ")

    print("(in ascending alphabetical order).")


    listOfNames.reverse()

    # To print the list like a, b, c & d instead of like ['a', 'b', 'c', 'd'].
    for w in range(numberOfStudents):
        if w+1 == numberOfStudents:
            print(listOfNames[w], end = " ")
        elif w+2 == numberOfStudents:
            print(listOfNames[w], end = " & ")
        else:
            print(listOfNames[w], end = ", ")

    print("(in descending alphabetical order).\n")



def print_the_marks_obtained_after_sorting(numberOfStudents, marksObtained):


    print("The marks obtained by the student(s) enrolled in this course",
          "is(are) :-")


    marksObtained.sort()

    # To print the list like 1, 2, 3 & 4 instead of like [1, 2, 3, 4].
    for u in range(numberOfStudents):
        if u+1 == numberOfStudents:
            print(marksObtained[u], end = " ")
        elif u+2 == numberOfStudents:
            print(marksObtained[u], end = " & ")
        else:
            print(marksObtained[u], end = ", ")

    print("(in ascending order).")


    marksObtained.reverse()

    # To print the list like 1, 2, 3 & 4 instead of like [1, 2, 3, 4].
    for v in range(numberOfStudents):
        if v+1 == numberOfStudents:
            print(marksObtained[v], end = " ")
        elif v+2 == numberOfStudents:
            print(marksObtained[v], end = " & ")
        else:
            print(marksObtained[v], end = ", ")

    print("(in descending order).")



main()





# /* Trivia
#
#  * numberOfStudents = get_the_number_of_students_from_user() creates a local
#    variable called numberOfStudents inside the main() function, 'runs' the
#    function called get_the_number_of_students_from_user() and assign's
#    get_the_number_of_students_from_user()'s return value to the local variable
#    numberOfStudents.
#    [Similarly for others]
#  * numberOfStudents in
#    'listOfNames = get_the_list_of_names_from_user(numberOfStudents)' and
#    numberOfStudents in
#    'def get_the_list_of_names_from_user(numberOfStudents):' are different from
#    each other. They are just named the same to avoid confusion.
#    [Similarly for others]
#
#  */