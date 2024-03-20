import os

import pygame.transform
from pymunk import Vec2d

os.environ['SDL_VIDEO_WINDOW_POS'] = '50, 50'
import pgzrun
import pymunk
import tkinter
from Doodler import Doodler
from Platform import Platform
from threading import Event

from random import random
import random
from Camera import Camera

WIDTH = 800
HEIGHT = 600
global plist
global space
global yOver
global score
global first

score: int = 0

initted: bool = False

collision_types = {
    "platform": 1,
    "doodler": 2
}


def init():
    pass


def update():
    global space
    global yOver
    global score
    doodler.update()
    space.step(1 / 50)
    global initted
    if not initted:
        init()
        initted = True
    if doodler.actor.y < 200:
        yOver = 200 - doodler.actor.y
        if yOver > 0:
            camera.moveCamera((0, - yOver / 20))
            score += yOver


def draw():
    screen.fill((0, 0, 0))
    doodler.draw()
    floor.draw(screen)
    global plist
    for y in plist:
        y.draw(screen)
    clock.tick(50)
    global score
    screen.draw.text("Score: " + str(round(score / 10)), topleft=(20, 20), color="white")

    if doodler.actor.y > 660:
        global first
        leaderboard()

        screen.fill("black")
        screen.draw.text("Game Over", center=(400, 250), color="white", fontsize=69)
        screen.draw.text("Your Score: " + str(round(score / 10)), center=(400, 330), color="white", fontsize=26)
        screen.draw.text("High Score: " + first, center=(400, 370), color="white", fontsize=35)


def leaderboard():
    global first
    leader = []
    f = open("Leaderboard.txt", "r")
    for x in f.readlines():
        leader.append(x)
    first = leader[0][2:]
    f.close()
    if score / 10 > int(first):
        g = open("Leaderboard.txt", "w")
        g.write("1." + str(round(score / 10)))


def only_block_down(arbiter, space, data) -> bool:
    return arbiter.shapes[0].body.velocity[1] > 0


def doodler_hit_platform(arbiter, space, data) -> bool:
    dBody = arbiter.shapes[0].body
    if dBody.velocity[1] > 0:
        dBody.velocity = Vec2d(0, -600)
    return False


space = pymunk.Space()
space.gravity = (0.0, 900.0)

h = space.add_collision_handler(collision_types["doodler"], collision_types["platform"])
h.pre_solve = only_block_down
h.begin = doodler_hit_platform

camera: Camera = Camera(800, 600, space)

doodler: Doodler = Doodler((400, 300), space)
doodler.rectShape.collision_type = collision_types["doodler"]
floor: Platform = Platform((400, 450), space)
floor.rectShape.collision_type = collision_types["platform"]
camera.addActorToCamera(floor.actor)

global plist
plist: list = []
for x in range(100):
    t = random.randint(100, 700)
    pos = (t, (500 - x * 245))
    if t < 350:
        pos2 = (t + 200, ((500 - x * 250) - 100))
    if t > 450:
        pos2 = (t - 200, ((500 - x * 250) - 100))

    platform = Platform(pos, space)
    platform.rectShape.collision_type = collision_types["platform"]
    plist.append(platform)
    camera.addActorToCamera(platform.actor)
    if t < 350 or t > 450:
        platform2 = Platform(pos2, space)
        platform2.rectShape.collision_type = collision_types["platform"]
        plist.append(platform2)
        camera.addActorToCamera(platform2.actor)

pgzrun.go()
