import pymunk
from pygame import Rect
from pgzero import actor
from Doodler import Doodler


class Platform:
    def __init__(self, pos: tuple, space: pymunk.space):

        self.actor = actor.Actor("platform2.png", pos)
        self.rectBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.rectShape = pymunk.Poly.create_box(self.rectBody, (self.actor.width * .5, self.actor.height * .8))
        self.rectBody.position = pos
        self.rectShape.mass = 3
        self.rectShape.friction = 0
        self.rectShape.elasticity = 1
        self.rectShape.actor = self
        space.add(self.rectBody, self.rectShape)
        self.actor.shape = self.rectShape # kludge for physics camera
        self.actor.body = self.rectBody  # kludge for physics camera

    def draw(self, screen):
        self.actor.draw()

    def delete(self):
        self.delete()
