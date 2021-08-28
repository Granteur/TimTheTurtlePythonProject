import random
from turtle import Turtle as t, Screen
#import Turtle as t -> an alias in Python.
#for modules with a longer name, it might be easier to import as an alias to save some typing on your fingers

tim = t()

screen = Screen()
screen.colormode(255)

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    color_mixer = (red, green, blue)
    return color_mixer



#Changes the turtle shape from an arrow to a turtle
tim.shape('turtle')



#Speeds up tim from default speed
tim.speed('fastest')
#the turtle automatically orients east at '0', this gives options for North, West, and South at 90, 180, and 270 respectively
#cardinal_directions = [0, 90, 180, 270]
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        #circle method causes tim to draw a circle
        tim.circle(100)

draw_spirograph(90)
draw_spirograph(60)
draw_spirograph(50)


#reset method centers Tim after he's done drawing
#tim.reset()
#tim.color('#000000', '#84ae94')


screen.exitonclick()
