from turtle import Turtle , Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #self.goto(0 , 0)
        self.X_pos = 10
        self.Y_pos = 10
        self.move_speed = 0.1
        self.y_bounce()
        self.x_bounce()
        self.reset_position()

    def reset_position(self):
        self.goto(0 , 0)
        self.x_bounce()
        
    def move(self):
        new_x = self.xcor() + self.X_pos
        new_y = self.ycor() + self.Y_pos
        self.goto(new_x , new_y)
    
    def y_bounce(self):
        self.Y_pos *= -1
    def x_bounce(self):
        self.X_pos *= -1
        self.move_speed *= 0.9
    
     