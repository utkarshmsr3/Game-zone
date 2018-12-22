#=====================================#
# snake.py                            #
# Date=14-01-2018  Time=21:00         #
# Utkarsh Mishra                      #
#=====================================#

import pygame
from colors import *

BLOCK_SIZE       = 30
BLOCK_SIZE_INNER = 20

UP    = 0
DOWN  = 1
LEFT  = 3
RIGHT = 4

class snake:

    def __init__(self,surface,headposx=10,headposy=10):
        self.surface=surface
        self.length=10
        self.poslist=[(headposx,y) for y in reversed(range(headposy-self.length+1,headposy+1))]
        self.motdir=RIGHT
        self.crashed=False

        self.snakeblock=pg.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.snakeblock.set_alpha(255)
        self.snakeblock.fill(GREEN)

        self.snakeblockdark=pg.Surface((BLOCK_SIZE_INNER,BLOCK_SIZE_INNER))
        self.snakeblockdark.set_alpha(255)
        self.snakeblockdark.fill(GREEN_DARK)

        self.backblock=pg.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.backblock.set_alpha(255)
        self.backblock.fill(BLACK)

    def getHeadPos(self):
        return (self.poslist[0])

    def getMotionDir(self):
        return self.motdir

    def getPosList(self):
        return self.poslist

    def setMotionDir(self,motdir):
        self.motdir=motdir

    def incLength(self):
        self.length+=1

    def move(self):
        motdir=self.getMotionDir()
        headpos=self.getHeadPos()

        if motdir == UP :
            poslist=[(headpos[0]-1,headpos[1])]
        elif motdir==DOWN:
            poslist=[(headpos[0]+1,headpos[1])]
        elif motdir==LEFT:
            poslist=[(headpos[0],headpos[1]-1)]
        elif motdir==RIGHT:
            poslist=[(headpos[0],headpos[1]+1)]

        poslist.extend(self.poslist[:-1])
        self.poslist=poslist

        if self.getHeadPos() in self.getPosList()[1:]:
            self.crashed=True

    def chrashed(self):
        return self.crashed

    def grow(self):
        lastpos=self.getPosList()[-1]
        self.length+=1
        self.poslist.append((lastpos[0]-1,lastpos[1]))

    def draw(self):
        skb=self.snakeblock
        skbd=self.snakeblockdark
        sf=self.surface

        for blockpos in self.getPosList():
            sf.blit(skb,(blockpos[1]*BLOCK_SIZE,blockpos[0]*BLOCK_SIZE))
            sf.blit(skbd,(blockpos[1]*BLOCK_SIZE+5,blockpos[0]*BLOCK_SIZE+5))

    def remove(self):
        bkb=self.backblock
        sf=self.surface

        for blockpos in self.getPosList():
            sf.blit(bkb,(blockpos[1]*BLOCK_SIZE,blockpos[0]*BLOCK_SIZE))






























    
