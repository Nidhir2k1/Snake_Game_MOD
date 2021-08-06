from scoreboard import Scoreboard
from food import Food
from turtle import Screen, Turtle, pencolor, position, screensize
import turtle
import time
from food import Food
from snake import Snake
import random

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Ultimate Snake Game")
screen.tracer(0)

#TELEPORT FIXED ENTRY GATE
tim=Turtle()
tim.hideturtle()
tim.pencolor("green")
tim.penup()
tim.goto(200,-200)
tim.color("black", "green")
tim.begin_fill()
tim.circle(20)
tim.end_fill()

#FOR TELEPORT EXIT GATE
ex=Turtle()
ex.penup()
ex.goto(-200,200)
ex.color("black", "red")
ex.begin_fill()
ex.circle(20)
ex.end_fill()

#FOR TELEPORT ENTRY  GATE 
class Tom():
    def __init__(self) -> None:
        pass
    tom=Turtle()
    tom.clear()
    tom.hideturtle()
    tom.pencolor("green")
    tom.penup()
    tom.goto(random.randint(-250,250),random.randint(-250,250))
    tom.color("red", "green")
    tom.begin_fill()
    tom.circle(20)
    tom.end_fill()
    print("called")

### FOR CLONE MODE ####
def refresh_tp():     
        
        nid=Turtle()
        nid.color("blue")
        nid.speed(0)
        nid.shapesize(stretch_len=0.6,stretch_wid=0.5)
        nid.shape("turtle")
        random_x=random.randint(-250,250)
        random_y=random.randint(-250,250)
        nid.goto(random_x,random_y)

turtle.onkeypress(refresh_tp,"c")

ex=Turtle()



tom=Tom
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
     
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()
        refresh_tp()       # FOR CLONE MODE
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
    if snake.head.distance(tim) < 30 :
        snake.tp()
    elif snake.head.distance(Tom.tom) < 30 :
        snake.tp()
       











screen.exitonclick()
