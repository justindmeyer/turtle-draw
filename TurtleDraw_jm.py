import turtle

TEXTFILE = "turtle-draw.txt"

print("Starting Turtle Draw...")
print()

turtleDrawTextFile = open(TEXTFILE, "r")
line = turtleDrawTextFile.readline()
while line:
    print(line, end="")
    line = turtleDrawTextFile.readline()

print()
print()
print("End")