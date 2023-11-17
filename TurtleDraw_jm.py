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

total_distance_all = 0
total_distance_spaces = 0
last_position = td.position()

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

        '''Following code from ChatGPT.'''
        current_position = (x, y)
        segment_distance = td.distance(last_position[0], last_position[1])
        total_distance_all += segment_distance
        last_position = current_position
        '''ChatGPT code done.'''

    if (len(parts) == 1):
        td.penup()

        '''Following code from ChatGPT.'''
        current_position = (x, y)
        segment_distance = td.distance(last_position[0], last_position[1])
        total_distance_spaces += segment_distance
        last_position = current_position
        '''ChatGPT code done.'''

        total_distance = total_distance_all - total_distance_spaces

td.goto(50, -150)
td.write(f"Total Distance is {total_distance:.2f}")

print()
turtleDrawTextFile.close()
print()
print("Program will not end until you click on the Turtle Graphics window.")
print()
turtle.exitonclick()
print("Program ended.")