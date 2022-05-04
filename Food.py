from turtle import Turtle
import random

class SnakeFood(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.shapesize(0.5,0.5)
    self.color('orange')
    self.penup()
    self.new_food_position()
  
  def new_food_position(self):
    new_x = random.randint(-235,235)
    new_y = random.randint(-235,235)
    self.goto(new_x, new_y)
