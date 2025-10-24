from turtle import Turtle

class State(Turtle):
    def __init__(self, x, y, user_input):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write(user_input)