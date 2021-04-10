# -*- coding: utf-8 -*-
# Python 3.8.6

a = input().split(",")
b = [int(i) for i in input().split(",")]
c = {}
positionOfToken = 0

for x in a:
    u = x.split(":")
    startOfToken = int(u[0].strip()); endOfToken = int(u[1].strip())
    c[startOfToken] = endOfToken

for y in b:

    positionOfToken = positionOfToken+y

    if positionOfToken in c:
        positionOfToken = c[positionOfToken]

if positionOfToken >= 100:
    print("Yes")
else:
    print("No")