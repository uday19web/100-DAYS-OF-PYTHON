from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!!", align="center", font=FONT)