import turtle as turtle_module
import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(100):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = turtle_module.Screen()
screen.exitonclick()
