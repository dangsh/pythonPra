import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800 , 600))
pygame.display.set_caption("我的")

img1 = pygame.image.load("imgs/a.png")
# img2 = pygame.image.load("imgs/a.png")
positionX , positionY = (0 , 0)
direction = "stop"
isFullscreen = False

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYUP:
            direction = "stop"
        if event.type == KEYDOWN:
            if event.key == K_w:
                direction = "up"
            if event.key == K_s:
                direction = "down"
            if event.key == K_a:
                direction = "left"
            if event.key == K_d:
                direction = "right"
            if event.key == K_f:
                if isFullscreen == False:
                    bigScreen = pygame.display.list_modes()[0]
                    screen = pygame.display.set_mode(bigScreen , FULLSCREEN)
                    isFullscreen = True
                else :
                    screen = pygame.display.set_mode((800 , 600))
                    isFullscreen = False
            if event.key == K_q:
                direction = "right_down"

            if event.key == K_b:
                img1 = pygame.transform.scale2x(img1)
            if event.key == K_n:
                width = img1.get_size()[0]
                height = img1.get_size()[1]
                if width < 10:
                    width = 10
                if height < 10 :
                    height = 10
                img1 = pygame.transform.scale(img1 , (width //2 , height//2))    

    if direction == "down":
        positionY +=1
    if direction == "up":
        positionY -=1
    if direction == "left":
        positionX -=1
    if direction == "right":
        positionX +=1
    if direction == "right_down":
        positionX +=1
        positionY +=1


    screen.blit(img1 , (positionX , positionY , 100 , 100))
    pygame.display.flip()