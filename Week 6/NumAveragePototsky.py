#-- This Program was developed by Jason Pototsky
#-- 11/25/2013 for Week 6 Assignment 2
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal
#------------------------------------- Region Global Variables --------------------------------------------------
averages = { } #-- Initializing the Averages Dictionary for later use
averages['AvgPositive'] = 0 #-- Initializing the AvgPositive Key in the Dictionary
averages['AvgNonPos'] = 0 #-- Initializing the AvgNonPos Key in the Dictionary
averages['AvgAllNum'] = 0 #-- Initializing the AvgAllNum Key in the Dictionary
#------------------------------------- End Region Global Variables -------------------------------------------
#------------------------------------- Region Functions -----------------------------------------------------------
def getnumbers (): #-- This Function will get the numbers an build the numlist list
    a = 0 #-- Initializes the temporary number variable for each iteration
    numlist = [] #-- Initializes the list
    while a != -9999: #-- While loop to continue inputting integers
        try: #-- A little exception handling, I realized string information would end the whole thing.
            a = int(input("Please input a number, when you are ready to be done input -9999:")) #-- Input the integer
            if a != -9999: #-- This ensures that I do not append the "sentinel value" of -9999
                numlist.append(a) #-- Append the information to the list
        except: #-- A little exception handling for string information
            print("Sanford would say 'What are you doing Dummy?'") #-- BumBum Bwena Bum Bum Bwena wanna waaa 
    return numlist #-- Return the numlist variable to global scope

def AvgPositive(): #-- This Function will return the positive average
    tally = 0 #-- Initializes the Tally accumulator
    total = 0 #-- Initializes the Total accumulator
    for i in numlist: #-- Iteration for every number in the numlist
        if i > 0: #-- Logic that states if item is above Zero or positive than conduct the following
            tally = tally + 1 #-- Running tally to determine the number of values to divide against
            total = total + i #-- The Total value that will determine the average
    try: #-- A little exception handling for lists without positive integers
        AvgPositive = round(total/tally,1) #-- Get the average, and round it to the nearest tenth
    except: # A little exception handling for lists without positive integers
        print("Evidently there is no Positive numbers in your list") #-- As it says
        AvgPositive = "N/A" #Set the AvgPositive to Not Applicable
    return AvgPositive #-- Return AvgPositive to the global scope

def AvgNonPos(): #-- This Function will return the Non-Positive average
    tally = 0 #-- Initializes the Tally accumulator
    total = 0 #-- Initializes the Total accumulator
    for i in numlist: #-- Iteration for every number in the numlist
        if i <= 0: #-- Logic that states if item is less than zero or zero
            tally = tally + 1 #-- Running tally to determine the number of values to divide against
            total = total + i #-- The Total value that will determine the average
    try: #-- A little Exception handling for lists without negative integers
        AvgNonPos = round(total/tally, 1) #-- Get the average of the negative integers and round it to the nearest tenth
    except: #-- A little Exception handling for lists without negative values
        print("Evidently there is no Negative numbers in your list") #-- As it says
        AvgNonPos = "N/A" #-- Sets the AvgNonPos variable to Not Applicable
    return AvgNonPos #-- Return the AvgNonPos variable ot the global scope

def AvgAllNum(): #This function will return the average off all numbers in the list
    tally = 0 #-- Initializes the Tally accumulator
    total = 0 #-- Initializes the Total accumulator
    for i in numlist: #-- Iteration for every number in the numlist
        tally = tally + 1 #-- Running tally to determine the number of values to divide against
        total = total + i #-- The Total value that will determine the average
    try: # A little exception handling because I like to trick my programs sometimes.
        AvgAllNum = round(total/tally, 1) #-- Get the average of all the values and round to the nearest tenth
    except: #-- Just in case somone just enters the sentinel value 
        print("You tried to trick with no numbers, but I am super SMRT") #-- I M SMRT
        AvgAllNum = "N/A" #sets the AvgAllNum Variable to Not Applicable
    return AvgAllNum #-- Returns the AvgAllNum variable to the global scope
#------------------------------------- End Region Functions -----------------------------------------------------
#------------------------------------- Region Main -------------------------------------------------------------------
numlist= getnumbers() #-- Create the numlist that will be used in all functions
print("""The values of the list are:
""", numlist) #-- Show the user the values of numlist
AvgPositive = AvgPositive() #-- Get the Positive Average and store it in AvgPositive
AvgNonPos = AvgNonPos() #-- Get the Non-Positive Average and store it in AvgNonPos
AvgAllNum = AvgAllNum() #-- Get the Average of all integers and store it in AvgAllNum 
averages['AvgPositive'] = AvgPositive #-- Set the Dictionary key AvgPositve to the Value stored in AvgPositive
averages['AvgNonPos'] = AvgNonPos #-- Set the Dictionary key AvgNonPos to the Value stored in AvgNonPos
averages['AvgAllNum'] = AvgAllNum #-- Set the Dictionary key AvgAllNum to the Value stored in AvgAllNum
print("""The Dictionary with averages is:
""", averages) #-- Display the dictionary for the user with the values changed for the number list
#------------------------------------- End Region Main ------------------------------------------------------------
