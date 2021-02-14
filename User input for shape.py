#Justin Mitchell 2/14/2021
#Program is supposed to ask user the 3 questions about their shape and draw it.
#I could not get this program to work, I am getting a non-int error because of how I have the turtle set. "Float" is not working anywhere I put it.
sides = input("How many sides?")

length = input("What is the length of the side?")

col = input("What is the color of the line?")

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for drawing in range(2):
    
    alex.forward(length)
    alex.right(sides)
    alex.color(col)

