import random
from enemy import Enemy

'''
	{^_^}
	  !
	  B
	  !
	  O
	  !
	  $
	  !
	  $
'''


class Boss(Enemy):

    def __init__(self):
        ''' inheritance '''
        super().__init__('!B!O!$!$', 1330, 27, 0)
        self.head = '{^_^}'
        self.height = 9
        self.updTime1 = 0
        self.lives = 6

    ''' polymorphism '''

    def updatePos(self):

        self.posX = random.choice(list(range(1330, 1345)))
        self.posY = random.choice(list(range(16, 27, 2)))
