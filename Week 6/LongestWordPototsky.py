#-- This Program was developed by Jason Pototsky
#-- 11/25/2013 for Week 6 Assignment 1
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal
#------------------------------------- Region Global Variables --------------------------------------------------
sent_input = input("Please input a few words and I will figure out which one is longest") #This will be the input sentance from the user

#------------------------------------- End Region Global Variables -------------------------------------------
#------------------------------------- Region Functions -----------------------------------------------------------
def createlist (): #-- This function will create a list from the input sentance
    list = sent_input.split() #-- This will use the split method to create a list of all the string data
    return list #-- This returns the list to the wordlist variable

def getlongest(): #-- This function will determine which word is the longest in the list
    answer = "" #-- Initializes the answer string
    for i in wordlist: #-- Iterates between all the words in the list
        if len(i) > len(answer): #-- If the length of the word in the iteration is greater than the currently stored answer variable than
            print("I am replacing",answer,"with",i) #-- I originally did this to test my logic and see what each iteration was doing but I decided to
                                                                  #-- keep it because it gave information to the user
            answer = i #-- stores the current word as the variable answer
        elif len(i) == len(answer): #-- I know this is not necessary, but I wanted to test the logic
            print("The word:",i,"has the same length as:",answer,"but:",answer,"occurs before:",i) #-- Again I put this in originally to test my logic
                                                                                                                                        #-- but I decided to keep it.
            
    return answer #-- returns the answer variable to the global answer variable
        
#------------------------------------- End Region Functions -----------------------------------------------------
#------------------------------------- Region Main -------------------------------------------------------------------
wordlist = createlist() #-- The creation of the list and storing it in wordlist in order to pass to the next function
answer = getlongest() #-- Getting the longest word in the list and storing it in the answer variable
print("The longest word in the sentance is:",answer) #-- Print statement to show which word was the longest in the list.
#------------------------------------- End Region Main ------------------------------------------------------------
