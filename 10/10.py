# -*- coding: utf-8 -*-
# Python 3.8.6

a, b = input().split()

a = int(a)
b = int(b)

e = a*b

print(e, "\n", sep = "", end = "")

# input().split("separator", unsignedInt) takes multiple inputs. The default separator is any whitespace. The number of inputs is equal to unsignedInt+1. The default value of unsignedInt is -1, which means that any number of inputs can be taken.
# int(input()).split(), etc. are not valid.