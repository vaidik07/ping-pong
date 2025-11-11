from turtle import Turtle , Screen


class Paddle(Turtle):
    def __init__(self , X_coordinate , Y_coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len= 1, stretch_wid=5)
        self.penup()
        self.goto(X_coordinate , Y_coordinate)
        self.go_up()
        self.go_down()

    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor() , new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor() , new_y_cor)