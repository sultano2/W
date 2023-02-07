import pygame, sys

from pygame.locals import *

pygame.init()

colors = ["R","G","B","Y"]

Y = (155, 155, 0)
B = (0, 0, 155)
R = (155, 0, 0)
G = (0, 155, 0)

BY = (255,255, 0)
BB = ( 0, 0, 255)
BR = (255, 0, 0)
BG = ( 0, 255, 0)

YELLOWRECT = pygame.Rect(20,20, 200, 200)
BlUERECT = pygame.Rect(240, 20, 200, 200)
REDRECT= pygame.Rect(20, 240, 200, 200)
GREENRECT= pygame.Rect(240, 240, 200, 200)

BEEP1 = pygame.mixer.Sound('beep1.ogg')
Beep2 = pygame.mixer.Sound('beep2.ogg')
Beep3 = pygame.mixer.Sound('beep3.ogg')
Beep4 = pygame.mixer.Sound('beep4.ogg')


pattern = []

move = 0

running = True
turn = "simon"
gameOver = False

def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint((x,y)):
        return Y
    elif BlUERECT.collidepoint((x,y)):
        return B
    elif REDRECT.collidepoint((x,y)):
        return R
    elif GREENRECT.collidepoint((x,y)):
        return G
    return None

def flashButtonAnimation(color):

    if color == Y:
       locationTuple = YELLOWRECT.topleft
       flashcolor = BY
       Sound = BEEP1
    elif color == B:
        locationTuple = BlUERECT.topleft
        flashcolor = BB
        Sound = Beep2
    elif color == R:
        locationTuple = REDRECT.topleft
        flashcolor = BR
        Sound = Beep3
    elif color == G:
        locationTuple = GREENRECT.topleft
        flashcolor = BG
        Sound = Beep4



        Sound.play()
        pygame.draw.rect(screen, flashcolor, (locationTuple[0], locationTuple[1], 200,200))
        pygame.display.update()
        pygame.time.wait(500)
        drawButtons()
        pygame.display.update()


def drawButtons():
    pygame.draw.rect(screen, Y, (20, 20, 200, 200))
    pygame.draw.rect(screen, B, (240, 20, 200, 200))
    pygame.draw.rect(screen, R, (20, 240, 200, 200))
    pygame.draw.rect(screen, G, (240, 240, 200, 200))







screen = pygame.display.set_mode((480,480))
screen.fill((0, 0, 120))
pygame.display.set_caption("Game Setup")

running = True
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
        flashButtonAnimation(Color)
        if Color == pattern[move]:
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

    pygame.draw.rect(screen, Y, (20,20,200,200))
