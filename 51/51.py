# -*- coding: utf-8 -*-
# Python 3.8.6

m, n = input().split(); m = int(m); n = int(n)

count = 0

for x in range(m):

    a = [y for y in input().split()]

    for z in a:
        if z in ["0", "1"]:
            count = count+1

if count == m*n:
    print("Yes")
else:
    print("No")





# /* Trivia
#
#  * variableName = () declares a tuple.
#  * Tuples are very similar to lists, except that tuples are immutable.
#  * Tuples are generally used for heterogeneous data, whereas lists are
#    generally used for homogeneous data.
#
#  */