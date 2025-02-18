from os import remove
from turtle import Turtle

COLORS = ["purple", "red", "blue", "yellow", "green"]
X_LOC = -320
Y_LOC = 200
Y_INCREMENT = 45

class Brick(Turtle):

    def __init__(self):
        self.all_bricks = []
        # self.bricks_to_remove = []
        super().__init__()
        self.penup()

    def create_bricks(self):
        for num in range(len(COLORS)):

            if COLORS[num] == "purple":
                for x in range(8):
                    brick = Turtle("square")
                    brick.shapesize(stretch_wid=2, stretch_len=5)
                    brick.color(COLORS[num])
                    brick.penup()
                    x_pos = X_LOC - 55 + (x * 105)
                    brick.goto(x_pos, Y_LOC)
                    self.all_bricks.append(brick)

            if COLORS[num] == "red":
                for x in range(7):
                    brick = Turtle("square")
                    brick.shapesize(stretch_wid=2, stretch_len=5)
                    brick.color(COLORS[num])
                    brick.penup()
                    x_pos = X_LOC + x * 105
                    brick.goto(x_pos, Y_LOC - (Y_INCREMENT * num))
                    self.all_bricks.append(brick)

            if COLORS[num] == "blue":
                for x in range(8):
                    brick = Turtle("square")
                    brick.shapesize(stretch_wid=2, stretch_len=5)
                    brick.color(COLORS[num])
                    brick.penup()
                    x_pos = X_LOC - 55 + (x * 105)
                    brick.goto(x_pos, Y_LOC - (Y_INCREMENT * num))
                    self.all_bricks.append(brick)

            if COLORS[num] == "yellow":
                for x in range(7):
                    brick = Turtle("square")
                    brick.shapesize(stretch_wid=2, stretch_len=5)
                    brick.color(COLORS[num])
                    brick.penup()
                    x_pos = X_LOC + x * 105
                    brick.goto(x_pos, Y_LOC - (Y_INCREMENT * num))
                    self.all_bricks.append(brick)

            if COLORS[num] == "green":
                for x in range(8):
                    brick = Turtle("square")
                    brick.shapesize(stretch_wid=2, stretch_len=5)
                    brick.color(COLORS[num])
                    brick.penup()
                    x_pos = X_LOC - 55 + (x * 105)
                    brick.goto(x_pos, Y_LOC - (Y_INCREMENT * num))
                    self.all_bricks.append(brick)

    def remove_brick(self, brick):
        brick.hideturtle()
        if brick in self.all_bricks:
            self.all_bricks.remove(brick)

