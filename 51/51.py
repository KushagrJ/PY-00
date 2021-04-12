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