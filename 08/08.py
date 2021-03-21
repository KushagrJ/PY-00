# -*- coding: utf-8 -*-
# Python 3.8.6

a = int(input("Enter the integer value for which you want to know the "
              "multiplication table: "))

for x in range(1,10):
    print(a, "x", x, " = ", a*x, sep = "")