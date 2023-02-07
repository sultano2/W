import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((0,0,10))
pygame.display.set_caption("Game setup")
running = True
boxSize = ()
pygame.draw.line(screen, (255,255, 255), (150, 250), (450,250), 7)
pygame.draw.line(screen, (255,255, 255), (150, 350), (450,350), 7)
pygame.draw.line(screen, (255,255, 255), (250, 150), (250,450), 7)
pygame.draw.line(screen, (255,255, 255), (350, 150), (350,450), 7)

column = 0
row = 0
turn = "X"
board = [[None,None,None],[None,None,None],[None,None,None]]
col = 0
rw = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            mouseX = mousePosition[0]
            mouseY = mousePosition[1]
            print(mousePosition)
            if 150 < mouseX < 251 :
                col = 0
                column = 160
            if 251 < mouseX < 350  :
                col = 1
                column = 280
            if 350 < mouseX < 458 :
                column = 370
                col = 2
            if 150 < mouseY < 250 :
                rw = 0
                row = 150
            if 251 < mouseY < 350  :
                rw = 1
                row = 255
            if 350 < mouseY < 458 :
                row = 355
                rw = 2
            if turn == "X":
                font0bj = pygame.font.SysFont('tahoma', 80)
                fontSurface0bj = font0bj.render("X", True, (255, 255, 255), (0, 0, 0))
                screen.blit(fontSurface0bj, (column, row))
                board[rw][col] = "X";
                turn = "O"
            else:
                font0bj = pygame.font.SysFont('tahoma', 80)
                fontSurface0bj = font0bj.render("O", True, (255, 255, 255), (0, 0, 0))
                screen.blit(fontSurface0bj, (column, row))
                board[rw][col] = "O";
                turn = "X"
            print(board[0])
            if board[0][0] == board[0][1] and board[0][2]== board[0][0] and board[0][0] != None:
                print("You win")
            if board[1][0] == board[1][1] and board[1][2]== board[1][1] and board[1][0] != None:
                print("win")
            if board[2][0] == board[2][1] and board[2][2]== board[2][1] and board[2][0] != None:
                print("Win")
            if board[0][0] == board[1][0] and board[2][0]== board[2][1] and board[2][0] != None:
                print ("win")
            if board[0][1] == board[1][1] and board[2][1]== board[0][1] and board[1][1] != None:
                print ("win")
            if board[0][2] == board[1][2] and board[2][2]== board[0][2] and board[1][2] != None:
                print ("win")
            if board[0][2] == board[1][1] and board[2][0]== board[0][2] and board[1][1] != None:
                print("win")
            if board[0][0] == board[1][1] and board[2][2]== board[0][0] and board[1][1] != None:
                print("win")

    font0bj = pygame.font.SysFont('tahoma', 30)
    fontSurface0bj = font0bj.render("TIC", True, (255, 255, 255), (0, 0, 0))
    screen.blit(fontSurface0bj, (280, 0))

    font0bj = pygame.font.SysFont('tahoma', 20)
    fontSurface0bj = font0bj.render("Column", True, (255, 255, 255), (0, 0, 0))
    screen.blit(fontSurface0bj, (146, 120))

    font0bj = pygame.font.SysFont('tahoma', 20)
    fontSurface0bj = font0bj.render("Row", True, (255, 255, 255), (0, 0, 0))
    screen.blit(fontSurface0bj, (78, 280))

    pygame.display.update()
