import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("purple")

def spiral(lines, degrees, increase):
  steps = 3
  for i in range(lines):
    t.fd(steps)
    t.rt(degrees)
    steps += increase

#spiral(100, 90, 5)

def spiralstar(lines, degrees, increase):
  steps = 7
  for i in range(lines):
    t.fd(steps)
    t.rt(degrees)
    steps += increase

#spiralstar(200, 556, 4)

def triangle(lines, degrees, increase):
  steps = 2
  for i in range(lines):
    t.fd(steps)
    t.rt(degrees)
    steps += increase

#triangle(100, 120, 3)
