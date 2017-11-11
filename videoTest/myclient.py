import socket
from PIL import Image
import pygame

from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((160 , 120))

pygame.display.flip()
clock = pygame.time.Clock()

c = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

c.bind(("127.0.0.1" , 7777))

while True:
    data , addr = c.recvfrom(80000)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    a = pygame.image.frombuffer(data , ( 160 , 120) , "RGB")
    screen.blit(a , (0 , 0 , 160 , 120))    
    pygame.display.update()
    
    clock.tick()



# c = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
# c.bind(("127.0.0.1" , 7777))
# while True:
#     data , addr = c.recv(80000)
