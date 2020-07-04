"""
COMPUTER GRAPHICS PROJECT.

Problem statement is to design an Analog Clock using graphics.

Team members:
    Marmik Sharma 
    Vivek Gusain 
    Mayank Singh 
"""

import turtle
import time

# Creating a screen for display with black background
# and a resolution of standard 720p.
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=1280, height=720)
window.title("Not so simple Analog Clock")

# Creating pen for drawing objects.
# Pen is hidden so that it doesn't appear on-screen.
# Animation speed set to minimum for fastest drawing.
# There are 3 pens for different purposes.
# Using different pens to make objects exclusive of one another.


pen = turtle.Turtle() # For Analog clock only.
pen2 = turtle.Turtle() # For text related objects only.
pen3 = turtle.Turtle() # For digital clock only.
pen.hideturtle()
pen4 = turtle.Turtle() #For randomised artifacts.
pen2.hideturtle()
pen3.hideturtle()
pen4.hideturtle()
pen.speed(0)
pen2.speed(0)
pen3.speed(0)
pen4.speed(0)
pen.pensize(4)
pen4.pensize(1)

def pen_reset(angle):
    """ Snippet funtion to reset the pen and set 
        the direction to draw.
    """
    pen.up()
    pen.home()
    pen.setheading(angle)

def text_info(pen2):
    pen2.goto(0,-300)
    pen2.color('white')
    pen2.pendown()
    pen2.write("Please wait\n\nSimulating clock...\n\nretrieving time from OS", move=False, align="center", font=("Arial", 12, "bold"))
    pen2.penup()
    
def digital_clock(pen3):
    """
        Function to create a digital clock for the reference and ease
        of evalutaion of the main analog clock. 
    """
    pen3.home()
    pen3.up()
    pen3.setheading(90)
    pen3.goto(450, -10)
    pen3.color('yellow')
    pen3.pendown()
    pen3.write(time.strftime("%I:%M:%S"), move=False, align="center", font=("Arial", 30, "bold"))
    pen3.penup()
    pen3.clear()

def clock_hands(x, mode):
    """ Here we will have three modes corresponding 
        to hour, minute and second hand.
            mode 0 --- hour
            mode 1 --- minute
            mode 2 --- second
    """
    if mode==0:
        angle = (x/12) * 360
        pen.color('green')
        pen.pensize(8)
        len = 150
    elif mode==1:
        angle = (x/60) * 360
        pen.color('yellow')
        pen.pensize(4)
        len = 250
    elif mode==2:
        angle = (x/60) * 360
        pen.color('red')
        pen.pensize(4)
        len = 200
    else:
        print("Please select correct mode")
    
    pen.right(angle)
    pen.pendown()
    pen.forward(len)
    pen_reset(90)
    

def clock_body(pen, hrs=0, min=0, sec=0):
    """ Under this fuction we'll try to draw a frame for our clock.
        Which should probably include a circle and 12 lines to mark the hours.
        Note : --- Here origin (0,0) is at the center of the screen. 
               ---setheading(angle) sets the direction in which we'll draw.
    """
    # To draw outer frame of the clock
    pen.up()
    pen.goto(x=0,y=300)
    pen.setheading(to_angle=180)
    pen.color("blue")
    pen.pensize(8)
    #pen.fillcolor("grey")
    pen.pendown()
    #pen.begin_fill()
    pen.circle(radius=300)
    pen.pensize(4)
    #pen.end_fill()
    
   
    # Marking hours and minutes on the clock
    pen_reset(90)

    for _ in range(60):
        pen.forward(295)
        pen.color('orange')
        pen.pendown()
        # Omitting dots to avoid overlap with hour markings.
        if _%5!=0:
            pen.dot(size=5)
        pen.penup()
        pen.goto(x=0, y=0)
        pen.right(6)
        
    pen_reset(90)
    pen2.setheading(60)

    

    for _ in range(1,13):
        pen.forward(280)
        pen.color("green")
        pen.pendown()
        pen.forward(15)
        pen.penup()
        pen.goto(x=0, y=0)
        pen.right(30)
        

    pen_reset(90)
    clock_hands(hrs, mode=0)
    clock_hands(min, mode=1)
    clock_hands(sec, mode=2)

    pen.up()
    pen.goto(0,0)
    pen.color("black")
    pen.dot(20)

def Numbers(pen):
    pen2.home()
    pen.setheading(60)
    pen2.color('white')
    for _ in range(1,13):
        pen2.forward(260)
        pen2.pendown()
        pen2.write(_, move=False, align="center", font=("Arial", 16, "bold" ))
        pen2.penup()
        pen2.goto(x=0, y=0)
        pen2.right(30)

def random_artifacts(pen4, pen2):
    pen4.penup()
    pen4.goto(0,0)
    pen4.color('white')
    
    for i in range(35):
        text_info(pen2)
        pen4.setheading(i*60)
        pen4.forward(i)
        pen4.pendown()
        pen4.circle(15)
        pen4.circle(40)
        pen4.penup()
    pen2.clear()
    pen2.home()

#text_info(pen2)   
random_artifacts(pen4,pen2)
window.tracer(0)

while True:
    """ Now we need to run an infinite loop to refresh our clock every second.
        Here, we will use python's time library to extract time from the OS and then
        display it on our clock.
    """
   
    hrs = float(time.strftime("%I")) + float(time.strftime("%M"))/60
    min = float(time.strftime("%M"))
    sec = float(time.strftime("%s"))

    clock_body(pen, hrs, min, sec)
    
    
    Numbers(pen2)
    window.update()
    digital_clock(pen3)
    time.sleep(1)
    pen.clear()


# This line is important to keep the screen from closing immediately.
window.mainloop()