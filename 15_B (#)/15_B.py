# -*- coding: utf-8 -*-
# Python 3.8.6

def main():

    get_the_number_of_students_from_user()

    if NUMBER_OF_STUDENTS > 0:
        get_the_list_of_names_from_user()
        get_the_list_of_marks_obtained_from_user()
        print_the_names_after_sorting()
        print_the_marks_obtained_after_sorting()
    else:
        print("The number of students should be greater than 0!")



def get_the_number_of_students_from_user():

    global NUMBER_OF_STUDENTS

    NUMBER_OF_STUDENTS = int(input("Enter the number of students enrolled in "
                                   "this course: "))

    print()



def get_the_list_of_names_from_user():

    global LIST_OF_NAMES

    LIST_OF_NAMES = []

    for x in range(NUMBER_OF_STUDENTS):
        print("Enter the name of student no. ", x+1, ": ", sep = "", end = "")
        dummyVariable1 = input()
        LIST_OF_NAMES.append(dummyVariable1)

    print()



def get_the_list_of_marks_obtained_from_user():

    global MARKS_OBTAINED

    MARKS_OBTAINED = []

    for y in LIST_OF_NAMES:
        print("Enter the marks obtained by ", y, ": ", sep = "", end = "")
        dummyVariable2 = int(input())
        MARKS_OBTAINED.append(dummyVariable2)

    print()



def print_the_names_after_sorting():


    # To let LIST_OF_NAMES stay constant.
    listOfNames = LIST_OF_NAMES


    print("The name(s) of the student(s) enrolled in this course is(are) :-")


    listOfNames.sort()

    # To print the list like a, b, c & d instead of like ['a', 'b', 'c', 'd'].
    for z in range(NUMBER_OF_STUDENTS):
        if z+1 == NUMBER_OF_STUDENTS:
            print(listOfNames[z], end = " ")
        elif z+2 == NUMBER_OF_STUDENTS:
            print(listOfNames[z], end = " & ")
        else:
            print(listOfNames[z], end = ", ")

    print("(in ascending alphabetical order).")


    listOfNames.reverse()

    # To print the list like a, b, c & d instead of like ['a', 'b', 'c', 'd'].
    for w in range(NUMBER_OF_STUDENTS):
        if w+1 == NUMBER_OF_STUDENTS:
            print(listOfNames[w], end = " ")
        elif w+2 == NUMBER_OF_STUDENTS:
            print(listOfNames[w], end = " & ")
        else:
            print(listOfNames[w], end = ", ")

    print("(in descending alphabetical order).\n")



def print_the_marks_obtained_after_sorting():


    # To let MARKS_OBTAINED stay constant.
    marksObtained = MARKS_OBTAINED


    print("The marks obtained by the student(s) enrolled in this course",
          "is(are) :-")


    marksObtained.sort()

    # To print the list like 1, 2, 3 & 4 instead of like [1, 2, 3, 4].
    for u in range(NUMBER_OF_STUDENTS):
        if u+1 == NUMBER_OF_STUDENTS:
            print(marksObtained[u], end = " ")
        elif u+2 == NUMBER_OF_STUDENTS:
            print(marksObtained[u], end = " & ")
        else:
            print(marksObtained[u], end = ", ")

    print("(in ascending order).")


    marksObtained.reverse()

    # To print the list like 1, 2, 3 & 4 instead of like [1, 2, 3, 4].
    for v in range(NUMBER_OF_STUDENTS):
        if v+1 == NUMBER_OF_STUDENTS:
            print(marksObtained[v], end = " ")
        elif v+2 == NUMBER_OF_STUDENTS:
            print(marksObtained[v], end = " & ")
        else:
            print(marksObtained[v], end = ", ")

    print("(in descending order).")



main()





# /* Trivia
#
#  * Unlike in C where functions can be declared at the beginning and defined
#    after their first use, functions in Python need to be defined before their
#    first use.
#  * global VARIABLE_NAME declares a global variable, but the ALL_CAPS indicates
#    that the global variable should be treated as a global constant, and its
#    value should not be changed.
#  * In this program, NUMBER_OF_STUDENTS, LIST_OF_NAMES and MARKS_OBTAINED
#    aren't purely constants, as they are set via user input (for eg., input())
#    and data conversion (for eg., int()). Constants should be set directly
#    (for eg., NUMBER_OF_DAYS_IN_A_WEEK = 7).
#  * Classes can also be used to use variables declared in one function in
#    another function of the same class, but that is very similar to using
#    global variables.
#
#  */