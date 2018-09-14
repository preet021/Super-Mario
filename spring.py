'''
	 ######
	  #  # 
	   ##  
      #  # 
     ######
'''


class Spring:

    def __init__(self, h, x, y):

        self.height = h
        self.posX = x
        self.posY = y
        self.body = ['######', ' #  # ', '  ##  ', ' #  # ', '######']

    def checkCollision(self, engine):

        if 1 + engine.mario.legsY == self.posY:
            for i in range(engine.mario.legsMinX + engine.gridX, 1 + engine.mario.legsMaxX + engine.gridX):
                if i in list(range(self.posX, self.posX + 6)):
                    engine.mario.moveUp(5)
