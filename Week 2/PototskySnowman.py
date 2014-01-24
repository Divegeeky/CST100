#-- This Program was developed by Jason Pototsky
#-- 10/29/2013 for Week 2 Assignment
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal

import turtle #--Importing the turtle module
import math  #Importing the math module in order to define Pi

wn = turtle.Screen() #--Defining the screen
turtle.bgcolor("Blue") #--Set the background color using the turtle.bgcolor method
alex = turtle.Turtle() #--Create the turtle
alex.width(3) #--Define the width of the outline for alex
alex.speed(0) #--Make Alex draw faster

#---Begin the Bottom Circle

alex.up() #--Lift the Pen using the .up method
alex.goto(0,-300) #--Move turtle to the beginning point for the Bottom Circle
alex.down() #--Place Pen back on the drawing surface
Radius = int(100) #--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100 #--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n #--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('White')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill

#---Begin the Middle Circle

alex.up()#--Tell Alex to lift up his pen
alex.goto(0,-100)#--Move Alex to beginning point of Middle Circle
alex.down()#--Tell Alex to drop his Pen
Radius = int(70)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('White')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill#--Tell Turtle to end the Fill

#---Begin Top Circle

alex.up()#--Tell Alex to lift up his pen
alex.goto(0,40)#--Move Alex to beginning point of Top Circle
alex.down()#--Tell Alex to drop his Pen
Radius = int(40)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('White')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill

#---Begin Arm one

alex.up()#--Tell Alex to lift up his pen
alex.goto(70,-25)#--Move Alex to beginning point of Arm one
alex.down()#--Tell Alex to drop his Pen
alex.left(45)#--Turn Alex to 45 Degrees to make cheering arms
alex.forward(115)#--Move Turtle Forward to make the Arms
alex.left(75)#--Turn alex to make finger one
alex.forward(25)#--Make Finger number one
alex.backward(25)#--Move alex back to finger start
alex.right(75)#--Turn alex to make finger number two
alex.forward(25)#--Move alex to make finger number two
alex.backward(25)#--Move alex back to start point to make Finger number three
alex.right(75)#--Turn alex to make finger number three
alex.forward(25)#--Move alex forward to make finger number three

#---Begin Arm two

alex.up()#--Tell Alex to lift up his pen
alex.goto(-70,-25)#--Move Alex to beginning point of Arm Two
alex.down()#--Tell alex to drop his pen
alex.left(170)#--Tell alex to turn to 170 Degrees to make cheering arm
alex.forward(115)#--Move alex forward to create arm two
alex.left(75)#--Tell alex to turn to make finger one
alex.forward(25)#--Tell alex to move forward to create finger one
alex.backward(25)#--Move alex back to beginning area
alex.right(75)#--Turn Alex to make finger two
alex.forward(25)#--Move alex to make finger two
alex.backward(25)#--Move alex back to beginning point
alex.right(75)#--Turn Alex to make finger three
alex.forward(25)#--Move Alex to make finger three

#---Begin Face
#---Eye One
alex.up()#--Tell alex to lift up his pen
alex.goto(-10,90)#--Move alex to beginning of eye one
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill

#---Eye Two
alex.up()#--Tell alex to lift up his pen
alex.goto(10,90)#--Move alex to beginning of eye two
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill

#---Nose
alex.up()#--Tell alex to lift up his pen
alex.goto(0,80)#--Move alex to beginning of nose
alex.down()#--Tell alex to drop pen
alex.color('Orange')#--Change outline to orange for the carrot nose
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Orange')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.color('Black')#--Tell alex to go back to black outlines

#---Mouth

alex.up()#--Tell alex to lift up his pen
alex.goto(-20,70)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(-15,65)#--Move alex to new point
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(-10,60)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(-5,60)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(0,60)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(5,60)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.5)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(10,60)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.9)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(15,65)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.9)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill
alex.up()#--Tell alex to lift up his pen
alex.goto(20,70)#--Move alex to beginning of mouth
alex.down()#--Tell alex to drop pen
Radius = int(2.9)#--Define the Radius of the Circle
Circumference = 2*(math.pi)*(Radius) #--Define the Circumference of the Circle
n = 100#--Define n where n is the number of Lines we wish to make
Circum_N = Circumference / n#--Create a range in which to split up the circumference to use in .forward
Angle_N = 360 / n#--Create a range in which to split up the degrees of the circle
alex.fillcolor('Black')#--Define the fillcolor of the Bottom Circle
alex.begin_fill()#--Tell turtle to begin the fill of the Geometric shape
for x in range(n):#--Create the iteration in which the turtle makes the circle
    alex.left(Angle_N)#--Turn turtle the amount needed based on Circle Degrees Div by N
    alex.forward(Circum_N)#--Move the turtle forward needed based on Circumference Div by N
alex.end_fill()#--Tell Turtle to end the Fill

#---Top Hat

alex.up()#--Tell Alex to lift his pen
alex.goto(0,120)#--Tell Alex to goto the beginning of the Top Hat
alex.down()#--Tell Alex to drop his pen
alex.fillcolor('Black')#--Tell Alex the color to fill of the Geometric shape
alex.begin_fill()#--Tell Alex to begin the Fill
alex.right(65)#--Tell alex to turn
alex.forward(50)#--Tell Alex to go forward to create a section of the Top Hat
alex.backward(100)#--Tell Alex to go backwards double to make the bottom of the top hat
alex.left(90)#--Tell Alex to turn to make bottom base of hat
alex.forward(20)#--Tell Alex to move forward to make outside edge
alex.right(90)#--Tell Alex to turn in order to make base
alex.forward(30)#--Tell Alex to move forward to make base and attach to top
alex.left(90)#--Tell Alex to turn to make top of hat
alex.forward(50)#--Tell Alex to move forward to make side edge of top hat
alex.right(90)#--Tell Alex to turn to make the side edge
alex.forward(40)#--Tell Alex to move forward to make top edge
alex.right(90)#--Tell Alex to turn to make top edge
alex.forward(50)#--Tell Alex to move forward to make right edge
alex.left(90)#--Tell Alex to turn to make base of hat
alex.forward(30)#--Tell Alex to move forward to make top of base
alex.right(90)#--Tell Alex to turn in order to make side edge of base
alex.forward(30)#--Tell Alex to move forward to finish the hat
alex.end_fill()#--Tell Alex to end the Fill
