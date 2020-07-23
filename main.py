import turtle
import math
s = turtle.screen

def shape(sides, size):
	for i in range(sides):
		t.fd(size)
		t.rt(360.0/sides)

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
    t.color("red")
    t.fd(steps)
    t.rt(degrees)
    steps += increase
    t.color("blue")

#spiralstar(100, 556, 4)

def spirotriangle(lines, degrees, increase):
  steps = 2
  for i in range(lines):
    t.fd(steps)
    t.rt(degrees)
    steps += increase
    t.color("red")
    t.fd(steps)
    t.rt(degrees)
    steps += increase
    t.color("blue")

#spirotriangle(320, 119, 2)


def sphere(size):
	shade = 125
	t.color(0,0,shade)
	while size > 0:
		t.begin_fill()
		shape(30, size)
		t.end_fill()
		size -= .5
		shade += 5
		t.color(0,0,shade)
  
#sphere(100, 10, 50)

def pattern():
  steps = 3
  for i in range(lines):
    t.fd(steps)
    t.rt(degrees)
    steps += increase

s.onkey(pattern, "space")
s.listen()