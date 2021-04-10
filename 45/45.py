# -*- coding: utf-8 -*-
# Python 3.8.6

actualList = list(input())
encodedList = list(input())

for x in range(len(encodedList)):
    if ord(encodedList[x]) < 70:
        encodedList[x] = chr(ord(encodedList[x])+21)
    else:
        encodedList[x] = chr(ord(encodedList[x])-5)

if sorted(actualList) == sorted(encodedList):
    print("Yes")
else:
    print("No")





# /* Trivia
#
#  * sorted(iterableName, reverse = True/False) returns a new sorted list,
#    leaving the original list unaffected, whereas listName.sort() sorts the
#    list in place.
#    [The default value of reverse is False]
#  * sorted() works on any iterable, not just lists, returning a list of
#    elements, sorted.
#
#  */