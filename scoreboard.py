from turtle import Turtle , Screen


class Scoreboard(Turtle):
    def __init__(self , X_coor , Y_coor):
        super().__init__()
        self.score =0
        self.color("white")
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Prevent drawing lines
        self.goto(X_coor , Y_coor)
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    

