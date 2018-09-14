import os   

''' 
	> 
	< 
'''


class Bullet:

    def __init__(self, s, x, y, t, spd):

        self.body = s
        self.posX = x
        self.posY = y
        self.speed = spd
        self.updTime = t

    def updatePos(self, engine):

        engine.board.grid[self.posY][self.posX] = ' '

        if not engine.board.grid[self.posY][self.posX + self.speed] == ' ':
            if engine.board.grid[self.posY][self.posX + self.speed] == '(':
                os.system('aplay ./sounds/bhe.wav > /dev/null 2>&1 &')
                engine.board.removeEnemy(self.posX + self.speed, self.posY)
                engine.score += 10
                engine.board.removeBullet(self.posX, self.posY)
            elif self.body == '>' and (engine.board.grid[self.posY][self.posX + self.speed] in ['{', '}', '!', 'B', 'O', '$', '/']):
                os.system('aplay ./sounds/bih.wav > /dev/null 2>&1 &')
                engine.board.boss.lives -= 1
                engine.score += 20
                engine.board.removeBullet(self.posX, self.posY)
            elif self.body == '<' and engine.board.grid[self.posY][self.posX + self.speed] == '>':
                engine.board.removeBullet(self.posX + self.speed, self.posY)
                self.posX += self.speed
                engine.board.grid[self.posY][self.posX] = self.body
            else:
                engine.board.removeBullet(self.posX, self.posY)
        else:
            self.posX += self.speed
            engine.board.grid[self.posY][self.posX] = self.body
