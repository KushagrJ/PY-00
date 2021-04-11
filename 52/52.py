# -*- coding: utf-8 -*-
# Python 3.8.6

n = int(input())
squareMatrix = []

for x in range(n):
    a = [int(y) for y in input().split()]
    squareMatrix.append(a)

counter = 0
for i in range(n):
    for j in range(n):
        if squareMatrix[i][j] == squareMatrix[j][i]:
            counter = counter+1

if counter == n**2:
    print("Yes")
else:
    print("No")