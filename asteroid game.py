import turtle
import math
from asteroid import Asteroid
from bullet import Bullet
from spaceship import Spaceship
import point_in_polygon
import random
from explosion import Explosion


def spaceship_collision():
    if s1.alive:
        dead_asteroids, died = list(), False
        for i in range(len(s1.lines)):
            for j in range(len(asteroids)):
                if died:
                    break
                for k in range(len(asteroids[j].p)):
                    if point_in_polygon.intersect(s1.lines[i][0], s1.lines[i][1], asteroids[j].p[k], asteroids[j].p[(k+1) % len(asteroids[j].p)]):
                        dead_asteroids.append(asteroids[j])
                        s1.alive, died, s1.lives = False, True, s1.lives - 1
                        if s1.lives:
                            turtle.write('Press s to start', font=style, align='center')
                        else:
                            turtle.write('Game Over', font=style, align='center')
                        break
        for a in dead_asteroids:
            if a.size > 20:
                asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
                asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
                asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
            else:
                exp = Explosion(a.x, a.y, screen)
                exp.explode()
            a.turtle.clear()
            asteroids.remove(a)


def collision_detection():
    dead_asteroids, dead_bullets = list(), list()
    if not len(asteroids):
        turtle.write('You Win', font=style, align='center')
        return
    for i in range(len(bullets)):
        p = (bullets[i].x, bullets[i].y)
        for j in range(len(asteroids)):
            if asteroids[j] in dead_asteroids:
                break
            if point_in_polygon.point_in_polygon(p, asteroids[j].p):
                dead_asteroids.append(asteroids[j])
                dead_bullets.append(bullets[i])
                break
    for a in dead_asteroids:
        if a.size > 20:
            asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
            asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
            asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
        else:
            exp = Explosion(a.x, a.y, screen)
            exp.explode()
        a.turtle.clear()
        asteroids.remove(a)

    for b in dead_bullets:
        b.turtle.clear()
        bullets.remove(b)


def animate():
    s1.move(1 / 20)
    s1.draw()
    for a in asteroids:
        a.move(1 / 20)
        a.draw2()
    for b in bullets:      
        b.move(1 / 20)
        b.draw()
    collision_detection()
    spaceship_collision()
    if len(bullets) > 0:
        if bullets[0].life < 0:
            bullets.pop(0)
    screen.update()
    screen.ontimer(animate, 50)


def rotate_left(): 
    s1.direction += 0.2


def rotate_right():
    s1.direction -= 0.2


def thrust():
    if s1.alive:
        s1.thrustlife = 0.5
        thrust_direction = s1.direction + math.pi/2
        s1.speedx, s1.speedy = s1.speedx + 5 * math.cos(thrust_direction), s1.speedy + 5 * math.sin(thrust_direction)
        speed = (s1.speedx ** 2 + s1.speedy ** 2) ** 0.5
        if speed > Spaceship.maxspeed:
            s1.speedx, s1.speedy = (s1.speedx * Spaceship.maxspeed) / speed, (s1.speedy * Spaceship.maxspeed)/speed


def fire():
    if s1.alive:
        if len(bullets) <= 0 or bullets[len(bullets) - 1].life <= 1:
            b = Bullet(s1.tipx, s1.tipy, s1.direction + math.pi / 2)
            bullets.append(b)


def alive():
    if not s1.alive and s1.lives:
        s1.alive = True
        turtle.clear()
        s1.x, s1.y, s1.direction, s1.speedx, s1.speedy = 0, 0, 0, 25, 40


screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0, 0)
screen.onkey(rotate_left, 'Left')
screen.onkey(rotate_right, 'Right')
screen.onkey(thrust, 'Up')
screen.onkey(alive, 's')
screen.onkey(fire, ' ')
style = ('Courier', 15, 'normal')
turtle.color("White")
turtle.write('Press s to start', font=style, align='center')
screen.listen()
bullets, asteroids = list(), list()
s1 = Spaceship(0, 0, 0)
asteroids.append(Asteroid(100, random.uniform(-200, 200), random.uniform(-200, 200)))
asteroids.append(Asteroid(100, random.uniform(-200, 200), random.uniform(-200, 200)))
asteroids.append(Asteroid(100, random.uniform(-200, 200), random.uniform(-200, 200)))
animate()
turtle.mainloop()
