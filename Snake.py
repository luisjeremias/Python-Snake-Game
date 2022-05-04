from turtle import Turtle

INITIAL_POSITIONS = [(0,0),(20,0),(40,0)]
UP_POSITION = 90
DOWN_POSITION = 270
LEFT_POSITION = 180
RIGHT_POSITION = 0

class SnakeBody(Turtle):
  def __init__(self) -> None:
    self.snake_segments = []
    self.create_snake()
    self.snake_head = self.snake_segments[0]
   
  def create_snake(self):
    for position in INITIAL_POSITIONS:
      self.add_segment(position)

  def add_segment(self,position):
    tr = Turtle('square')
    tr.speed('slow')
    tr.color('white')
    tr.penup()
    tr.goto(position)
    self.snake_segments.append(tr)

  def snake_extend(self):
    self.add_segment(self.snake_segments[-1].position())
    
  def snake_move(self):
    for i in range(len(self.snake_segments) - 1, 0, -1):
      new_x = self.snake_segments[i -1].xcor()
      new_y = self.snake_segments[i -1].ycor()
      self.snake_segments[i].goto(new_x,new_y)
    self.snake_segments[0].forward(20)
  
  def snake_move_up(self):
    if self.snake_head.heading() != DOWN_POSITION:
      self.snake_head.setheading(UP_POSITION)

  def snake_move_down(self):
    if self.snake_head.heading() != UP_POSITION:
      self.snake_head.setheading(DOWN_POSITION)

  def snake_move_left(self):
    if self.snake_head.heading() != RIGHT_POSITION:
      self.snake_head.setheading(LEFT_POSITION)

  def snake_move_right(self):
    if self.snake_head.heading() != LEFT_POSITION:
      self.snake_head.setheading(RIGHT_POSITION)
