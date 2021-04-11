# -*- coding: utf-8 -*-
# Python 3.8.6

n = int(input())

for i in range(n):
    for j in range((n*i)+1, n*(i+1)+1):
        print(j, end = " ")
    print()