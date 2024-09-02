from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from edge import COORDINATE, Edge
import time


COORDINATE = COORDINATE - 20

def reset():
    snake.snake_reset()
    scoreboard.reset_score()
    time.sleep(1)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snake game")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

snake = Snake()
food = Food()
scoreboard = Scoreboard()
edge = Edge()

screen.update()
time.sleep(1)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    snake.snake_move()
    screen.update()

# detect collision with dot
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

# detect collision with border
    if snake.head.xcor() > COORDINATE or snake.head.ycor() > COORDINATE \
            or snake.head.xcor() < -COORDINATE or snake.head.ycor() < -COORDINATE:
        reset()

    for position in snake.segments[1:]:
        if snake.head.distance(position) < 10:
            print("hit")
            reset()

screen.exitonclick()

# # print("-------------")
# # print(snake.head.position())
# for segment in snake.segments:
#     if segment == snake.head:
#         pass
#     elif snake.head.distance(segment) < 10:
#         print("hit")
#         scoreboard.game_over()
#         screen.update()
#         game_is_on = False
#         time.sleep(6)
#         exit()
