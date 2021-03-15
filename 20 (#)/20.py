# -*- coding: utf-8 -*-
# Python 3.8.6

inputList = [int(i) for i in input().split()]
outputList = []


for x in inputList:

    if abs(x)%10 != 4:
        outputList.append(x)
    else:
        pass


print(*outputList, end = "")





# /* Trivia
#
#  * print(*sequenceName) prints the elements of the specified sequence with a space between them.
#  * [int(i) for i in input().split()] converts the multiple inputs into integers before adding them to a list and
#    returning the list.
#  * abs(number) returns the absolute value of the specified number.
#
#  * This program contains unnecessary code in order to avoid presentation errors, such as the exclusion of \n, etc.
#
#  */