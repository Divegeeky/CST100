#-- This Program was developed by Jason Pototsky
#-- 11/12/2013 for Week 4 Assignment 2
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal

#------------------------------------- Region Global Variables ----------------------------------------------

#------------------------------------- End Region Global Variables ------------------------------------------

#------------------------------------- Region Functions -----------------------------------------------------
#-- Menu selection
def choice(): #-- function defined to select the pathway
    print("Good Afternoon, welcome to the Bad Wolf Encryptotron 3000!") #-- I <3 Dr. Who
    #-- Selection for the pathway of the "program"
    selection = int(input("Please select if you want to encrypt or decrypt a message 1 for encrypt 2 for decrypt."))
    if selection == 1: #-- If user inputs 1 than goto encrypt function
        encrypt() #-- encrypt function call
    elif selection == 2: #-- If user inputs 2 than gogo decrypt function
        decrypt() #-- decrypt function call
    else: #--If user puts anything else in....sort of error checking
        print ("I do not understand you....")
        choice()#-- Go back to beginning

#-- Encrypt a user's input
def encrypt (): #--function defined to encrypt a message
    message = input("Please input the message you want to encrypt:")#-- User message input
    key = int(input("Please input the key:"))#--User key input
    result="" #-- Initializing the result string
    for i in range(0, len(message)): #-- Loop based on the length of the message
        ordkey = message[i] #-- For each character define it as ordkey
        chrkey = ord(ordkey) #--Get the integer value of the string character
        if (chrkey+key) > 126: #-- If the resulting key+string integer is greater than 126
            encryptedchar = ((chrkey + key)-127)+32 #-- Formula defined in the assignment to change the string integer value thus "encrypting" it.
        elif (chrkey+key) <= 126: #-- If the resulting key+string integer is less than or equal to 126
            encryptedchar = (chrkey + key) #-- change the string integer value thus "encrypting" it.
        else: #-- Originally I put this in to debug my logic. I decided to leave it in as sort of error checking
            print("There is something wrong with your logic!") #-- Spock judges you
        encryptedord = chr(encryptedchar) #-- Gets the resulting string from the adjusted value
        result += encryptedord #-- Adds the "decrypted" character into the string in order
    print("Your encrypted message will be", result) #-- This is the resulting string print
#-- Continue yes or no
    #-- define the endprog variable based upon user input
    endprog = int(input("Do you wish to leave or try again? Select 1 to go back to main menu, 2 to quit, and 3 to encrypt another message"))
    if endprog == 1: #-- Menu item 1
        choice()
    elif endprog == 2: #-- Menu item 2
        print("Goodbye!")
    elif endprog == 3: #-- Menu item 3
        encrypt() #-- restart the function
    else: #-- In case the user puts something else in other than 1,2,or 3
        print("I have a hard time saying goodbye as well.")
        choice() #-- Back to the "beginning"


#--Decrypt a user's input        
def decrypt(): #-- function defined to decrypt a message
    message = str(input("Please input the message you want to decrypt:"))
    #-- I decided to do user input as opposed to function defined variables 
    #-- So that the function could be performed independantly
    for key in range(1, 101): #-- Loop for each key 1-100
        result="" #-- Instantiates the result string
        for i in range(0, len(message)): #-- Loop for each character in the message
            encryptedord = message[i] #-- Defines the character within the message for each part of the loop
            chrkey = ord(encryptedord) #-- Gets the resulting integer value of the "encrypted" character
            if (chrkey - key) < 32 : #-- Logic to determine if the string's integer value minus the key is less than 32
                decryptedchar = ((chrkey - key)+127)-32 #-- Changes the integer value of the string's character to "decrypt" it
            elif (chrkey - key) >= 32 : #--Logic if the character's integer value minus the current key loop is greater than or equal to 32
                decryptedchar = (chrkey - key) #--Changes the character's integer value to "decrypt" it
            else: #-- I originally put this in here to debug my logic but I decided to leave it in "just in case"
                print("There is something wrong with yout logic!") #-- Spock definitely dissaproves
            decryptedord = chr(decryptedchar)#--Gets the string character for the "decrypted" integer value
            result += decryptedord #-- Adds the decrypted character to the string in order
        print("Key", key, "is", result) #-- Prints each key's string result, up to the loop's endpoint 100
    print("I hope this helped your mission.") 
#-- Continue yes or no
    endprog = int(input("Do you wish to leave or try again? Select 1 to go back to main menu, 2 to quit, and 3 to encrypt another message"))
    if endprog == 1: #-- Menu item 1
        choice() #-- Back to the "beginning"
    elif endprog == 2: #-- Menu item 2
        print("Goodbye!")
    elif endprog == 3: #-- Menu item 3
        decrypt() #-- restart the function
    else: #-- In case the user puts something else in
        print("I have a hard time saying goodbye as well.")
        choice() #-- Back to the beginning

#------------------------------------------ End Region Functions ------------------------------------------

#------------------------------------------ Region Main ---------------------------------------------------
choice() #-- function call for the program 

#------------------------------------------ End Region Main -----------------------------------------------
