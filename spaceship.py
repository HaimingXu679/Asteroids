import turtle
import math
import random
turtle.bgcolor("black")
turtle.hideturtle()


class Spaceship:
    maxspeed = 100

    def __init__(self, x, y, direction):
        self.x, self.y, self.thrustlife, self.speedx, self.speedy, self.direction = x, y, 0, 25, 40, direction
        self.turtle, self.lines, self.alive, self.lives, self.tipx, self.tipy = turtle.Turtle(), list(), False, 3, 0, 0
        self.turtle.hideturtle()

    def draw_one(self, x, y):
        dir_degree = self.direction * 180 / math.pi
        self.turtle.up()
        self.turtle.goto(x, y)
        self.turtle.seth(180 + dir_degree)
        self.turtle.fd(3.875)
        self.turtle.left(75)
        self.turtle.fd(5)
        self.turtle.down()
        self.turtle.seth(75 + dir_degree)
        x3, y3 = self.turtle.xcor(), self.turtle.ycor()
        self.turtle.fd(5)
        x1, y1 = self.turtle.xcor(), self.turtle.ycor()
        self.turtle.fd(15)
        self.tipx, self.tipy = self.turtle.xcor(), self.turtle.ycor()
        self.turtle.right(150)
        self.turtle.fd(15)
        x2, y2 = self.turtle.xcor(), self.turtle.ycor()
        self.turtle.fd(5)
        x4, y4 = self.turtle.xcor(), self.turtle.ycor()
        self.turtle.up()
        self.turtle.goto(x1, y1)
        self.turtle.down()
        self.turtle.goto(x2, y2)
        self.lines.append(((self.tipx, self.tipy), (x3, y3)))
        self.lines.append(((self.tipx, self.tipy), (x4, y4)))
        if self.thrustlife > 0 or __name__ == '__main__':
            self.turtle.color("purple")
            self.turtle.up()
            self.turtle.goto(x3, y3)
            self.turtle.goto(x4, y4)
            x5, y5 = (x3 + x4) / 2, (y3 + y4) / 2
            self.turtle.goto(x5, y5)
            self.turtle.down()
            self.turtle.seth(75 + dir_degree)
            self.turtle.fillcolor("red")
            self.turtle.begin_fill()
            self.turtle.fd(5)
            self.turtle.left(105)
            self.turtle.fd(2.5)
            self.turtle.goto(x5, y5)
            self.turtle.end_fill()

    def draw(self):
        self.turtle.clear()
        if self.alive or __name__ == '__main__':
            if self.x > 300:
                self.x -= 600
            if self.x < -300:
                self.x += 600
            if self.y > 300:
                self.y -= 600
            if self.y < -300:
                self.y += 600
            self.draw_one(self.x + 600, self.y)
            self.draw_one(self.x - 600, self.y)
            self.draw_one(self.x, self.y + 600)
            self.draw_one(self.x, self.y - 600)
            self.draw_one(self.x, self.y)

    def move(self, t):
        self.x, self.y, self.thrustlife = self.x + self.speedx * t, self.y + self.speedy * t, self.thrustlife - t


if __name__ == '__main__':
    def animate():
        s1.move(0.05)
        s1.draw()
        screen.ontimer(animate, 50)

    def rotate_left():
        s1.direction += 0.2

    def rotate_right():
        s1.direction -= 0.2

    def thrust():
        s1.thrustlife, thrust_direction = 0.5, s1.direction + math.pi / 2
        s1.speedx, s1.speedy = s1.speedx + 5 * math.cos(thrust_direction), s1.speedy + 5 * math.sin(thrust_direction)
        speed = (s1.speedx ** 2 + s1.speedy ** 2) ** 0.5
        if speed > Spaceship.maxspeed:
            s1.speedx, s1.speedy = (s1.speedx * Spaceship.maxspeed) / speed, (s1.speedy * Spaceship.maxspeed) / speed
            
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.tracer(0, 0)
    screen.onkey(rotate_left, 'Left')
    screen.onkey(rotate_right, 'Right')
    screen.onkey(thrust, 'Up')
    screen.listen()
    s1 = Spaceship(0, 0, 0)
    animate()
