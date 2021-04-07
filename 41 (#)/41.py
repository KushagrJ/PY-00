# -*- coding: utf-8 -*-
# Python 3.8.6

n = int(input())

for x in range(1, n+1):

    multiplier = int(((10**x)-1)/9)
    print(multiplier**2)





# /* Trivia
#
#  * For x = 1,2,3,..., multiplier = 1,11,111,...
#
#  */