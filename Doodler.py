import pymunk
import math
from pgzero import actor
from pgzero.keyboard import keyboard


class Doodler:
    def __init__(self, pos: tuple, space: pymunk.space):

        self.actor = actor.Actor("doodler_right.png", pos)
        self.rectBody = pymunk.Body()
        self.rectShape = pymunk.Poly.create_box(self.rectBody, (self.actor.width, self.actor.height))
        self.rectBody.position = pos
        self.rectShape.mass = 3
        self.rectShape.friction = 0
        self.rectShape.elasticity = 1
        self.rectShape.actor = self
        space.add(self.rectBody, self.rectShape)
        self.actor.shape = self.rectShape  # kludge for physics camera
        self.actor.body = self.rectBody  # kludge for physics camera

    def update(self):
        self.actor.pos = self.rectBody.position
        # self.keydown = False
        if keyboard.left and not self.keydown:
            self.rectBody.apply_impulse_at_local_point((-50, 0))
            self.actor = actor.Actor("doodler_left.png", self.actor.pos)
            self.keydown = True
        elif keyboard.right and not self.keydown:
            self.rectBody.apply_impulse_at_local_point((+50, 0))
            self.actor = actor.Actor("doodler_right.png", self.actor.pos)
            self.keydown = True
        else:
            self.keydown = False

    def draw(self):
        self.actor.draw()

    def rotate(self, degrees: float):
        self.actor.angle += degrees
