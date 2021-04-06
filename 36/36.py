# -*- coding: utf-8 -*-
# Python 3.8.6

a = list(map(int, input().split()))
n = len(a)

numberOfSwaps = 0

for x in range(1,n):

    for y in range(n-x):

        if a[y] > a[y+1]:
            temp = a[y]
            a[y] = a[y+1]
            a[y+1] = temp
            numberOfSwaps = numberOfSwaps+1
        else:
            pass

print(numberOfSwaps)





# /* Trivia
#
#  * map(function, iterable(s)) executes the specified function for each item in
#    the given iterable(s). For multiple iterables, the function should have one
#    parameter for each iterable.
#    [Used here as an alternative for list comprehension]
#
#  */