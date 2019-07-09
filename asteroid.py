import turtle
import math
import random
import time


class Asteroid:
    def __init__(self, size, x, y, fast=30, tilt=0):
        self.size, self.tilt, self.x, self.y, self.rs, self.speed = size, tilt, x, y, random.uniform(-0.1, 0.1), fast
        self.direction, self.turtle, self.s, self.p = random.uniform(0, 2*math.pi), turtle.Turtle(), list(), list()
        self.turtle.hideturtle()
        self.turtle.color("blue")
        self.turtle.speed(0)
        for _ in range(12):
            self.s.append(random.uniform(0.5 * self.size, self.size))

    def draw_one(self, x, y, make_polygon=False):
        self.p.clear()
        self.turtle.up()
        px_first, py_first, angle = x + self.s[0] * math.cos(self.tilt), y + self.s[0] * math.sin(self.tilt), self.tilt
        if make_polygon:
            self.p.append((px_first, py_first))
        self.p.append((px_first, py_first))
        self.turtle.goto(px_first, py_first)
        self.turtle.down()
        for i in range(11):
            angle += 2 * math.pi / 12
            px, py = x + self.s[i+1] * math.cos(angle), y + self.s[i+1] * math.sin(angle)
            self.turtle.goto(px, py)
            if make_polygon:
                self.p.append((px, py))
        self.turtle.goto(px_first, py_first)
        
    def draw2(self):
        if self.x > 300:
            self.x -= 600
        if self.y > 300:
            self.y -= 600
        if self.x < -300:
            self.x += 600
        if self.y < -300:
            self.y += 600
        self.turtle.clear()
        self.draw_one(self.x + 600, self.y)
        self.draw_one(self.x - 600, self.y)
        self.draw_one(self.x, self.y + 600)
        self.draw_one(self.x, self.y - 600)
        self.draw_one(self.x, self.y, True)

    def move(self, t):
        self.x += self.speed * t * math.cos(self.direction)
        self.y += self.speed * t * math.sin(self.direction)
        self.tilt -= self.rs


def animate():
    a1.move(1 / 30)
    a1.draw2()
    screen.ontimer(animate, 33)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.tracer(0, 0)
    screen.setup(600, 600)
    a1 = Asteroid(200, 0, 20, 0)
    animate()
