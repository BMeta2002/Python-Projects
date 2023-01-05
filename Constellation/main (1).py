#Aries Connstellation

import turtle #imported turtle and time 
import time
import random
from turtle import *

turtle.Turtle()
window = turtle.Screen()
window.setup (width=1.0, height=1.0, startx=0, starty=0)
turtle.pensize(1)
turtle.shape("turtle")
turtle.hideturtle()

#This function shows the splash page 
def firstPage():
    turtle.color('black')
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.write("Welcome!", font=("Courier",30,'italic'),align='center')
    turtle.right(90)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write("The Aries Constellation", font=    ("Courier",30,'italic'),align='center')
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write("Bilal Malik", font=("Courier",30,'italic'),align='center')

firstPage()

time.sleep(1)#Here page will be displayed for 10 seconds
turtle.clear()#this clears the window

#In this function the second page displays, could only import gif images
def secondPage():
    window.bgpic('aries-1.gif')
    turtle.color('white')
    time.sleep(5)
secondPage()

window.clear()

#In this function, the constellation appears in white background
def thirdPage():
   
    #moved the turtle to top left of the page to start.I could also 
    #use the goto(), but realized it later
    #This was my first step to start the code
    
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.dot(10)
  
    #main diagram begins
    turtle.dot
    turtle.write("Mesarthim",font=("Courier",8,'bold'))
    turtle.delay(5)
    turtle.left(-45)
    turtle.forward(-100)
    turtle.dot(15)
    turtle.write("Sheratan",font=("Courier",8,'bold'))
    turtle.delay(5)
    turtle.right(-10)
    turtle.forward(-100)
    turtle.dot(10)
    turtle.write("Hamal",font=("Courier",8,'bold'))
    turtle.delay(5)
    turtle.right(-18)
    turtle.forward(-200)
    turtle.dot(5)
    turtle.write("41 Ari",font=("Courier",8,'bold'))
    turtle.pendown
    
  
thirdPage()
time.sleep(5)
window.clear()
#In this function the dots appears before and the lines get connected after wards
def upgrade():
    window.bgpic('sky.gif')
    turtle.color('yellow')
    time.sleep(2)
    

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.dot(15)
    turtle.delay(3)

    turtle.penup()
    turtle.goto(-40, 80)
    turtle.pendown()
    turtle.dot(15)
    turtle.delay(3)

    turtle.penup()
    turtle.goto(-170 , 140)
    turtle.pendown()
    turtle.dot(15)
    turtle.delay(3)

    turtle.penup()
    turtle.goto(-500 , 190)
    turtle.pendown()
    turtle.dot(15)
    turtle.delay(3)

    time.sleep(5)

    #the dots starts to get connected
    turtle.penup()
    turtle.goto(0 , 0)
    turtle.pendown()
    turtle.goto(-40, 80)
    turtle.goto(-170, 140)
    turtle.goto(-500, 190)
    turtle.pendown()
    turtle.write("The Aries Constellation",font=("Courier",12,'bold'))

upgrade()
time.sleep(5)
window.clear()


