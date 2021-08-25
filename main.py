import random
from turtle import Turtle as t, Screen
#import Turtle as t -> an alias in Python.
#for modules with a longer name, it might be easier to import as an alias to save some typing on your fingers

tim = t()
tom = t()
terry = t()
tina = t()

color_choice = ['maroon','medium violet red', 'gainsboro', 'light steel blue', 'powder blue', 'dark cyan', 'light green', 'lime green', 'goldenrod', 'red', 'purple', 'blue violet']


tim.shape('turtle')

""" tim.pu()
tim.goto(-50)
tim.pd() """

def draw_shape(number_of_sides):
    angle = (360 / number_of_sides)
    for _ in range(number_of_sides):
        #color_a = randint(0, 255)
        #color_b = randint(0, 255)
        #color_c = randint(0, 255)
        tim.color()
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3,21):
    tim.color(random.choice(color_choice))
    draw_shape(shape_side_n);

tim.color('#000000', '#84ae94')

#first attempt at drawing a series of shapes
""" #drawing a triangle
tim.color('pink')
for _ in range (3):
    tim.forward(100)
    tim.right(120)

#drawing a square
tim.color('purple')
for _ in range(4):
    tim.forward(100)
    tim.right(90)

#drawing a pentagon
tim.color('blue')
for _ in range(5):
    tim.forward(100)
    tim.right(72)

#drawing a hexagon
tim.color('orange')
for _ in range(6):
    tim.forward(100)
    tim.right(60)

#drawing a heptagon
tim.color('magenta')
for _ in range(7):
    tim.forward(100)
    tim.right(51.43)

#drawing an octagon
tim.color('black')
for _ in range(8):
    tim.forward(100)
    tim.right(45)

#drawing a nonagon
tim.color('green')
for _ in range(9):
    tim.forward(100)
    tim.right(40)

#drawing a decagon
tim.color('red')
for _ in range(10):
    tim.forward(100)
    tim.right(36)
 """

#first attempt to create dashed line in Turtle
#for steps in range(10):
""" for _ in range (10):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd() """


# different tests to see how it would render multiple turtles
""" tom.shape('turtle')
tom.color('blue')
tom.right(90)
for steps in range(4):
    tom.forward(100)
    tom.right(90)

terry.shape('turtle')
terry.color('purple')
terry.left(90)
for steps in range(4):
    terry.forward(100)
    terry.right(90)

tina.shape('turtle')
tina.color('pink')
tina.right(180)
for steps in range(4):
    tina.forward(100)
    tina.right(90) """






screen = Screen()
screen.exitonclick()