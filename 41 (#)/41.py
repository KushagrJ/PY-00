# -*- coding: utf-8 -*-
# Python 3.8.6

def fibonacciSequence(n):

    if n < 3:
        return n-1
    else:
        return (fibonacciSequence(n-1)+fibonacciSequence(n-2))


n = 0
while n < 1:
    n = int(input("Enter the number of terms of the Fibonacci sequence: "))

for x in range(n):
    if x == n-1:
        print(fibonacciSequence(x+1))
    else:
        print(fibonacciSequence(x+1), end = ", ")





# /* Trivia
#
#  * In the Fibonacci sequence, every number is the sum of the two preceding
#    ones, starting from 0 and 1. The sequence is 0,1,1,2,3,5,8,...
#
#  */