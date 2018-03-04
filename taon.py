#coding:utf-8
import pygame, sys
from pygame.locals import *
import ctypes  # An included library with Python install.
import random

red = (255,  0,  0)
black = ( 0,  0, 0)
white = (255,255,255)
green = (0,255,0)
blue = (0,150,255)
col = [red,white,green,blue]
width = 360
height = 640
tasize = 50
case = 0
keys = [False, False]
ax = width/2 - tasize
astate = 0
score = 0
bars = []
bheight = 20
dby = 1
dbx = 0.5
nani = [700 , 1300]
lasttime = 0
waittime = random.randrange(nani[0],nani[1])
best = 0

case0=pygame.image.load("open.jpg")
right=pygame.image.load("aRRow.png")
left=pygame.image.load("aLLow.png")
bg=pygame.image.load("black.jpg")
end=pygame.image.load("over.jpg")

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('taon')

pygame.mixer.init()
pygame.mixer.music.load("beat.mp3")
pygame.mixer.music.play(-1,0.0)

def drawarrow(s,x):
	#pygame.draw.rect(screen, red, [x, y, p_width, p_height], 2)
	if(s==True):
		screen.blit(left,(x,400))
	if(s==False):
		screen.blit(right,(x,400))

def drawscore():
    global score,best,blue
    scoreFont = pygame.font.Font(None,30)
    scoreText = scoreFont.render(str(score),0,white)
    screen.blit(scoreText, (5,5))
    score += 1
    bcoreFont = pygame.font.Font(None,30)
    bcoreText = bcoreFont.render(str(best),0,blue)
    screen.blit(bcoreText, (5,25))

def barsinit():
    global width,bars,col,white,case
    x = random.randrange(0,width)
    y = -30
    state = True
    if case < 5:
        bwidth = random.randrange(40,120)
    else:
        bwidth = random.randrange(40,80)
    direc = True
    cl = col[1]
    #cl = col[random.randrange(0,4)]
    bar=[x,y,state,bwidth,direc,cl]
    bars.append(bar)

def drawbar():
    global bars,score,bheight,dby
    for b in bars:
        if b[2] == True:
            b[1] += dby
            pygame.draw.rect(screen, b[5], [b[0], b[1],b[3], bheight])
        if b[1] >= height:
            bars.remove(b)


def keymove():
    global ax,keys,tasize
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                keys[0] = True
            if event.key == K_RIGHT:
                keys[0] = False


    if keys[0] == True:
        ax -= 1
        if (ax < 0):
            keys[0] = False
    if keys[0] == False:
        ax += 1
        if (ax + (tasize/2) > width):
            keys[0] = True

def moving():
    global bars, dbx
    if case >= 4:
        for b in bars:
            if b[4] == True:
                b[0] -= dbx
            if b[4] == False:
                b[0] += dbx
            if b[0] <= 0:
                b[4] = False
            if b[0]+b[3] >= width:
                b[4] = True

def crush():
    global bars, ax , tasize,bheight,case
    for b in bars:
        me = pygame.Rect(ax, 400, tasize-20, tasize-20)
        objbar = pygame.Rect(b[0],b[1],b[3],bheight)
        if me.colliderect(objbar):
            case = 100

def reset():
    global ax,score,bars,case,best
    pygame.mixer.init()
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play(-1,0.0)
    ax = width/2 - tasize
    bars = []
    case = 1
    if score > best:
        best = score
    score = 0

while True:
    if case == 0:
        screen.blit(case0,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    keys[1] = True
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    keys[1] = False
            if keys[1] == True:
                case = 1
                pygame.mixer.init()
                pygame.mixer.music.load("bgm.mp3")
                pygame.mixer.music.play(-1,0.0)
                keys[1] = False

        pygame.display.update()

    if case == 1:
        screen.blit(bg,(0,0))
        keymove()
        drawscore()
        drawarrow(keys[0],ax)

        if score > 500:
            case = 2
            lasttime =  pygame.time.get_ticks()

        pygame.display.update()

    if case == 2:
        screen.blit(bg,(0,0))
        drawscore()
        drawbar()
        drawarrow(keys[0],ax)
        crush()

        if (pygame.time.get_ticks() - lasttime >= waittime):
            barsinit()
            lasttime =  pygame.time.get_ticks()
            waittime = random.randrange(nani[0],nani[1])

        if score > 2500:
            case = 3
            #dby += 1

        keymove()
        pygame.display.update()

    if case == 3:
        screen.blit(bg,(0,0))
        drawscore()
        drawbar()
        drawarrow(keys[0],ax)
        crush()

        if (pygame.time.get_ticks() - lasttime >= waittime):
            barsinit()
            barsinit()
            lasttime =  pygame.time.get_ticks()
            waittime = random.randrange(nani[0],nani[1])

        if score > 4000:
            case = 4

        keymove()
        pygame.display.update()

    if case == 4:
        screen.blit(bg,(0,0))
        moving()
        drawscore()
        drawbar()
        drawarrow(keys[0],ax)
        crush()

        if (pygame.time.get_ticks() - lasttime >= waittime):
            barsinit()
            lasttime =  pygame.time.get_ticks()
            waittime = random.randrange(nani[0],nani[1])

        if score > 6000:
            case = 5

        keymove()
        pygame.display.update()

    if case == 5:
        screen.blit(bg,(0,0))
        drawscore()
        drawbar()
        drawarrow(keys[0],ax)
        crush()

        if (pygame.time.get_ticks() - lasttime >= waittime):
            barsinit()
            barsinit()
            lasttime =  pygame.time.get_ticks()
            waittime = random.randrange(nani[0],nani[1])

        '''if score > 6000:
            case = 6'''

        moving()
        keymove()
        pygame.display.update()

    if case == 100:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(end,(-70,-20))
        fFont = pygame.font.Font(None,24)
        fText = fFont.render("score : " + str(score),0, white)
        screen.blit(fText, (135,460))

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    reset()

        pygame.display.update()

pygame.quit()
sys.exit()
