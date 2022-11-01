import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((127,127,127))

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (130, 170), 30)
circle(screen, (255, 0, 0), (270, 170), 30)
circle(screen, (0, 0, 0), (270, 170), 15)
circle(screen, (0, 0, 0), (130, 170), 15)
rect(screen, (0, 0, 0), (130, 270, 140, 30))
rect(screen, (0, 0, 0), (130, 270, 140, 30))
polygon(screen, (0, 0, 0), [(170,150), (30,70), (37,60),(176,140), (170,150)])
polygon(screen, (0, 0, 0), [(230,150), (370,70), (360,55),(220,140), (230,150)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()