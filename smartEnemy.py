from enemy import Enemy


class SmartEnemy(Enemy):

    def __init__(self, s, posx, posy, t):
        super().__init__(s, posx, posy, t)

    def findMario(self, engine):

        if engine.mario.legsMaxX + engine.gridX > self.posX:
            self.speed = 1
        else:
            self.speed = -1

        super(SmartEnemy, self).updatePos(engine.board.grid)
