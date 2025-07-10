from turtle import Turtle
import random

class Obstacle:
    def __init__(self, count=10):
        self.blocks = []
        for _ in range(count):
            block = Turtle("square")
            block.penup()
            block.color("red")
            size = random.uniform(0.8, 2.0)
            block.shapesize(stretch_wid=size, stretch_len=size)
            block.speed(0)
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            block.goto(x, y)
            self.blocks.append(block)

    def move_obstacles(self):
        for block in self.blocks:
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            new_x = block.xcor() + dx
            new_y = block.ycor() + dy
            if -280 < new_x < 280 and -280 < new_y < 280:
                block.goto(new_x, new_y)

    def detect_collision(self, player):
        for block in self.blocks:
            if player.distance(block) < 25:  # Tune based on block size
                return True
        return False
