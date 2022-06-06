from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0.0, 0.0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


