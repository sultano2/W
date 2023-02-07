import pygame, sys,random,time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((480, 480))
screen.fill((0,0,0))
pygame.display.set_caption("Game Setup")

YELLOWRECT = pygame.Rect(20,20,200,200)
BLUERECT = pygame.Rect(240,20,200,200)
REDRECT = pygame.Rect(20,240,200,200)
GREENRECT = pygame.Rect(240,240,200,200)

Y = (155,155,0)
B = (0,0,155)
R = (155,0,0)
G = (0,155,0)

colors = [R,G,B,Y]

WHITE   =(255,255,255)
BLACK   =(0,0,0)
BRIGHTRED   =(255,0,0)
R     =(155,0,0)
BRIGHTGREEN     =(0,255,0)
G      =(0,155,0)
BRIGHTBLUE      =(0,0,255)
B    =(0,0,155)
BRIGHTYELLOW    =(255,255,0)
Y      =(155,155,0)
DARKGRAY    = (40,40,40)
bgColor = BLACK

BEEP1 = pygame.mixer.Sound('beep1.ogg')
BEEP2 = pygame.mixer.Sound('beep2.ogg')
BEEP3 = pygame.mixer.Sound('beep3.ogg')
BEEP4 = pygame.mixer.Sound('beep4.ogg')

def drawButtons():
    pygame.draw.rect(screen, Y, (20,20,200,200))
    pygame.draw.rect(screen, B, (240,20,200,200))
    pygame.draw.rect(screen, R, (20,240,200,200))
    pygame.draw.rect(screen, G, (240,240,200,200))

pattern = []

def flashButtonAnimation(color):

    if color == Y:
       locationTuple = YELLOWRECT.topleft
       flashColor = BRIGHTYELLOW
       sound = BEEP1
    elif color == B:
        locationTuple = BLUERECT.topleft
        flashColor = BRIGHTBLUE
        sound = BEEP2
    elif color == R:
        locationTuple = REDRECT.topleft
        flashColor = BRIGHTRED
        sound = BEEP3
    elif color ==   G:
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
                color = Y
            if BLUERECT.collidepoint((mousex, mousey)):
                color = B
            if REDRECT.collidepoint((mousex, mousey)):
                color = R
            if GREENRECT.collidepoint((mousex, mousey)):
                color = G
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
                fontSurfaceObj = fontObj.render("game over"), True,
                (255, 0, 0),(255,255,255)
                screen.blit(fontSurfaceObj,(10,500))
                gameOver = True


                turn = "simon"


    if turn == "simon":
        pattern.append(random.choice(colors))
        print(pattern)
        for color in pattern:
            pygame.time.wait(250)
            flashButtonAnimation(color)

        turn = "player"





    pygame.display.update()

pygame.draw.rect(DISPLAYSURF, Y, (20,20,200,200))
