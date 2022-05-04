from turtle import Screen
import time
from Snake import SnakeBody
from Food import SnakeFood
from Score import SnakeScore

screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor('black')
screen.tracer(0)

game_on = True

snake = SnakeBody()
food = SnakeFood()
score = SnakeScore()

screen.listen()

screen.onkey(snake.snake_move_up,'Up')
screen.onkey(snake.snake_move_down,'Down')
screen.onkey(snake.snake_move_left,'Left')
screen.onkey(snake.snake_move_right, 'Right')

while game_on:
  screen.update()
  time.sleep(0.1)
  snake.snake_move()

  if snake.snake_head.distance(food) < 15:
    food.new_food_position()
    snake.snake_extend()
    score.add_score()

  if snake.snake_head.xcor() > 250 or snake.snake_head.xcor() < -250 or snake.snake_head.ycor() > 250 or snake.snake_head.ycor() < -250:
    game_on = False
    score.game_over()

  for segment in snake.snake_segments[3:]:
    if snake.snake_head.distance(segment) < 10:
      game_on = False

screen.exitonclick()