#SNake GAME by RAhul RAwat


import turtle
import time
import random

delay=0.1


wn=turtle.Screen()
wn.title("Snake Game @ RAHUL")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the screeen updates

#score
score=0
high_score=0

#snake HEad

head=turtle.Turtle()
head.speed(0) #animation speed
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction="stop" #start diction of the snake

#SnakeFood


food=turtle.Turtle()
food.speed(0) #animation speed
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)

segments = [] #list for the body of snake

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score:0", align="center", font=("Courier", 24, "bold"))

#Functions
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_left():
    if head.direction!="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
 
#Main game loop

while True:
    wn.update()#updates the screen
    #check for a collion with the border
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
       time.sleep(1)
       head.goto(0,0)
       head.direction="stop"

       #Hide the SEgMEnts
       for segment in segments:
           segment.goto(1000,1000)

       #clear the segment List
       segments.clear()

       score=0

       #RESET THE DELAYY
       delay =0.1
       
    #check for collison with food
    if head.distance(food)<20:
        #move the food to a random spot on the screen
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        food.goto(x,y)

        #ADD A SEGMENT
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.penup()
        new_segment.color("black")
        segments.append(new_segment)

        #sorten the dealy
        delay -=0.001

        #INCrease the score
        score +=10

        if score>high_score:
            high_score=score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center", font=("Courier", 24, "bold"))


    #Move the head segmesnts first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide the segmensts
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segment list
            segment.clear()

            #reset Score
            score=0

            #RESET THE DELAYY
            delay =0.1
            
            pen.clear()
            pen.write("Score: {} High Score:{}".format(score,high_score),align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)
wn.mainloop()
