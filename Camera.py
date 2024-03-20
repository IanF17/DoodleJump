import pymunk
from pgzero.actor import Actor


class Camera:
    def __init__(self, screenWidth: int, screenHeight: int, space:pymunk.Space = None):
        self.actorList: list = list()
        self.cameraCenter = (screenWidth / 2, screenHeight / 2)
        self.space = space

    def addActorToCamera(self, actor: Actor):
        self.actorList.append(actor)

    def setCameraPos(self, pos: tuple):
        deltaX: int = pos[0] - self.cameraCenter[0]
        deltaY: int = pos[1] - self.cameraCenter[1]
        self.moveCamera((deltaX, deltaY))

    def moveCamera(self, delta):
        for actor in self.actorList:
            pos = actor.body.position
            actor.body.position = (pos[0]-delta[0],pos[1]-delta[1])
            actor.center = (actor.center[0] - delta[0], actor.center[1] - delta[1])
            self.space.reindex_shape(actor.shape)
        self.cameraCenter = (self.cameraCenter[0] + delta[0], self.cameraCenter[1] + delta[1])
