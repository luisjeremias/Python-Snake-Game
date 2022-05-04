from turtle import Turtle

class SnakeScore(Turtle):
  def __init__(self):
    super().__init__()
    self.game_score = 0
    self.color('blue')
    self.hideturtle()
    self.penup()
    self.goto(0,-230)
    self.write_score()
  
  def write_score(self):
    self.write(arg=f'Score: {self.game_score}',align='center',font=('fira code',18,'bold'))

  def game_over(self):
    self.goto(0,0)
    self.color('red')
    self.write(arg=f'Game Over',align='center',font=('fira code',18,'bold'))
  
  def add_score(self):
    self.game_score += 1
    self.clear()
    self.write_score()