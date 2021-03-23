# -*- coding: utf-8 -*-
# Python 3.8.6

inputList = [int(i) for i in input().split()]
outputList = []


for x in inputList:

    if abs(x)%10 != 4:
        outputList.append(x)
    else:
        pass


print(*outputList)





# /* Trivia
#
#  * print(*sequenceName) prints the elements of the specified sequence with a
#    space between them.
#  * [int(i) for i in input().split()] converts the multiple inputs into
#    integers before adding them to a list and returning the list. This is known
#    as list comprehension.
#    For eg., fruitsStartingWithA = [x for x in fruits if x[0] == "A"]
#  * abs(number) returns the absolute value of the specified number.
#
#  */