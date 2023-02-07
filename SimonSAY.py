import pygame, sys,random,time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((460, 600))
screen.fill((0,0,0))
pygame.display.set_caption("Game Setup")

YELLOWRECT = pygame.Rect(20,20,200,200)
BLUERECT = pygame.Rect(240,20,200,200)
REDRECT = pygame.Rect(20,240,200,200)
GREENRECT = pygame.Rect(240,240,200,200)

YELLOW = (155,155,0)
BLUE = (0,0,155)
RED = (155,0,0)
GREEN = (0,155,0)

colors = [RED,GREEN,BLUE,YELLOW]

WHITE   =(255,255,255)
BLACK   =(0,0,0)
BRIGHTRED   =(255,0,0)
RED     =(155,0,0)
BRIGHTGREEN     =(0,255,0)
GREEN       =(0,155,0)
BRIGHTBLUE      =(0,0,255)
BLUE    =(0,0,155)
BRIGHTYELLOW    =(255,255,0)
YELLOW      =(155,155,0)
DARKGRAY    = (40,40,40)
bgColor = BLACK

BEEP1 = pygame.mixer.Sound('beep1.ogg')
BEEP2 = pygame.mixer.Sound('beep2.ogg')
BEEP3 = pygame.mixer.Sound('beep3.ogg')
BEEP4 = pygame.mixer.Sound('beep4.ogg')

def drawButtons():
    pygame.draw.rect(screen, YELLOW, (20,20,200,200))
    pygame.draw.rect(screen, BLUE, (240,20,200,200))
    pygame.draw.rect(screen, RED, (20,240,200,200))
    pygame.draw.rect(screen, GREEN, (240,240,200,200))

pattern = []

def flashButtonAnimation(color):

    if color == YELLOW:
       locationTuple = YELLOWRECT.topleft
       flashColor = BRIGHTYELLOW
       sound = BEEP1
    elif color == BLUE:
        locationTuple = BLUERECT.topleft
        flashColor = BRIGHTBLUE
        sound = BEEP2
    elif color == RED:
        locationTuple = REDRECT.topleft
        flashColor = BRIGHTRED
        sound = BEEP3
    elif color ==   GREEN:
        locationTuple = GREENRECT.topleft
        flashColor = BRIGHTGREEN
        sound = BEEP4

    sound.play()
    pygame.draw.rect(screen,flashColor,
    (locationTuple[0],locationTuple[1],200,200))
    pygame.display.update()
    pygame.time.wait(500)
    drawButtons()
    pygame.display.update()

move = 0

running = True
turn = "simon"
gameOver = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            print(mousex, mousey)

            if YELLOWRECT.collidepoint((mousex, mousey)):
                color = YELLOW
            if BLUERECT.collidepoint((mousex, mousey)):
                color = BLUE
            if REDRECT.collidepoint((mousex, mousey)):
                color = RED
            if GREENRECT.collidepoint((mousex, mousey)):
                color = GREEN
            flashButtonAnimation(color)
            if color == pattern[move]:
                if move == len(pattern)-1:
                    pygame.time.wait(500)
                    turn = "simon"
                    move = 0
                else:
                    move = move+1
            else:
                print("game over")
                fontObj = pygame.font.SysFont('papyrus',30)
                fontSurfaceObj = fontObj.render("Game over", True,
                (255, 0, 0),(0,255,0))
                screen.blit(fontSurfaceObj,(100,200))
                gameOver = True


                turn = "simon"

    if gameOver == False:
        drawButtons()
        fontObj = pygame.font.SysFont('papyrus',30)
        fontSurfaceObj = fontObj.render("Click and follow the pattern", True,
        (255, 0, 0),(0,255,0))
        screen.blit(fontSurfaceObj,(10,500))
    if turn == "simon":
        pattern.append(random.choice(colors))
        print(pattern)
        for color in pattern:
            pygame.time.wait(250)
            flashButtonAnimation(color)

        turn = "player"





    pygame.display.update()

pygame.draw.rect(DISPLAYSURF, YELLOW, (20,20,200,200))
