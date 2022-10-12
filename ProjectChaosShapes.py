import turtle
import math as m
import random as r

def TurtleDotting(P):
    t.goto(P)
    t.pendown()
    t.dot()
    t.penup()
       
# Gets a screen up
s = turtle.getscreen()
turtle.title("Project Choas Shapes")

# Creates a turtle
t = turtle.Turtle()
t.pensize(2.5)
t.pencolor("teal")
t.penup()
t.speed(0)

# Turtle Commands
HH = 3
HH_X = m.sqrt(((HH * 100) ** 2) - ((HH * 100 / 2) ** 2))
HH_Y = HH * 100 / 2

# Hexagon Points
A = 0,HH * 100
TurtleDotting(A)
B = HH_X, HH_Y
TurtleDotting(B)
C = HH_X, HH_Y * -1
TurtleDotting(C)
D = 0,HH * -100
TurtleDotting(D)
E = HH_X * -1, HH_Y * -1
TurtleDotting(E)
F = HH_X * -1, HH_Y 
TurtleDotting(F)
H_Points = {"1": A, "2": B, "3": C, "4": D, "5": E, "6": F}

NP_C = 0,0
Destination = []

# Creating Chaos
for i in range(500):
    # Get the Old Position Points
    if i == 0:
        OP_C = H_Points["1"]
    else:
        OP_C = NP_C
    OP_X, OP_Y = OP_C

    # Get the Destination Points
    DP = str(r.randint(1,6))
    DP_C = H_Points[DP]
    while DP_C == OP_C:
        DP = str(r.randint(1,6))
        DP_C = H_Points[DP]
    
    DP_X, DP_Y = DP_C

    # Get the New Position
    ## X Cords
    if OP_X == DP_X:
        NP_X = OP_X
    elif OP_X > DP_X:
        NP_X = OP_X - abs((OP_X - DP_X) * (2/3))
    elif OP_X < DP_X:
        NP_X = OP_X + abs((OP_X - DP_X) * (2/3))
    ## Y Cords
    if OP_Y == DP_Y:
        NP_Y = OP_Y
    elif OP_Y > DP_Y:
        NP_Y = OP_Y - abs((OP_Y - DP_Y) * (2/3))
    elif OP_Y < DP_Y:
        NP_Y = OP_Y + abs((OP_Y - DP_Y) * (2/3))
    
    # Stitching and Plotting
    print(f"Turn {i+1}, going to point {DP}")
    Destination.append(DP)
    NP_C = NP_X, NP_Y
    TurtleDotting(NP_C)

freq = dict((i, Destination.count(i)) for i in set(Destination))
print(f'\n1 occured {freq.get("1")} times')
print(f'2 occured {freq.get("2")} times')
print(f'3 occured {freq.get("3")} times')
print(f'4 occured {freq.get("4")} times')
print(f'5 occured {freq.get("5")} times')
print(f'6 occured {freq.get("6")} times')
turtle.exitonclick()