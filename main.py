import turtle
import math
s = turtle.Screen()

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
	sides = 5
	spiralstar(lines = 100, degrees = 360/sides + 1, increase = .5)

def moveturtle(x, y):
	t.penup()
	t.goto(x,y)
	t.pendown()

s.onkey(pattern, "space")
s.onclick(moveturtle)
s.listen()

def bump(level, size):
	if level == 1:
		t.fd(size)
		t.lt(60)
		t.fd(size)
		t.rt(120)
		t.fd(size)
		t.lt(60)
		t.fd(size)
	elif level > 1:
		bump(level - 1, size)
		t.lt(60)
		bump(level - 1, size)
		t.rt(120)
		bump(level - 1, size)
		t.lt(60)
		bump(level - 1, size)

def snowflake(level, size):
	for i in range(3):
		bump(level, size)
		t.rt(120)
t.penup()
t.goto(-225, 0)
t.pendown()
snowflake(level = 3, size = 5)



s.onkey(pattern, "space")
s.onclick(moveturtle)
s.listen()

t.ondrag(t.goto)
