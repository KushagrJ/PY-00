# -*- coding: utf-8 -*-
# Python 3.8.6

sum = 1

for x in range(2, 10):
    sum = sum+x
    print("The sum of the first ", x, " positive integers is ", sum, "\n",
          sep = "", end = "")



# /* Trivia
#
#  * for x in range(unsignedInt1, unsignedInt2, positiveInt) assigns a new value to x every time, beginning with
#    unsignedInt1 and ending with unsignedInt2-1, no matter x's previous value. positiveInt sets the incrementation.
#    The default values of unsignedInt1 and positiveInt are 0 and 1, respectively.
#
#  */