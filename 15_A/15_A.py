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
#    [This doesn't work for lists containing numerical and string elements both]
#  * listName.reverse() reverses the order of the specified list.
#
#  * listName[unsignedInt1 : unsignedInt2+1 : positiveInt] returns a subset of
#    the specified list containing those items whose indices are in the range
#    unsignedInt1 to unsignedInt2, including them both. This is known as
#    slicing. positiveInt sets the incrementation. The default values of
#    unsignedInt1, unsignedInt2+1 and positiveInt are 0, len(listName) and 1,
#    respectively.
#    [Similarly for other sequences]
#
#    For negative incrementations,
#    a[::-1] returns all items (reversed),
#    a[1::-1] returns the first two items (reversed),
#    a[:-3:-1] returns the last two (not four) items (reversed),
#    a[-3::-1] returns all items except the last two (reversed), and so on.
#    [For s[i:j], (i) if i is omitted/'None', then it is treated like 0.
#                 (ii) if j is omitted/'None', then it is treated like len(s).
#     For s[i:j:k], (i) if i or j are omitted/'None', then they become the 'end'
#                       values (which end depends on the sign of k).
#                       i and j will always represent the start and stop values,
#                       respectively. Only their ends will change depending on
#                       the sign of k.
#                   (ii) if k is omitted/'None', then it is treated as 1.]
#    [Slices like s[2:5:-1] don't work. They return an empty sequence.]
#
#  */