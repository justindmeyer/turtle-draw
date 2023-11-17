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

# The following code is from ChatGPT.
total_distance = 0
# End of ChatGPT code.

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
 
 # The following code is from ChatGPT. 
        if td.isdown():
            distance = td.distance(x, y)
            total_distance += distance
# End of ChatGPT code.

        window = Screen()
        window.setup(WIDTH, HEIGHT)
        td.color(color)
        td.goto(x,y)
        td.pendown()

    if (len(parts) == 1):
        td.penup()

td.goto(50, -150)
td.write(f"Total Distance is {total_distance:.2f}")

print()
turtleDrawTextFile.close()
print()
print("Program will not end until you press enter.")
input()
print()
turtle.bye()
print("Program ended.")