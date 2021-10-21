# -*- coding: utf-8 -*-
# Python 3.8.6

m = int(input())
n = int(input())

def factorial(x):
    a = 1
    for i in range(1,x+1):
        a = a*i
    return a

if m+n > 20 or n >= m:
    print("invalid")

else:
    numberOfWays = int((factorial(m)*factorial(m+1))/(factorial(m+1-n)))
    print(numberOfWays)





# /* Trivia - 28.py
#
#  * Recursion can also be used to calculate factorials.
#
#  * End of Trivia */
