from turtle import Turtle

FONT = ("courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290, 277)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center", font=FONT)
