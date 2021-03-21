# -*- coding: utf-8 -*-
# Python 3.8.6

a, b = input().split()

a = int(a)
b = int(b)

c = a*b

print(c, end = "")





# /* Trivia
#
#  * input().split("separator", unsignedInt-1) takes multiple inputs as strings.
#    The default separator is any whitespace. The number of inputs is equal to
#    unsignedInt. The default value of unsignedInt-1 is -1, which means that any
#    number of inputs can be taken.
#  * int(input()).split(), etc. are not valid.
#  * a, b = input().split() makes the interpreter expect only 2 inputs.
#    a = input().split() will take any number of inputs and assign a list of the
#    inputs to a.
#
#  * This program contains unnecessary code in order to avoid presentation
#    errors, such as the exclusion of \n, etc.
#
#  */