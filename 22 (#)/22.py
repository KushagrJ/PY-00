# -*- coding: utf-8 -*-
# Python 3.8.6

n = int(input())
inputList = [int(i) for i in input().split()]
outputList = []


for x in inputList:

    if x not in outputList:
        outputList.append(x)
    else:
        pass


print(*outputList, end = "")





# /* Trivia
#
#  * This program contains unnecessary code in order to avoid presentation errors, such as the exclusion of \n, etc.
#
#  */