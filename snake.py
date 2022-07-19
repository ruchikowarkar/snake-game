from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            self.increase_length(x, y)
            x -= 20

    def increase_length(self, x, y):
        self.snake.append(Turtle(shape="square"))
        pos = len(self.snake) - 1
        self.snake[pos].color("white")
        self.snake[pos].penup()
        self.snake[pos].setx(x)
        self.snake[pos].setx(y)

    def move(self):
        x = self.snake[0].xcor()
        y = self.snake[0].ycor()
        self.snake[0].forward(20)
        for i in range(1, len(self.snake)):
            new_x = x
            new_y = y
            x = self.snake[i].xcor()
            y = self.snake[i].ycor()
            self.snake[i].setx(new_x)
            self.snake[i].sety(new_y)

    def last_x(self):
        return self.snake[len(self.snake)-1].xcor()

    def last_y(self):
        return self.snake[len(self.snake)-1].ycor()

    def right(self):
        if self.snake[0].ycor() == self.snake[1].ycor():
            return
        elif self.snake[0].ycor() > self.snake[1].ycor():
            self.move_right(90)
        else:
            self.move_right(270)

    def left(self):
        if self.snake[0].ycor() == self.snake[1].ycor():
            return
        elif self.snake[0].ycor() > self.snake[1].ycor():
            self.move_right(270)
        else:
            self.move_right(90)

    def up(self):
        if self.snake[0].xcor() == self.snake[1].xcor():
            return
        elif self.snake[0].xcor() > self.snake[1].xcor():
            self.move_right(270)
        else:
            self.move_right(90)

    def down(self):
        if self.snake[0].xcor() == self.snake[1].xcor():
            return
        elif self.snake[0].xcor() > self.snake[1].xcor():
            self.move_right(90)
        else:
            self.move_right(270)

    def move_right(self, a):
        self.snake[0].right(a)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()