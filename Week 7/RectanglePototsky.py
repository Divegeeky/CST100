#-- This Program was developed by Jason Pototsky
#-- 11/30/2013 for Week 7 Assignment 1
#-- For CST100 Object Oriented Software Development - 87955
#-- Instructor: Dr. Ajay Bansal
#------------------------------------- Region Global Variables --------------------------------------------------
#------------------------------------- End Region Global Variables -------------------------------------------
#------------------------------------- Region Objects -------------------------------------------------------------------
class Rectangle: #-- Rectangle Object

#-------- Initialization method ------------------#
    def __init__(self, x, y, width, length): #-- Parameters required to initialize the rectangle
        self.x = x #-- Create the X parameter for the rectangle
        self.y = y #-- Create the Y parameter for the rectangle
        self.width = width #-- Create the width parameter for the rectangle
        self.length = length #Create the length parameter for the rectangle
        
#-------- string return method (What do I print?) ------------------#
    def __str__ (self): #-- String return
        return "( x = " + str(self.x) + ", y = " + str(self.y) + ", width = " + str(self.width) + ", length = " + str(self.length) +")"
    #-- Outputs the Contents of the rectangle instead of the default Rectangle Object output

#--------Right edge method ------------------#
    def right(self): #-- Right Method
        return self.x + self.width #-- Adds the X value with the Width to get the constant for X for the rectangle

#-------- Bottom edge method ------------------#
    def bottom(self): #-- Bottom method
        return self.y + self.length #-- Adds the Y value with the length to get the constrant for Y for the rectangle

#-------- Size method ------------------#
    def size(self): #-- Size method
        return "( Width = " + str(self.width) + ", Length = " + str(self.length) +' )' #-- Returns a string pattern for the "size" of the rectangle

#-------- Position method ------------------#
    def position(self): #-- Position Method
        return "( X = " + str(self.x) + ",  Y = " + str(self.y) + " )" #-- Returns a string pattern for the location of the corner of the rectangle

#-------- Area method ------------------#
    def area(self): #-- Area method
        return self.width * self.length #-- Length Times Width for area of a rectangle

#-------- Expand method ------------------#
    def expand(self, offset): #-- Necessary parameters for the expand function
        newx = self.x - offset #-- make new X values for the new rectangle
        newy = self.y - offset #-- make new Y value for the new rectangle
        newlength = self.length + (offset*2) #-- make new length value for the new rectangle
        newwidth = self.width + (offset*2) #-- make new width value for the new rectangle
        expanded = Rectangle(newx,newy,newwidth,newlength) #-- Create new rectangle
        return expanded #-- Return the new object to the function
        
#-------- Contains_Point method ------------------#
    def contains_point ( self, xcont, ycont ): #-- Necessary parameters for the contains_point method
        if xcont > (self.x + self.width) or xcont < self.x: #-- If the X value is larger than the rectangles x+ width it does not fall in the rectangle or if it is smaller than the
                                                                            #-- corner of the rectangle
            value = False #-- value to return
        elif xcont <= (self.x + self.width) and xcont >= self.x: #-- If the x falls in the rectangle goto next
            if ycont <= (self.y + self.length) and ycont >= self.y: #-- Check the Y variable to see if if falls within the rectangle
                value = True #-- True dat yo
            else: #-- Y is not in the rectangle
                value = False #-- No Soup for you
        else: #-- Just in case
            value = False
        return value #-- Return the value for the method
        
#------------------------------------- End Region Objects -------------------------------------------------------------------
#------------------------------------- Region Functions -----------------------------------------------------------

#--- Main Function --- (I DO ALL THE WORK!)----
def mainfunction(): #-- No necessary parameters
    rectangle = makevalues() #-- Create rectangle with values that are received in the makevalues() function
    contin = 1 #-- initialize the contin variable for the loop
    while contin == 1: #-- While loop for contin
            methodlist=['expand',"contains_point", 'bottom', 'right', 'size', 'position', 'area', 'print'] #-- initialize the list with allowed entries
            method = input("Please input the name of the method you wish to utilize: acceptable answers are {0}".format(methodlist)) #-- I decided to try a little string formatting for
            #-- this assignment because it looked like the best way to accomplish this.
            
            if method == 'expand': #-- Expand method "call"
                offset = int(input("Please input the offset value: ")) #-- Get offset value
                expanded_rect = rectangle.expand(offset) #-- Create the new rectangle and store it in expanded_rect
                print("""The expanded rectangle is, {0}
While the original rectangle is, {1}""".format(expanded_rect, rectangle)) #-- I decided to output this so that you can see that rectangle was not modifed
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: ")) #--Continue?
                
            elif method =='contains_point': #-- Contains point method "call"
                xvalue = int(input("Please input the X Value you wish to see if it is within the rectangle: ")) #--X Value
                yvalue = int(input("Please input the Y Value you wish to see if it is within the rectangle: ")) #-- Y Value
                rectangle.contains_point(xvalue, yvalue) #-- See if the rectangle has the values in question
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: ")) #--Continue?
                
            elif method == 'bottom': #-- Bottom method call (Booty Call)
                print(rectangle.bottom()) #-- Print the resulting edge
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: ")) #--Continue?
                
            elif method == 'right': #-- Right method call 
                print(rectangle.bottom()) #-- Print the resulting edge
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: ")) #--Continue?

            elif method == 'size': #-- Size method call
                print(rectangle.size()) #-- Print the size (I thought it didn't matter)
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: "))#--Continue?

            elif method == 'position': #-- Position method call
                print(rectangle.position()) #-- Print the position of the X and Y coordinates
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: "))#--Continue?

            elif method == 'area': #-- Area method call
                print(rectangle.area()) #-- Print the area of the rectangle
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: "))#--Continue?

            elif method == 'print': #-- Here so you can see the __str__ method
                print(rectangle) #-- print the rectangle
                contin = int(input("Do you wish to run another method, create another rectangle or quit? 1 for another method, 2 for new rectangle, 3 to quit: "))#--Continue?

    if contin == 2: #-- New Rectangle time!
        mainfunction() #--- strart at the beginning

    if contin == 3: #-- Bye Bye
        print("Thank you, have a wonderful day! and thank you for playing with my rectangles.") #-- My little goodbye message

#--- Make Values Function --- (I take the values)
def makevalues(): #-- define the function
    try: #-- A little error checking
        xpoint = int(input("What is the X value for the beginning of the rectangle, should be the bottom left corner: ")) #-- What is the X Value
        ypoint = int(input("What is the Y value for the beginning of the rectangle, should be the bottom left corner: ")) #-- What is the Y Value
        length = int(input("What is the length of the rectangle? ")) #-- What do you want the length to be?
        width = int(input("What is the width of the rectangle? ")) #-- What do you want the width to be?
        rectangle = Rectangle(xpoint, ypoint, width, length) #-- Create the rectangle
        return rectangle # return the rectangle object to the main function
    except: #-- A little error checking
        print("You need to use integers please") #-- No String for you!
        makevalues() #-- Start again

#------------------------------------- End Region Functions -----------------------------------------------------
#------------------------------------- Region Main -------------------------------------------------------------------
mainfunction() #-- I looked into another way of doing this by using the if name == "__main__": function but I couldn't figure it out by the time it was necessary to
#-- Turn this in, however I will definitely be doing more python in the future!


#------------------------------------- End Region Main ------------------------------------------------------------
