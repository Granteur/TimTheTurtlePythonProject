import random
from turtle import Turtle as t, Screen
#import Turtle as t -> an alias in Python.

#project requirements:
#   dot grid 10x10
#   each dot is 20px in diameter
#   each dot spaced 50px apart
Shelldon = t()
screen = Screen()
screen.colormode(255)

#this list was created using the colorgram module to pull colors from the source image.
colors = [(9, 22, 58), (40, 41, 129), (114, 94, 205), (56, 73, 167), (150, 120, 221), (86, 34, 117), (136, 53, 168), (59, 25, 80), (164, 83, 214), (181, 109, 229), (0, 2, 0), (1, 0, 0), (169, 166, 250), (187, 204, 254), (215, 154, 254), (226, 184, 255)]




#Changes the turtle shape from an arrow to a turtle, speeds him up, and 'lifts the pen' 
Shelldon.shape('turtle')
Shelldon.speed('fastest')
Shelldon.penup()

#Sets Shelldon's initial location at certain coordinates
Shelldon.goto((-250, -200))

#method which pulls a random color located in RGB format from a list I made called 'colors'
def get_color():
    color = random.choice(colors)
    return color
# Shelldon.color(random.randint(color_pallete()))

#method which causes 'Shelldon' turtle to pull a color from the get_color() method to paint dot with, paint a single dot, then move forward 50px ten Shelldones
def draw_row_of_dots():
    for _ in range (10):
        Shelldon.color(get_color())
        Shelldon.dot(20)
        Shelldon.penup()
        Shelldon.forward(50)

#method which moves Shelldon up the y-axis
def next_line():
    for _ in range (9):
        Shelldon.setx(-250)
        Shelldon.sety(Shelldon.ycor() + 5)

""" #early first attempt at what became the 'next_line' method    
    Shelldon.left(90)
    Shelldon.forward(50)
    Shelldon.left(90)
    Shelldon.forward(250)
    Shelldon.left(180)
    Shelldon.setx(-250)
    Shelldon.sety(+10) 
    
    early second attempt at what became the 'next_line' method
    #Shelldon.goto(-250, y=None)
    # """
    
    
for _ in range (10):
    draw_row_of_dots()
    Shelldon.penup()
    next_line()

#hides Shelldon after completing the picture
Shelldon.ht()
    

screen.exitonclick()
