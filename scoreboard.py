from turtle import Turtle

FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Courier", 20, "normal"))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -20)
        self.write("GAME OVER", align="center", font=FONT)



