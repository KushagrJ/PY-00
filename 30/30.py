# -*- coding: utf-8 -*-
# Python 3.8.6

inputList = [int(x) for x in input().split()]
totalNumberOfCandies = sum(inputList)

if totalNumberOfCandies%len(inputList) != 0:
    print(-1)

else:

    finalNumberOfCandiesInEachPacket = int(totalNumberOfCandies/len(inputList))

    answer = 0
    for z in inputList:

        if z > finalNumberOfCandiesInEachPacket:
        # Because the candies to be redistributed will be taken from those
        # packets which initially had more candies than the final average.

            answer = answer+int((z-finalNumberOfCandiesInEachPacket))

    print(int(answer))