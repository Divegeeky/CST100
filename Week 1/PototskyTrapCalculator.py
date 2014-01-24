#-- This Program was developed by Jason Pototsky
#-- 10/21/2013 for Week 1 Assignment #1 Part 2
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal

#-- First line will initialize the variable height and assign the input to the variable
height = float(input("Please input the height of the trapezoid: "))

#-- Second line will initialize the variable lbtm and assign the input to the variable
lbtm = float(input("Please input the length of the bottom base: "))

#-- Third line will initialize the variable ltop and assign the input to the variable
ltop = float (input("Please input the length of the top base: "))

#-- This line will layout the algorithm for the program to accomplish the computation
A = ((1/2)*(ltop + lbtm)) * height

#-- This line will output the results to the host
print ("The Area of the Trapezoid is :", A)

#-- End
