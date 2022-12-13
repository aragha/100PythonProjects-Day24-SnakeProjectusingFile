from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.get_previous_highscore()
        self.update_scoreboard()

    def get_previous_highscore(self):
        with open("data.txt") as file:
            prev_highscore = file.read()
            if len(prev_highscore) > 0:
                self.high_score = int(prev_highscore)
                print(self.high_score)
    def save_new_highscore(self, score):
        with open("data.txt", "w") as file:
            file.write(str(score))
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_new_highscore(self.high_score)
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
