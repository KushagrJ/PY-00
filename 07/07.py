# -*- coding: utf-8 -*-
# Python 3.8.6

sum = 1

for x in range(2,10):
    sum = sum+x
    print("The sum of the first", x, "positive integers is", sum)





# /* Trivia
#
#  * for x in range(unsignedInt1, unsignedInt2+1, positiveInt) assigns a new
#    value to x every time, beginning with unsignedInt1 and ending with
#    unsignedInt2, no matter x's previous value. positiveInt sets the
#    incrementation. The default values of unsignedInt1 and positiveInt are 0
#    and 1, respectively.
#    [The arguments of range() can be negative numbers as well]
#  * When only one value is specified in the for loop's range, it is taken to be
#    unsignedInt2+1. When two values are specified in the for loop's range, they
#    are taken to be unsignedInt1 and unsignedInt2+1, respectively.
#
#  */