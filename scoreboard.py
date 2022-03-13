from turtle import Turtle

SCORE = 0
ALLIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.refresh()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", False, ALLIGNMENT, FONT)
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score}", False, ALLIGNMENT, FONT)
        self.hideturtle()