from board import Board
from mario import Mario
from enemy import Enemy
from bullets import Bullet
from boss import Boss
import getInput
import os
import signal
import time


class Engine(Board, Mario, Enemy, Bullet):

    '''game engine that inherits from classes
       Board, Mario, Enemy, Bullet'''

    def __init__(self):
        self.score = 0
        self.coins = 0
        self.lives = 3
        self.gridX = 0
        self.board = Board()
        self.mario = Mario(self)
        self.getch = getInput._getChUnix()
        self.speed = 1
        self.its = 0
        self.lefTime = 300
        self.lupd = 0

    '''main function to run the game'''

    def run(self):
        '''below two functions are to wait for the input for {timeout} seconds'''

        def alarmhandler(signum, frame):
            raise TypeError

        def getinp(timeout=0.09):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                ch = self.getch()
                signal.alarm(0)
                return ch
            except TypeError:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        '''terminate the game and display the final score etc.'''
        def terminate(s):
            os.system('killall -9 aplay')
            self.score += 5 * self.coins + self.gridX // 10
            print(s)
            print('\nGAME OVER\nYour Score : {}\nCoins Collected : {}\nCome Back Again!\n'.format(
                self.score, self.coins))
            exit()

        '''initialize the board/background'''
        self.board.createBackground()

        '''print the board'''
        self.board.render(self)

        os.system('aplay ./sounds/bg.wav > /dev/null 2>&1 &')

        while True:

            if self.board.boss.lives <= 0:
                terminate('You Won!')

            if self.lives <= 0:
                terminate('You Lose :(')

            '''update the left time'''
            if time.time() - self.lupd > 1:
                self.lefTime -= 1
                if self.lefTime == 0:
                    terminate('Time Up...You Lose :(')
                self.lupd = time.time()

            '''scanning the input key'''
            inp = getinp()
            if inp == 'q':
                terminate('You Lose :(')
            elif inp == ' ':
                self.mario.fireBullet(self)
            elif inp == 'w':
                self.mario.up = True
            elif inp == 's':
                self.mario.up = False
            elif inp == 'a':
                if self.gridX > 0:
                    if self.board.render(self):
                        self.gridX = self.gridX - self.speed
                        if self.mario.legs == '/    \\':
                            self.mario.legs = '\\    /'
                        else:
                            self.mario.legs = '/    \\'
            elif inp == 'd':
                if self.gridX < 1250 and self.board.render(self):
                    self.gridX = self.gridX + self.speed
                    if self.mario.legs == '/    \\':
                        self.mario.legs = '\\    /'
                    else:
                        self.mario.legs = '/    \\'

            self.coins = self.mario.updatePos(
                self, self.board, self.gridX, self.coins)
            if self.mario.legsY >= self.board.height - 3:
                self.lives = self.lives - 1
                os.system('aplay ./sounds/')
                if self.lives == 0:
                    terminate()
                self.mario.newLife(self)
                self.gridX = 0

            self.its += 0.1
            self.board.render(self)
