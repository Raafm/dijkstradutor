import pygame
from graph import nodes
pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill((0,0,0))


for node  in nodes:
    pygame.draw.circle(screen, (255,255,255),(node),20)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            quit()                          #exit() program


    pygame.display.update()
