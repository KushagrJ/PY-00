# -*- coding: utf-8 -*-
# Python 3.8.6

inputList = [int(i) for i in input().split()]

inputList.sort()

if (len(inputList) == 1):
    print(2*inputList[0], end = "")
else:
    print(inputList[1]+inputList[-2], end = "")





# /* Trivia
#
#  * Negative indexing starts from where a sequence ends. So, [-1] corresponds
#    to the last element of a sequence, [-2] corresponds to the second last
#    element of a sequence, and so on.
#
#  * This program contains unnecessary code in order to avoid presentation
#    errors, such as the exclusion of \n, etc.
#
#  */