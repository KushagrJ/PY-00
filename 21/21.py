# -*- coding: utf-8 -*-
# Python 3.8.6

inputList = [int(i) for i in input().split()]

inputList.sort()

if (len(inputList) == 1):
    print(2*inputList[0])
else:
    print(inputList[1]+inputList[-2])