# -*- coding: utf-8 -*-
# Python 3.8.6

a, b = input().split()

a = int(a)
b = int(b)

if (a>b):
    print(a, "\n", sep = "", end = "")
else:
    print(b, "\n", sep = "", end = "")