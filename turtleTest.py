import turtle
import os

s = turtle.getscreen()
t = turtle.Turtle()

s.setup(1920, 1080)

turtle.title("LogicoGames.com")
t.fillcolor("red")
t.pencolor("blue")
t.shape("circle")
t.pensize(1)
t.speed(500)

t.goto(0, -400)

n=10
while n <= 500:
    t.circle(n)
    n += 10

