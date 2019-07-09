import turtle
import math
import random


class Bullet:
    speed = 200
    lifespan = 1.5

    def __init__(self, x, y, direction):
        self.x, self.y, self.direction, self.life, self.turtle = x, y, direction, Bullet.lifespan, turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.color("purple")

    def draw(self):
        self.turtle.clear()
        if self.life >= 0:
            self.turtle.goto(self.x, self.y)
            self.turtle.dot(5)

    def move(self, t):
        self.life, dist = self.life - t, Bullet.speed * t
        self.x, self.y = self.x + dist * math.cos(self.direction), self.y + dist * math.sin(self.direction)


if __name__ == '__main__':
    def animate():
        for b in bullets:
            b.move(1 / 20)
            b.draw()
        if len(bullets) > 0:
            if bullets[0].life < 0:
                bullets.pop(0)
        screen.ontimer(animate, 50)
        
    def fire():
        if len(bullets) > 0:
            if bullets[len(bullets) - 1].life > 1:
                return
        b = Bullet(random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(0, 2 * math.pi))
        bullets.append(b)
    screen = turtle.Screen()
    screen.tracer(0, 0)
    bullets = list()
    screen.onkey(fire, ' ')
    screen.listen()
    animate()
