import time


class Bridge:

    def __init__(self):

        self.speed = -1
        self.posX = 584
        self.length = 23
        self.posY = 17
        self.s = '#######################'
        self.updTime = 0

    def updatePos(self, engine):

        if self.speed == -1:
            if self.posY - 1 < 17:
                self.speed = 1

        elif self.speed == 1:
            if self.posY + 1 > 30:
                self.speed = -1

        engine.board.grid[self.posY][self.posX:(
            self.posX + self.length)] = ' ' * self.length

        if self.speed == -1:
            if engine.mario.legsY + 2 == self.posY:
                engine.mario.onBridge = True

        self.posY += self.speed
        engine.board.grid[self.posY][
            self.posX:(self.posX + self.length)] = self.s
        self.updTime = time.time()

        if engine.mario.onBridge:
            engine.mario.headY = self.posY - 7
            if engine.mario.headY < 0:
                engine.mario.headY = 0
            engine.mario.neckY = engine.mario.headY + 1
            engine.mario.bodyYs = [engine.mario.neckY + 1, engine.mario.neckY + 2, engine.mario.neckY + 3]
            engine.mario.bottomY = engine.mario.neckY + 4
            engine.mario.legsY = engine.mario.bottomY + 1
