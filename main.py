import pygame

# initialize pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((900, 700))


# RGB = Red, Green, Blue
screen.fill((250, 250, 0))


# Title and Icon
pygame.display.set_caption("CAT DASH")
icon = pygame.image.load('cat.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('cat-2.png')
playerX = 275
playerY = 634

def player(x,y):
    screen.blit(playerImg, (x, y))
player(playerX, playerY)   
pygame.display.update()

# Game Loop and controling player
running = True
while running:
         
         # RGB = Red, Green, Blue
         screen.fill((250, 250, 0))
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
                 
if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_LEFT:
         playerX_change = -0.1
     if event.key == pygame.K_RIGHT:
         playerX_change = 0.1
if event.type == pygame.KEYUP:
     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
         playerX_change = 0



# Updating the code
playerX += playerX_change
player(playerX, playerY)   
pygame.display.update()
