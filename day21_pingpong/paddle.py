from turtle import Turtle

LENGTH_PADDLE = 1
WIDTH_PADDLE = 5


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH_PADDLE, stretch_len=LENGTH_PADDLE)
        self.penup()
        self.goto(x=x_pos, y=y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
