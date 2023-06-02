import pygame, random
from time import sleep
from Constante import *
from Function import Start_Grid
from Function import ERASE
from Function import SIMULATION

pygame.init()

Win = pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()

# start of the function :
while run:
    clock.tick(FPS)
    Win.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if Play_button_rect.collidepoint(event.pos):
                Chose = 1
                continue
            if event.button == 1 :
                Chose = 2
                ADD = pygame.mouse.get_pos()
            elif event.button == 3 :
                Chose = 3
                DEL = pygame.mouse.get_pos()
            if Erase_button_rect.collidepoint(event.pos):
                Grid = ERASE()

    # For lauch the simulation !:
    if Chose == 1 :
        Grid = SIMULATION(Grid, Length, Scare_Number, Win)

    # For delete or add scare in the first grid :
    if Chose == 2 :
        Grid = Start_Grid(Length, Win, Scare_Number, ADD, Grid, Chose)
    elif Chose == 3 :
        Grid = Start_Grid(Length, Win, Scare_Number, DEL, Grid, Chose)
    else :
        Chose == 4
        Grid = Start_Grid(Length, Win, Scare_Number, DEL, Grid, Chose)

    if Chose != 1:
        Win.blit(Play_button, Play_button_rect)
        Win.blit(Erase_button, Erase_button_rect)

    pygame.display.update()
    sleep(0.01)
