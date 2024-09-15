import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
tim=Turtle()
tim.shape("arrow")
tim.hideturtle()

colors_list=[(32, 107, 148), (224, 154, 87), (213, 131, 158), (6, 52, 93), (118, 172, 194), (34, 132, 81), (148, 80, 31), (19, 169, 203), (207, 156, 18), (229, 210, 103), (138, 25, 44), (210, 90, 121), (141, 183, 166), (10, 100, 57), (13, 64, 126), (222, 213, 7), (11, 44, 35), (81, 81, 20), (224, 169, 192), (58, 51, 11), (138, 61, 85), (3, 89, 115), (168, 207, 187), (240, 171, 155), (72, 157, 107), (157, 25, 16)]

def painting():
    vertical=-225
    for i in range(10):
        tim.teleport(-225,vertical)
        vertical+=50
        for j in range(10):
            tim.penup()
            tim.dot(20, random.choice(colors_list))
            tim.fd(50)

painting()

screen = Screen()
screen.exitonclick()
