#=====================================#
# snakegame.py                        #
# Date=15-01-2018 Time=17:30          #
# Utkarsh Mishra                      #
#=====================================#

import pygame as pg
import sys
from colors import *
import food as fd
import snake as snk


WIDTH      = 20
HEIGHT     = 20
SPEED      = 8
SPEED_TICK = 2
SPEED_INC  = 5
SHORT      = 12
LONG       = 1

wallblock = pg.Surface((snk.BLOCK_SIZE,snk.BLOCK_SIZE))
wallblock.set_alpha(255)
wallblock.fill(BLUE)
wallblockdark = pg.Surface((snk.BLOCK_SIZE_INNER,snk.BLOCK_SIZE_INNER))
wallblockdark.set_alpha(255)
wallblockdark.fill(BLUE_DARK)


def inLimits(snake):
    headpos=snake.getHeadPos()
    return not (headpos[0]<1 or headpos[1]<1 or headpos[0]>=HEIGHT+1 or headpos[1]>=WIDTH+1)


def drawWalls(surface):
    for y in range (HEIGHT+1):
        surface.blit(wallblock,(0,y*snk.BLOCK_SIZE))
        surface.blit(wallblockdark,(5,y*snk.BLOCK_SIZE+5))
        surface.blit(wallblock,((WIDTH+1)*snk.BLOCK_SIZE,y*snk.BLOCK_SIZE))
        surface.blit(wallblockdark,((WIDTH+1)*snk.BLOCK_SIZE+5,y*snk.BLOCK_SIZE+5))

    for x in range(WIDTH+2):
        surface.blit(wallblock,(x*snk.BLOCK_SIZE,0))
        surface.blit(wallblockdark,(x*snk.BLOCK_SIZE+5,5))
        surface.blit(wallblock,(x*snk.BLOCK_SIZE,(HEIGHT+1)*snk.BLOCK_SIZE))
        surface.blit(wallblockdark,(x*snk.BLOCK_SIZE+5,(HEIGHT+1)*snk.BLOCK_SIZE+5))

pg.init()
pg.mixer.init()
eatsound=pg.mixer.Sound("snakeeat.wav")
crashsound=pg.mixer.Sound("snakecrash.wav")
clock=pg.time.Clock()
screen=pg.display.set_mode(((WIDTH+2)*snk.BLOCK_SIZE,(HEIGHT+2)*snk.BLOCK_SIZE))
pg.display.set_caption("Snake")
font=pg.font.SysFont(pg.font.get_default_font(),40)
gameovertext=font.render("GAME OVER",1,WHITE)
starttext=font.render("PRESS ANY KEY TO START",1,WHITE)
screen.fill(BLACK)

snake=snk.snake(screen,WIDTH//2,HEIGHT//2)
food=fd.food(screen,1,HEIGHT+1,1,WIDTH+1)

while food.getPos() in snake.getPosList():
    food,__init__(screen,1,WIDTH+1,1,HEIGHT+1)

pg.event.set_blocked([pg.MOUSEMOTION,pg.MOUSEBUTTONUP,pg.MOUSEBUTTONDOWN])

eaten=0


drawWalls(screen)
screen.blit(starttext,((WIDTH-10)*snk.BLOCK_SIZE/2,HEIGHT*snk.BLOCK_SIZE/2))
pg.display.flip()
waiting= True
while waiting:
    event=pg.event.wait()
    if(event.type==pg.KEYDOWN):
        waiting=False

screen.fill(BLACK)
drawWalls(screen)

running=True
while running:

    if not inLimits(snake) or snake.crashed:
        running=False
        crashsound.play()

    else:
        food.draw()
        snake.draw()
        pg.display.flip()

        if food.getPos() == snake.getHeadPos():
            eatsound.play()
            snake.grow()
            food.__init__(screen,1,WIDTH+1,1,HEIGHT+1)
            while food.getPos() in snake.getPosList():
                food.__init__(screen,1,WIDTH+1,1,HEIGHT+1)
            eaten+=1
            
            if eaten%SPEED_INC == 0:
                SPEED+=SPEED_TICK

        clock.tick(SPEED)

        event=pg.event.poll()
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type==pg.KEYDOWN:
            actmotdir=snake.getMotionDir()
            if event.key == pg.K_ESCAPE:
                sys.exit()
            elif event.key==pg.K_UP and actmotdir!=snk.DOWN:
                snake.setMotionDir(snk.UP)
            elif event.key==pg.K_DOWN and actmotdir!=snk.UP:
                snake.setMotionDir(snk.DOWN)
            elif event.key==pg.K_LEFT and actmotdir!=snk.RIGHT:
                snake.setMotionDir(snk.LEFT)
            elif event.key==pg.K_RIGHT and actmotdir!=snk.LEFT:
                snake.setMotionDir(snk.RIGHT)

        snake.remove()
        snake.move()


clock.tick(LONG)
snake.draw()
drawWalls(screen)
snakeposlist=snake.getPosList()
blackblock=snake.backblock
for pos in snakeposlist[1:]:
    screen.blit(blackblock,(pos[1]*snk.BLOCK_SIZE,pos[0]*snk.BLOCK_SIZE))
    pg.display.flip()
    clock.tick(SHORT)

gameovertext=font.render("GAME OVER SCORE=%s"%eaten,1,WHITE)
while True:
    screen.blit(gameovertext,((WIDTH-9)*snk.BLOCK_SIZE/2,HEIGHT*snk.BLOCK_SIZE/2))
    pg.display.flip()
    event=pg.event.wait()
    if event.type==pg.KEYDOWN:
        if event.key==pg.K_ESCAPE:
            sys.exit()


            









































    
    
