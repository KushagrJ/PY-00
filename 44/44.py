# -*- coding: utf-8 -*-
# Python 3.8.6

import turtle

turtle.bgcolor("black")
myTurtle = turtle.Turtle(); myTurtle.setpos(-250,250); myTurtle.color("white")
distanceToMoveWhenCalled = 25

rows = 20; columns = 22;
rowCounterForSpiral = rows; columnCounterForSpiral = columns

while rowCounterForSpiral > 0 and columnCounterForSpiral > 0:

    for x in range(rowCounterForSpiral):
        myTurtle.forward(distanceToMoveWhenCalled)
    myTurtle.right(90)
    rowCounterForSpiral = rowCounterForSpiral-1

    for y in range(columnCounterForSpiral):
        myTurtle.forward(distanceToMoveWhenCalled)
    myTurtle.right(90)
    columnCounterForSpiral = columnCounterForSpiral-1

turtle.Screen().exitonclick()





# /* Trivia
#
#  * turtle.bgcolor(color) sets the background color of the TurtleScreen.
#  * myTurtle = turtle.Turtle() creates a variable named myTurtle and assigns it
#    a turtle object, which comes from the turtle module.
#  * myTurtle.pendown()/myTurtle.pd()/myTurtle.down() makes the turtle draw when
#    moving.
#    myTurtle.penup()/myTurtle.pu()/myTurtle.up() makes the turtle not draw when
#    moving.
#    [The default mode is pen down]
#  * myTurtle.setpos(x,y)/myTurtle.setposition(x,y)/myTurtle.goto(x,y) moves the
#    turtle to the specified position.
#    Initially, the bgcolor and the turtle's color are both black, so the line
#    drawn when going from (0,0) to (-250,250) isn't visible.
#  * myTurtle.color(color) sets the pen color of the turtle.
#  * myTurtle.forward(distance)/myTurtle.fd(distance) moves the turtle forward
#    by the specified distance.
#  * myTurtle.backward(distance)/myTurtle.bk(distance)/myTurtle.back(distance)
#    moves the turtle backward by the specified distance, opposite to the
#    direction in which the turtle is headed.
#  * myTurtle.right(angle)/myTurtle.rt(angle) turns the turtle right by the
#    specified angle.
#  * myTurtle.left(angle)/myTurtle.lt(angle) turns the turtle left by the
#    specified angle.
#
#  */