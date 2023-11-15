import turtle
from turtle import Screen, Turtle

WIDTH = 450
HEIGHT = 450

print()
print("What file would you like to pull data from?")
TEXTFILE = input()
print()

print("Starting Turtle Draw.")
print()

td = turtle.Turtle()
td.speed(0)
td.penup()

print("Drawing with info from the given file:")
turtleDrawTextFile = open(TEXTFILE, "r")
line = turtleDrawTextFile.readline()
while line:
    print(line, end="")
    line = turtleDrawTextFile.readline()
    parts = line.split(" ")

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        window = Screen()
        window.setup(WIDTH, HEIGHT)
        td.color(color)
        td.goto(x,y)
        td.pendown()

    if (len(parts) == 1):
        td.penup()

print()
turtleDrawTextFile.close()
print()
print("Program will not end until you close the Turtle Graphics window.")
print()
turtle.done()
print("Program ended.")