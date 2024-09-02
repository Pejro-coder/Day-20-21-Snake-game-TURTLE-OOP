from turtle import Turtle

COORDINATE = 290


class Edge(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pencolor("yellow")
        self.pensize(2)
        self.hideturtle()
        self.penup()
        self.goto(-COORDINATE, COORDINATE)

        self.pendown()
        self.goto(COORDINATE, COORDINATE)
        self.goto(COORDINATE, -COORDINATE)
        self.goto(-COORDINATE, -COORDINATE)
        self.goto(-COORDINATE, COORDINATE)
