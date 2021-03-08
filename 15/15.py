# -*- coding: utf-8 -*-
# Python 3.8.6

numberOfStudents = int(input("Enter the number of students enrolled in "
                                  "this course: "))
print("\n", sep = "", end = "")




if (numberOfStudents > 0):



    listOfNames = []
    marksObtained = []

    for x in range(numberOfStudents):
        print("Enter the name of student no. ", x+1, ": ", sep = "", end = "")
        dummyVariable1 = input()
        listOfNames.append(dummyVariable1)

    print("\n", sep = "", end = "")

    for y in listOfNames:
        print("Enter the marks obtained by ", y, ": ", sep = "", end = "")
        dummyVariable2 = int(input())
        marksObtained.append(dummyVariable2)

    print("\n", sep = "", end = "")



    print("The name(s) of the student(s) enrolled in this course is(are) :-\n",
          sep = "", end = "")


    listOfNames.sort()

    for z in range(numberOfStudents):
        if (z+2 != numberOfStudents and z+1 != numberOfStudents):
            print(listOfNames[z], sep = "", end = ", ")
        elif (z+2 == numberOfStudents):
            print(listOfNames[z], sep = "", end = " & ")
        else:
            print(listOfNames[z], sep = "", end = " ")

    print("(in ascending alphabetical order).\n", sep = "", end = "")


    listOfNames.reverse()

    for w in range(numberOfStudents):
        if (w+2 != numberOfStudents and w+1 != numberOfStudents):
            print(listOfNames[w], sep = "", end = ", ")
        elif (w+2 == numberOfStudents):
            print(listOfNames[w], sep = "", end = " & ")
        else:
            print(listOfNames[w], sep = "", end = " ")

    print("(in descending alphabetical order).\n\n", sep = "", end = "")



    print("The marks obtained by the student(s) enrolled in this course ",
          "is(are) :-\n", sep = "", end = "")


    marksObtained.sort()

    for u in range(numberOfStudents):
        if (u+2 != numberOfStudents and u+1 != numberOfStudents):
            print(marksObtained[u], sep = "", end = ", ")
        elif (u+2 == numberOfStudents):
            print(marksObtained[u], sep = "", end = " & ")
        else:
            print(marksObtained[u], sep = "", end = " ")

    print("(in ascending order).\n", sep = "", end = "")


    marksObtained.reverse()

    for v in range(numberOfStudents):
        if (v+2 != numberOfStudents and v+1 != numberOfStudents):
            print(marksObtained[v], sep = "", end = ", ")
        elif (v+2 == numberOfStudents):
            print(marksObtained[v], sep = "", end = " & ")
        else:
            print(marksObtained[v], sep = "", end = " ")

    print("(in descending order).\n", sep = "", end = "")




else:
    print("The number of students should be greater than 0!\n",
          sep = "", end = "")





# /* Trivia
#
#  * listName.sort() sorts a list in ascending order.
#  * listName.reverse() reverses the order of a list.
#
#  */