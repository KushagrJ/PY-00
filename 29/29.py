# -*- coding: utf-8 -*-
# Python 3.8.6

n = int(input())

num = 1
for i in range (1, n+1):
    for j in range (1, i+1):
        print(num*num, end = " ")
        num = num+1
    print()