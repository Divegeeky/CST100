#-- This Program was developed by Jason Pototsky
#-- 11/04/2013 for Week 3 Assignment 1
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal
import random   #-- Import the random module
status = False  #-- Set the initial status as False for the while loop
number = random.randrange(1,21) #-- Define the random number to guess
num_iterations = 0 #-- Initialize the number of moves
user_name = input ("Please input your Name:") #-- Get the user's Name
user_guess = 0
#-- Welcome message
print ("Hello," ,user_name, "would you like to play a game? How about Thermonuclear War? No? Ok Number Guessing it is.")

#-- Begin the user input function
def user_input(): #-- Initialize the named function
    global user_guess #-- Allows you to modify the global variable
    #-- Ask for the guess
    user_guess = int(input("Please make a guess one through twenty:"))
    #-- A little bit of error checking fun
    try:
        if user_guess > 20:
            user_guess = int(input("Don't try and fool me my brother was skynet:"))
        #-- A little bit of redundant error checking fun
        if user_guess > 20:
            user_guess = int(input("Seriously? Are you Jon Conner? Just guess 1-20:"))
            if user_guess >20:
                user_input()
            if user_guess <0:
                user_input()
        elif user_guess < 0:
            user_guess = int(input("You are pretty thick aren't you?:"))
            if user_guess >20:
                user_input()
            if user_guess <0:
                user_input()

    #-- I know I probably could have done a loop, but that isn't as fun as all this typing
        if user_guess < 0:
            user_guess = int(input("Negative numbers won't work on me:"))
            if user_guess > 20:
                user_guess = int(input("Do we seriously have to do this:"))
                if user_guess > 20:
                    user_input()
                if user_guess < 0:
                    user_input()
            elif user_guess < 0:
                user_guess = int(input("I'm going to nuke your planet:"))
                if user_guess > 20:
                    user_input()
                if user_guess < 0:
                    user_input()
    #-- My program would fail if I put in a string so I added this
    except:
        print("I don't know what you did but its not that hard to type in a number 1-20, is it?")
        user_input()
        
    return user_guess #-- Return the user_guess variable to the next function

#-- Begin the compare number function
def compare_number (UG, number): #-- Initialize the function and set the parameters
    #-- Allow for global maipulation of the variables
    global num_iterations
    global status
    #-- The winning guess
    if UG == number:
        print("Congratulations," ,user_name, "you have won the game in",num_iterations,"moves")
        status = True #-- while loop end
    #-- The User Guess is too large
    if UG > number:
        print("OOOoooooh, so close but you are too high")
        num_iterations = num_iterations + 1 #-- Increase the move numbers
        status = False #-- while loop continue
        print("You have made,",num_iterations,"guesses")
        user_input() #-- Ask for new input....Inpuuuut Johnny 5 is aliiiive
    #-- The User Guess is too small
    if UG < number:
        print("Your too small, not the first time you heard that I am guessing.")
        num_iterations = num_iterations + 1 #-- Increase the move numbers
        status = False #-- while loop continue
        print("You have made,",num_iterations,"guesses")
        user_input() #-- Wouldn't you like to be a pepper too?
    #-- Return the status variable to begin or end the while loop
    return status

#-- My program didn't have error handling for the first guess, so I made a function
def initializeuser_guess ():
    global user_guess
    try :
        user_guess = user_input() #-- Initial user_guess variable and input call
    except:
        print("I don't know what you did but its not that hard to type in a number 1-20, is it?")
        initializeuser_guess()
#-- The first guess call
initializeuser_guess()
#-- While loop begins
while status == False: #-- statment to be met in order to continue
    ###It amuses me that this one little line does most
    ###of the work of this program
    compare_number(user_guess,number)
    
