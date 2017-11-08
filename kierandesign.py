import turtle
from myfunctions import *
turtle.colormode(255) 


bob = turtle.Turtle()
bob.speed(0)
turtle.bgcolor("orange")


bob.width(4)

for times in range(10):
    bob.color(17,0,255)
    design(bob,45,30)
    bob.forward(20)
    bob.left(45)
    

bob.width(4)
bob.left(40)
for times in range(10):
    bob.color(0,255,255)
    design(bob,45,30)
    bob.forward(20)
    bob.left(45)


bob.width(4)
bob.left(60)

for times in range(10):
    bob.color(102,255,178)
    design(bob,45,30)
    bob.forward(20)
    bob.left(45)

"""
secound circle
"""


bob.width(4)

for times in range(10):
    bob.color(17,0,255)
    
    bob.penup()
    bob.goto(500,-300)
    bob.pendown()
    design(bob,20,30)
    bob.forward(20)
    bob.left(45)
    

bob.width(4)
bob.left(40)
for times in range(10):
    bob.color(0,255,255)
    design(bob,20,30)
    bob.penup()
    bob.goto(500,-300)
    bob.pendown()
    bob.forward(20)
    bob.left(45)

bob.width(4)
bob.left(60)
for times in range(10):
    bob.color(102,255,178)   
    design(bob,20,30)
    bob.penup()
    bob.goto(500,-300)
    bob.pendown()
    bob.forward(20)
    bob.left(45)



"""
third cirlce
"""

bob.width(4)

for times in range(10):
    bob.color(17,0,255)
    
    bob.penup()
    bob.goto(-500,-300)
    bob.pendown()
    design(bob,20,30)
    bob.forward(20)
    bob.left(45)
    

bob.width(4)
bob.left(40)
for times in range(10):
    bob.color(0,255,255)
    design(bob,20,30)
    bob.penup()
    bob.goto(-500,-300)
    bob.pendown()
    bob.forward(20)
    bob.left(45)

bob.width(4)
bob.left(60)
for times in range(10):
    bob.color(102,255,178)   
    design(bob,20,30)
    bob.penup()
    bob.goto(-500,-300)
    bob.pendown()
    bob.forward(20)
    bob.left(45)




