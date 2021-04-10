# -*- coding: utf-8 -*-
# Python 3.8.6

a = list(map(int, input().split())); a.sort()
b = []
k = int(input())

for x in a:
    if x not in b:
        b.append(x)
    else:
        pass

sum = b[-k]+b[k-1]; print(sum)





# /* Trivia
#
#  * Given that the inputs are logically valid.
#
#  */