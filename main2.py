from turtle import Screen, Turtle
from boxes import Boxes
from obstacles import Obstacle
import time

# Setup screen
screen = Screen()
screen.title("Turtle Race with Obstacles")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create objects
boxes = Boxes()
obstacles = Obstacle(count=15)

# Score display
score = 0
start_time = time.time()

score_display = Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(-270, 260)
score_display.write("Score: 0", font=("Arial", 16, "normal"))

# Game Over display
game_over_display = Turtle()
game_over_display.hideturtle()
game_over_display.color("yellow")
game_over_display.penup()

# Keyboard controls
screen.listen()
screen.onkey(boxes.up, 'w')
screen.onkey(boxes.down, 's')
screen.onkey(boxes.left, 'a')
screen.onkey(boxes.right, 'd')

# Main loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    obstacles.move_obstacles()

    # Update score
    score = int(time.time() - start_time)
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

    # Check collision
    if obstacles.detect_collision(boxes):
        game_on = False
        game_over_display.goto(0, 0)
        game_over_display.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
        game_over_display.goto(0, -40)
        game_over_display.write(f"Your Score: {score}", align="center", font=("Arial", 20, "normal"))

screen.mainloop()
