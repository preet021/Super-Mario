''' (E) '''


class Enemy:

    def __init__(self, s, posx, posy, t):
        self.body = s
        self.posX = posx
        self.posY = posy
        self.speed = -1
        self.updTime = t

    def updatePos(self, grid):

        grid[self.posY][self.posX:(self.posX + 3)] = '   '

        if self.speed == -1 and (not grid[self.posY][self.posX - 1] == ' '):
            self.speed = 1

        elif self.speed == 1 and (not grid[self.posY][self.posX + 3] == ' '):
            self.speed = -1

        self.posX += self.speed

        if grid[self.posY + 1][self.posX] == ' ' and grid[self.posY + 1][self.posX + 1] == ' ' and grid[self.posY + 1][self.posX + 2] == ' ' and self.posY <= 32:
            self.posY += 1

        grid[self.posY][self.posX:(self.posX + 3)] = self.body
