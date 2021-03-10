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

    for z in range(numberOfStudents):                                               # To print listOfNames like
        if (z+1 == numberOfStudents):                                               # a, b, c, d & e instead of like
            print(listOfNames[z], sep = "", end = " ")                              # ['a', 'b', 'c', 'd', 'e'].
        elif (z+2 == numberOfStudents):
            print(listOfNames[z], sep = "", end = " & ")
        else:
            print(listOfNames[z], sep = "", end = ", ")

    print("(in ascending alphabetical order).\n", sep = "", end = "")


    listOfNames.reverse()

    for w in range(numberOfStudents):                                               # To print listOfNames like
        if (w+1 == numberOfStudents):                                               # a, b, c, d & e instead of like
            print(listOfNames[w], sep = "", end = " ")                              # ['a', 'b', 'c', 'd', 'e'].
        elif (w+2 == numberOfStudents):
            print(listOfNames[w], sep = "", end = " & ")
        else:
            print(listOfNames[w], sep = "", end = ", ")

    print("(in descending alphabetical order).\n\n", sep = "", end = "")



    print("The marks obtained by the student(s) enrolled in this course ",
          "is(are) :-\n", sep = "", end = "")


    marksObtained.sort()

    for u in range(numberOfStudents):                                               # To print marksObtained like
        if (u+1 == numberOfStudents):                                               # 1, 2, 3, 4 & 5 instead of like
            print(marksObtained[u], sep = "", end = " ")                            # [1, 2, 3, 4, 5].
        elif (u+2 == numberOfStudents):
            print(marksObtained[u], sep = "", end = " & ")
        else:
            print(marksObtained[u], sep = "", end = ", ")

    print("(in ascending order).\n", sep = "", end = "")


    marksObtained.reverse()

    for v in range(numberOfStudents):                                               # To print marksObtained like
        if (v+1 == numberOfStudents):                                               # 1, 2, 3, 4 & 5 instead of like
            print(marksObtained[v], sep = "", end = " ")                            # [1, 2, 3, 4, 5].
        elif (v+2 == numberOfStudents):
            print(marksObtained[v], sep = "", end = " & ")
        else:
            print(marksObtained[v], sep = "", end = ", ")

    print("(in descending order).\n", sep = "", end = "")




else:
    print("The number of students should be greater than 0!\n",
          sep = "", end = "")





# /* Trivia
#
#  * listName.sort() sorts a list in ascending order.
#  * listName.reverse() reverses the order of a list.
#  * listName[unsignedInt1:unsignedInt2+1] returns a subset of a list containing those items whose indices are in the
#    range unsignedInt1 to unsignedInt2, including them both. The default values of unsignedInt1 and unsignedInt2+1 are
#    0 and len(listName), respectively.
#
#  */