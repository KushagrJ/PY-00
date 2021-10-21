# -*- coding: utf-8 -*-
# Python 3.8.6

list1 = input().split(); list2 = input().split()

string1 = ''.join(list1); string2 = ''.join(list2)

if string2.find(string1) == 0:
    print("Yes")
else:
    print("No")





# /* Trivia - 48.py
#
#  * string1.find(string2) returns the starting index of the first occurrence
#    of string2 in string1. If string2 is not found in string1, then it
#    returns -1.
#  * find() is similar to index(), but index() raises ValueError when the string
#    is not found, instead of returning -1.
#
#  * End of Trivia */
