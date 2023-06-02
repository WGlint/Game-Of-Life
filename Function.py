import random, pygame
from Constante import *

# Create Grid and with mouse add or delete scare :
def Start_Grid(Length, Win, Number_Scare, Pos, Grid, Chose):
    global iniz
    Scare_Size = int(Length / Number_Scare)
    X_Pos = int((Pos[0]) / (Scare_Size))
    Y_Pos = int((Pos[1]) / (Scare_Size))

    if Chose == 2 :
        Grid[Y_Pos][X_Pos] = 1
    elif Chose == 3 :
        Grid[Y_Pos][X_Pos] = 0

    # Delete the first black scare in 0,0 :
    if iniz == 0:
        if Pos == (0, 0):
            Grid[0][0] = 0
        else :
            iniz += 1

    for x in range(len(Grid)):
        for y in range(len(Grid)):
            if Grid[y][x] == 1:
                Scare = pygame.Surface((Scare_Size, Scare_Size))
                Scare.fill(BLACK)
                Win.blit(Scare, (x * Scare_Size, y * Scare_Size))

    return Grid

# Button ERASE for delete all scare in the grid :
def ERASE():
    global Grid
    Grid = zeros((Scare_Number, Scare_Number))
    return Grid

# lAUNCH THE SIMULATION ! :
def SIMULATION(Grid, Length, Number_scare, Win):
    New_Grid = zeros((Scare_Number, Scare_Number))
    Scare_Size = int(Length / Number_scare)
    for x in range(len(Grid)):
        for y in range(len(Grid)):
            Dead_Or_Alive = Neighbor_Matrice(Grid, x, y)
            if Grid[y][x] == 1:
                if (Dead_Or_Alive == 2) or (Dead_Or_Alive == 3):
                    New_Grid[y][x] = 1
                else :
                    New_Grid[y][x] = 0
            else :
                if Dead_Or_Alive == 3:
                    New_Grid[y][x] = 1
                else :
                    New_Grid[y][x] = 0

    for x in range(len(Grid)):
        for y in range(len(Grid)):
            if New_Grid[y][x] == 1:
                Scare = pygame.Surface((Scare_Size, Scare_Size))
                Scare.fill(BLACK)
                Win.blit(Scare, (x * Scare_Size, y * Scare_Size))

    return New_Grid

# How number neighbor have scare :
def Neighbor_Matrice(Grid, x, y):
    Neighbor = 0
    Coord_x = [-1, 0, 1, 1, 1, 0, -1, -1]
    Coord_y = [-1, -1, -1, 0, 1, 1, 1, 0]
    for X,Y in zip(Coord_x, Coord_y):
        try :
            if ((y + Y) == -1) or ((x + X) == -1):
                continue
            Neighbor += Grid[y + Y][x + X]
        except :
            Neighbor += 0
    return int(Neighbor)