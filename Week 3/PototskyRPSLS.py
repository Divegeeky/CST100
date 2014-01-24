#-- This Program was developed by Jason Pototsky
#-- 11/04/2013 for Week 3 Assignment 2
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal

import random #-- Import random module
status = False #-- Initializes the status variable for the while loop to keep playing
game_selection = 0 #-- Initializes the game_selection variable to choose when function
rule_selection = 0 #-- Initialize the rules variable
score1 = 0 #-- Initialize score1
score2 = 0 #-- Initialize score2

#-- Welcome message
print ("Hello, welcome to Gamestation! We here at Satellite 5 welcome you to the games.")
print ("Today's festivities is a game called Rock, Paper, Scissors, Lizard, Spock")
print ("It is told, that early human civilizations used this game to decide their kings")

#-- Do you require rules for this game?
def rule_select(rule_selection):
        try:
                rule_selection = int(input("Do you require rules for this game Hooman? Please select 1 for Yes 2 for No."))        
                if rule_selection == 1:
                        print("The rules are relatively easy to understand, even for a Hoooman.")
                        print("You will select either Rock, Paper, Scissors, Lizard, or Spock.")
                        print("Your opponent will do the same.")
                        print("Scissors cut paper, Paper covers rock, Rock crushes Lizard, Lizard poisons Spock.")
                        print("Spock smashes Scissors, Scissors decapitate lizard, Lizard eats paper.")
                        print("Paper disproves Spock, Spock vaporizes rock, and Rock crushes scissors.")
                        rule_select(rule_selection)
                elif rule_selection == 2:
                        gameselect()
                else: 
                        rule_select(rule_selection)
        except:
                print("I have no clue what you did, but please say 1 for yes, 2 for no.")
                rule_select(rule_selection)

#-- Select 1Player or 2Player
def gameselect (): #-- define the gameselect 
        try:
                global game_selection #-- Give the ability to manipulate the game_selection variable
                print("Would you like to play another player, or play me?")
                game_selection = int(input("Type 1 for 1Player, or Type 2 for 2Player:"))
                #-- 1 Player or 2 Player selection
                if game_selection == 1:
                        print("Awe, poor you, you have no friends")
                        run_1Player()
                elif game_selection == 2:
                        print("Lets get ready to RUUUUUUUUUUMBLLE")
                        run_2Player()
                else:
                        print("You aren't the brightest bulb in the box are you?")
                        gameselect()

        except: #-- A little error catching.
                print("What'd you do???")
                gameselect()

#-- 1 Player Game
def run_1Player ():
        global status #-- Allows manipulating the global status variable
        Player1 = input("Hooman what shall I call you?:")

        #-- Begin the while loop
        while status == False: 
                print(Player1,"it is, so we shall begin,CHOOSE YOUR WEAPON!")
                weapon1 = chooseweapon() #-- Call the choose weapon function for human selection
                weapon2 = computerchoose() #-- Call the computer selection
                combat(weapon1,weapon2) #-- Perform the "combat"
                print("The battle between you and I stands at",score1,"for you.",score2,"For me")#-- Results of the round
                #--Option to leave the game
                cont = int(input("Do you wish to continue? 1 for yes 2 for no."))
                if cont == 1:
                        status = False
                #-- Begins leaving the while loop
                elif cont == 2:
                        status = True
                        print("Our battle has come to an end. The score is",score1,"for you and",score2,"for me.")
                        #-- End results for 1Player Game
                        if score1 > score2:
                                print("I bow before your greatness.",Player1, "I demand a re-match!")
                        if score1 < score2:
                                print("HA!! I am victorious, I see the remains of",Player1, "before me!")
                        if score1 == score2:
                                print("I see our powers are matched, you have emerged unscathed this time",Player1)
                else: #-- For the fat fingers
                        staus = False
                        print("I will take that as you want to continue playing")
#-- 2 Player Game
def run_2Player() :
        global status #-- Allow manipulating the global status variable
        Player1 = input("Player one, what shall I call you?:")
        Player2 = input("Player two, what shall I call you?:")
        #-- Enter the while loop
        while status == False:
                weapon1 = chooseweapon() #--Call the chooseweapon function for Player 1
                weapon2 = chooseweapon() #--Call the chooseweapon function for Player 2
                combat(weapon1,weapon2) #--Perform the "combat"
                print("The battle between",Player1,"and",Player2,"Stands as:",Player1,score1,Player2,score2) #Results of the round
                cont = int(input("Do you wish to continue? 1 for yes 2 for no.")) #-- Option to leave
                if cont == 1:
                        status = False
                #-- Begin the functions upon leaving the while loop
                elif cont == 2:
                        status = True
                        print("The Battle Between",Player1,"and",Player2,"has come to an end")
                        if score1 > score2:
                                print(Player1,"emerges from the field victorious.",Player2,"must watch as his RPSLS skills are questioned.")
                        if score1 < score2:
                                print("What is greates in life?",Player2,"To crush your enemies, see them driven before you, and to hear the lamentation of",Player1,"'s women.")
                else:
                        status = False
                        print("I will take that as you want to continue for another round.")
