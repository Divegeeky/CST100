#-- This Program was developed by Jason Pototsky
#-- 11/12/2013 for Week 4 Assignment 1
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal
#------------------------------------- Region Global Variables ----------------------------------------------

#------------------------------------- End Region Global Variables ------------------------------------------
#------------------------------------- Region Functions -----------------------------------------------------
#-- Original Pattern
def patternoriginal(): #-- This is the original pattern
    for i in range(10): #-- Outside loop for each line
        for j in range(10):#-- Inside loop for the numbers
            print(j, end = ' ') #-- The actual print statement
        print() #-- New line

#-- Pattern Number 1
def pattern1(): #-- This is the modified version asked for in #1
    j = 0 #-- Initialize the j variable
    for i in range(10): #-- First for loop
        for q in range(10): #-- Second for loop
            print(j, end = ' ') #-- Prints the line with spacing
        print() #-- This is the Carriage Return for each line
        j = j+1

#-- Pattern Number 2
def pattern2(): #-- This is the pattern asked for in #2
    for i in range(10): #-- The outside loop for each line
        for j in range(0, i+1): #-- The inside loop, with the changing spacing for
                                #-- variation of i
            print(j, end = ' ') #-- prints the line
        print() #-- new line

#-- Pattern Number 3
def pattern3(): #-- This is the pattern asked for in #3
    for i in range(10): #-- This is the line iteration
        for k in range(i): #-- This loop adds the whitespace to "justify" the results
            print(' ', end = ' ') #-- Each line whitespace
        for j in range(0, 10-i): #-- The inside loop, with the changing spacing
                                 #-- for variation of i
            print(j, end = ' ') #-- prints the line
        print() #-- This is the new line

#-- Pattern Number 4
def pattern4(): #-- This is the pattern asked for in #4
    j=10 #-- Initializing the j variable
    for k in range(9): #-- The outside loop for each line
        for i in range(0,k+1): #-- The inside loop with changing variation
            print(j, end = ' ') #-- prints each line with an accumulative function
            j = j+1 #-- Accumulator iteration
        print() #-- End of line
#------------------------------------- End Region Functions -----------------------------------------------------
#------------------------------------- Region Main --------------------------------------------------------------
#-- Function Calls
patternoriginal()
print()
pattern1()
print()
pattern2()
print()
pattern3()
print()
pattern4()
#------------------------------------- End Region Main ----------------------------------------------------------
