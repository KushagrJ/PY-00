# -*- coding: utf-8 -*-
# Python 3.8.6

import turtle, random

listOfPenColors = ["white", "yellow", "brown", "red", "blue", "green", "orange",
                   "pink", "violet", "grey", "cyan"]

turtle.bgcolor("black")
myTurtle = turtle.Turtle(); myTurtle.setpos(-250,250); myTurtle.penup()
distanceToMoveWhenCalled = 25

rows = 20; columns = 22;
rowCounterForSpiral = rows; columnCounterForSpiral = columns

while rowCounterForSpiral > 0 and columnCounterForSpiral > 0:

    myTurtle.color(random.choice(listOfPenColors))
    for x in range(rowCounterForSpiral):
        myTurtle.dot()
        myTurtle.forward(distanceToMoveWhenCalled)
    myTurtle.right(90)
    rowCounterForSpiral = rowCounterForSpiral-1

    myTurtle.color(random.choice(listOfPenColors))
    for y in range(columnCounterForSpiral):
        myTurtle.dot()
        myTurtle.forward(distanceToMoveWhenCalled)
    myTurtle.right(90)
    columnCounterForSpiral = columnCounterForSpiral-1

turtle.Screen().exitonclick()





# /* Trivia
#
#  * myTurtle.dot(size, color) prints a dot with the specified size and color.
#    If the size is not specified, then a default value is used. If the color is
#    not specified, then the pen color is used.
#
#  */