import os
import time
from bullets import Bullet

'''
	[MM]
	_][_
   |    |
   |    |
   |    |
   |____|
   /    \
'''


class Mario:

    def __init__(self, engine):

        self.head = '[MM]'
        self.neck = '_][_'
        self.body = '|    |'
        self.bottom = '|____|'
        self.legs = '/    \\'
        self.legsMaxX = 78
        self.legsMinX = 73
        self.bottomMaxX = 78
        self.bottomMinX = 73
        self.bodyMaxX = 78
        self.bodyMinX = 73
        self.neckMaxX = 77
        self.neckMinX = 74
        self.headMaxX = 77
        self.headMinX = 74
        self.headY = 29
        self.neckY = 30
        self.bodyYs = [31, 32, 33]
        self.bottomY = 34
        self.legsY = 35
        self.up = False
        self.jumpSize = 8
        self.allowedJumps = 2
        self.cnt = 1
        self.it = -1
        self.onBridge = False

    def moveUp(self, steps):
        os.system('aplay ./sounds/jmp.wav > /dev/null 2>&1 &')
        self.headY = self.headY - steps
        if self.headY < 0:
            self.headY = 0
        self.neckY = self.headY + 1
        self.bodyYs = [self.neckY + 1, self.neckY + 2, self.neckY + 3]
        self.bottomY = self.neckY + 4
        self.legsY = self.bottomY + 1

    def moveDown(self, steps):
        self.headY = self.headY + steps
        self.neckY = self.headY + 1
        self.bodyYs = [self.neckY + 1, self.neckY + 2, self.neckY + 3]
        self.bottomY = self.neckY + 4
        self.legsY = self.bottomY + 1

    def updatePos(self, engine, board, curx, coins):

        if self.onBridge and (engine.gridX + self.legsMaxX > 611 or engine.gridX + self.legsMaxX < 584):
            self.onBridge = False

        if self.onBridge:
            return coins

        if self.allowedJumps <= 0:
            self.up = False

        if self.up:
            steps = self.jumpSize
            f = False
            for i in range(self.headY - 1, self.headY - self.jumpSize, -1):
                if f:
                    break
                for j in range(self.headMinX, 1 + self.headMaxX):
                    if board.grid[i][curx + j] == board.green + '#' + board.reset:
                        steps = self.headY - i
                        f = True
                        os.system('aplay ./sounds/ubb.wav > /dev/null 2>&1 &')
                        break
                    elif board.grid[i][curx + j] == board.red + '0' + board.reset:
                        steps = self.headY - i
                        f = True
                        os.system('aplay ./sounds/brb.wav > /dev/null 2>&1 &')
                        board.changeBrick(board.red + '0' +
                                          board.reset, i, curx + j)
                        break
                    elif board.grid[i][curx + j] == board.red + '1' + board.reset:
                        steps = self.headY - i
                        f = True
                        coins += 1
                        board.changeBrick(board.red + '1' +
                                          board.reset, i, curx + j)
                        break
                    elif board.grid[i][curx + j] == board.red + '2' + board.reset:
                        steps = self.headY - i
                        f = True
                        coins += 1
                        board.changeBrick(board.red + '2' +
                                          board.reset, i, curx + j)
                        break
                    elif board.grid[i][curx + j] == board.red + '3' + board.reset:
                        steps = self.headY - i
                        f = True
                        coins += 1
                        board.changeBrick(board.red + '3' +
                                          board.reset, i, curx + j)
                        break
            self.moveUp(steps)
            self.allowedJumps -= 1
            self.up = False

        if not self.up:
            X, Y, f = -1, -1, 0
            for i in range(self.legsMinX, 1 + self.legsMaxX):
                if board.grid[self.legsY + 1][curx + i] == board.yellow + '#' + board.reset or board.grid[self.legsY + 1][curx + i] == '#' or board.grid[self.legsY + 1][curx + i] == board.green + '#' + board.reset or board.grid[self.legsY + 1][curx + i] == board.red + '0' + board.reset or board.grid[self.legsY + 1][curx + i] == board.red + '1' + board.reset or board.grid[self.legsY + 1][curx + i] == board.red + '2' + board.reset or board.grid[self.legsY + 1][curx + i] == board.red + '3' + board.reset:
                    f = 1
                    break
                elif board.grid[self.legsY + 1][curx + i] == '(' or board.grid[self.legsY + 1][curx + i] == 'E' or board.grid[self.legsY + 1][curx + i] == ')':
                    X, Y = i, (self.legsY + 1)
                    f = 2
                    break
                elif board.grid[self.legsY + 1][curx + i] == 'C':
                    X, Y = (i + curx), (self.legsY + 1)
                    f = 3
                    break
            if f == 0:
                if time.time() - self.it >= 0.091:
                    self.moveDown(self.cnt)
                    self.it = time.time()
            elif f == 1:
                self.cnt = 1
                self.allowedJumps = 2
            elif f == 3:
                coins += 1
                board.removeCoins(engine, X, Y)
            else:
                self.allowedJumps = 0
                board.removeEnemy(X + curx, Y)
                engine.score += 10
        return coins

    def newLife(self, engine):

        os.system('killall -9 aplay')
        os.system('aplay ./sounds/bg.wav > /dev/null 2>&1 &')
        engine.lefTime += 50
        if engine.lefTime > 300:
            engine.lefTime = 300
        self.headY = 29
        self.neckY = self.headY + 1
        self.bodyYs = [self.neckY + 1, self.neckY + 2, self.neckY + 3]
        self.bottomY = self.neckY + 4
        self.legsY = self.bottomY + 1

    def fireBullet(self, engine):
        if engine.gridX + self.legsMaxX > 611:
            os.system('aplay ./sounds/mbf.wav > /dev/null 2>&1 &')
            engine.board.bullets.append(
                Bullet('>', engine.gridX + self.bodyMaxX + 1, self.legsY - 2, time.time(), 1))

    def getXpos(self, engine):
        curx = engine.gridX
        tmp_list = [self.headMaxX, self.neckMaxX,
                    self.bottomMaxX, self.legsMaxX, self.bodyMaxX]
        for i in tmp_list:
            i += curx
        return tmp_list
