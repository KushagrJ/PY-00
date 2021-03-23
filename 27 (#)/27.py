# -*- coding: utf-8 -*-
# Python 3.8.6

m = int(input())
n = int(input())

if m > n:
    a = n
else:
    a = m

# To make a the greatest common divisor of m and n.
while m%a != 0 or n%a != 0:
    a = a-1

print(a)





# /* Trivia
#
#  * In general, a+=b is the same as a = a+b (for numbers, immutable
#    sequences, etc.). But, for lists (a mutable sequence), a+=b is not the
#    same as a = a+b.
#    [Similarly for -, *, /, //, **, %, etc. for numerical data types]
#  * For numerical data types, a//b is similar to int(a/b).
#  * For numerical data types, a**b means a raised to the power of b.
#
#  */