#-- Weapon selection
def chooseweapon():
    try:
        #-- Get user input on the variable
        weapon = int(input("Please select 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, 5 for Spock:"))
        if weapon == 1: 
            print("Rock, a strong choice, one with earth.")
            return weapon
        elif weapon == 2:
            print ("Paper, ahhh intellectual, imaginative, trickery is afoot.")
            return weapon
        elif weapon == 3:
            print ("Scissors, yes metal, strong and unbendable are you.")
            return weapon
        elif weapon == 4:
            print ("Lizard, master of camoflague and venom.")
            return weapon
        elif weapon == 5:
            print ("Spock, number 1, Kirk's right hand man, master of logic.")
        else: #-- A little error checking for numbers greater than 6 and less than 1
            print ("You are daft.")
            chooseweapon()
    except:  #-- Mainly if they put in string data
              print("I have heard the trickery of your species, but please follow the rules!")
              chooseweapon()
    return weapon #-- return the value

#-- Computer chooses a weapon
def computerchoose():
        weapon = random.randrange(1,6) #-- random choice of weapons
        #-- Weapon results, mainly just wanted to have the computer tell you what it selected
        if weapon == 1:
                text = "ROCK"
                print ("It is my turn puny human, Fear the wrath of my: " ,text)
        elif weapon == 2:
                text = "PAPER"
                print ("It is my turn puny human, Fear the wrath of my: " ,text)
        elif weapon == 3:
                text = "SCISSORS"
                print ("It is my turn puny human, Fear the wrath of my: " ,text)
        elif weapon == 4:
                text = "LIZARD"
                print ("It is my turn puny human, Fear the wrath of my: " ,text)
        elif weapon == 5:
                text = "SPOCK"
                print ("It is my turn puny human, Fear the wrath of my: " ,text)
        return weapon

#-- Combat!!!
def combat (weapon1, weapon2):
        global score1 #-- Allow global variable of score1
        global score2 #-- Allow global variable of score2
        #-- The results of the selections
        if weapon1 == weapon2:
                print("You have tied, this isn't hockey!")
                score1= score1 + 1
                score2= score2 + 1
        elif weapon1 == 1 and weapon2 == 2:
                print("Paper Covers Rock!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 1 and weapon2 == 3:
                print("Rock Crushes Scissors!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 1 and weapon2 == 4:
                print("Rock Crushes Lizard!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 1 and weapon2 == 5:
                print("Spock Vaporizes Rock!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 2 and weapon2 == 1:
                print("Paper Covers Rock!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 2 and weapon2 == 3:
                print("Scissors Cut Paper!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 2 and weapon2 == 4:
                print("Lizard Eats Paper!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 2 and weapon2 == 5:
                print("Paper Disproves Spock!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 3 and weapon2 == 1:
                print("Rock Crushes Scissors!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 3 and weapon2 == 2:
                print("Scissors Cut Paper!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 3 and weapon2 == 4:
                print("Scissors Decapitate Lizard!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 3 and weapon2 == 5:
                print("Spock Smashes Scissors!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 4 and weapon2 == 1:
                print("Rock Crushes Lizard!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 4 and weapon2 == 2:
                print("Lizard Eats Paper!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 4 and weapon2 == 3:
                print("Scissors Decapitate Lizard!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 4 and weapon2 == 5:
                print("Lizard Poisons Spock!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 5 and weapon2 == 1:
                print("Spock Vaporizes Rock!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 5 and weapon2 == 2:
                print("Paper Disproves Spock!")
                score1= score1 + 0
                score2= score2 + 1
        elif weapon1 == 5 and weapon2 == 3:
                print("Spock Smashes Scissors!")
                score1= score1 + 1
                score2= score2 + 0
        elif weapon1 == 5 and weapon2 == 4:
                print("Lizard Poisons Spock!")
                score1= score1 + 0
                score2= score2 + 1

#-- Begin main call
rule_select(rule_selection)
#-- It still amuses me that most of the coding is done in the functions. Oh well.
