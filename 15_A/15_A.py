# -*- coding: utf-8 -*-
# Python 3.8.6

numberOfStudents = int(input("Enter the number of students enrolled in "
                             "this course: "))

print()




if numberOfStudents > 0:



    listOfNames = []
    marksObtained = []

    for x in range(numberOfStudents):
        print("Enter the name of student no. ", x+1, ": ", sep = "", end = "")
        dummyVariable1 = input()
        listOfNames.append(dummyVariable1)

    print()

    for y in listOfNames:
        print("Enter the marks obtained by ", y, ": ", sep = "", end = "")
        dummyVariable2 = int(input())
        marksObtained.append(dummyVariable2)

    print()



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




else:
    print("The number of students should be greater than 0!")





# /* Trivia
#
#  * listName.sort() sorts the specified list in ascending order.
#  * listName.reverse() reverses the order of the specified list.
#  * listName[unsignedInt1 : unsignedInt2+1 : positiveInt] returns a subset of
#    the specified list containing those items whose indices are in the range
#    unsignedInt1 to unsignedInt2, including them both. This is known as
#    slicing. positiveInt sets the incrementation. The default values of
#    unsignedInt1, unsignedInt2+1 and positiveInt are 0, len(listName) and 1,
#    respectively.
#    [Similarly for other sequences]
#
#  */