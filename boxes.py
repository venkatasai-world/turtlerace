from turtle import Turtle

class Boxes(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("turtle")
        self.goto(0, -290)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)

    def left(self):
        self.setx(self.xcor() - 20)

    def right(self):
        self.setx(self.xcor() + 20)
