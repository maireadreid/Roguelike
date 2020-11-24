# roguelike Room Objects - write your code here

#import necessary libraries
import numpy as np
from random import seed
from random import random
from IPython.display import clear_output

#define class of type room
class Room(): 
    """Model a Car."""
    def __init__(self, w, h): #initialise function 
        """Initialise"""
        self.w = w
        self.h = h
        self.x = 0 #initial x value
        self.y = 0 #initial y value
    
    #change the x variable to move it left or right
    def left(self):
        clear_output()
        if (self.x == 0):
            self.x = self.x
        else:
            self.x = self.x-1
    def right(self):
        clear_output()
        if (self.x > self.w-2):
            self.x = self.x
        else:
            self.x = self.x+1
            
    #change the y variable to move it up or down
    def up(self):
        clear_output()
        if(self.y == 0):
            self.y = self.y
        else:
            self.y = self.y-1
    def down(self):
        clear_output()
        if (self.y > self.h-2):
            self.y = self.y
        else:
            self.y = self.y+1
            
    #helper functions to use later
    def horizontalLine(self): 
        '''function to create the horizontal line frame'''
        print("+", end="") #print t he first "+"
        for column in range(self.w): #prints a line of "-"s which is c long
            print("-", end="")
        print("+")

    def emptyLine(self):
        '''function to create the empty line with no player'''
        print("|", end="") #prints the first "|"
        for column in range(self.w): #prints a line of "."s which is c long
            print(".", end="")
        print("|")

    def playerLine(self):
        '''function to create the line with player in specified location'''
        print("|", end="")#prints the first "|"
        for pcolumn in range(self.x):#prints a line of "."s which is x long
            print(".", end="")
        print("@", end="")#prints the player 
        for pcolumn in range(self.x, self.w-1):#prints however many "." are left after the player
            print(".", end="")
        print("|")
        
    #draw function    
    def draw(self):
        '''function to combine the functions into the final draw room'''
        self.horizontalLine() #prints the first horizontal line
        for t in range(self.y): #prints the empty line for as many rows as needed
            self.emptyLine()    
        self.playerLine() #prints the line with the player on it
        for p in range(self.y, self.h-1):#prints the rest of the lines with the empty lines
            self.emptyLine()    
        self.horizontalLine()


myRoom = Room(4, 4)
myRoom.draw()


while True:
    s = input()
    if s=='a': myRoom.left()
    if s=='s': myRoom.right()
    if s=='q': myRoom.up()
    if s=='z': myRoom.down()
    if s=='x': 
        print("all done")
        break
    myRoom.draw()
