from turtle import Turtle, up, xcor
import random
import turtle
MOVE_DISTANCE=20
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color


class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.head =self.segments[0]
        
    def create_snake(self):
        self.head=Turtle()
        self.head.turtlesize(stretch_len=1.5,stretch_wid=1.3,)
        self.head.penup()
        self.head.shape("circle")
        self.head.color(random_color())
        self.segments.append(self.head)
        
        

        self.body=Turtle()
        self.body.penup()
        self.body.shape("square")
        self.body.color("white")
        self.body.goto(x=-20,y=0)
        self.segments.append(self.body)


        self.tail=Turtle()
        self.tail.penup()
        self.tail.shape("square")
        self.tail.color(random_color())
        self.tail.goto(x=-40,y=0)
        self.segments.append(self.tail)

    def add_segment(self):
        self.new_segment=Turtle()
        self.new_segment.penup()
        self.new_segment.shape("square")
        self.new_segment.color(random_color())
        self.new_segment.goto(x=self.tail.xcor(),y=self.tail.ycor())
        self.segments.append(self.new_segment)
    

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].fd(MOVE_DISTANCE) 

    def tp(self):
        self.head.setheading(0)
        self.segments[0].goto(-200,200)

    
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)
    def right (self):
        if self.head.heading() != 180:
            self.head.setheading(0)