#================================#
# food.py                        #
# Date=14-01-2018 Time=12:10     #
# Utkarsh Mishra                 #
#================================#

import random
from colors import *
import pygame as pg

BLOCK_SIZE=30
BLOCK_SIZE_INNER=20

class food:
    def __init__(self,surface,minx,maxx,miny,maxy):
        self.surface=surface
        self.posx=random.randint(minx,maxx-1)
        self.posy=random.randint(miny,maxy-1)
        
        self.foodblock=pg.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.foodblock.set_alpha(255)
        self.foodblock.fill(RED)

        self.foodblockdark=pg.Surface((BLOCK_SIZE_INNER,BLOCK_SIZE_INNER))
        self.foodblockdark.set_alpha(255)
        self.foodblockdark.fill(RED_DARK)

    def getPos(self):
        return (self.posx,self.posy)

    def draw(self):
        fb=self.foodblock
        fbd=self.foodblockdark
        sf=self.surface

        foodpos =self.getPos()
        sf.blit(fb,(foodpos[1]*BLOCK_SIZE,foodpos[0]*BLOCK_SIZE))
        sf.blit(fbd,(foodpos[1]*BLOCK_SIZE+5,foodpos[0]*BLOCK_SIZE+5))


"""
window_size=window_width,window_height=480,480
window=pg.display.set_mode(window_size,pg.RESIZABLE)
window.fill((255,255,255))
eat=food(window,1,20,1,20)
eat.draw()
pg.display.update()
"""
