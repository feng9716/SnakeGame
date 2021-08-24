from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = -1;
        # Read high_score from file
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Rewrite high score
            with open("high_score.txt", mode = "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.write_score()
