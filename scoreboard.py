from turtle import Turtle, goto

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,260)
        self.color("white")
        self.write(f"Score : {self.score}",align="center",font=("Courier",24,"normal"))
        self.hideturtle()
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Courier",24,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over ! : {self.score}",align="center",font=("Courier",24,"normal"))