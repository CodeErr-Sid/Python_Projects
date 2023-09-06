from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 13, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
