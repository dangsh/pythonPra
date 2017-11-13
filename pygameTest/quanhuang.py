import pygame 
from pygame.locals import *
import sys

bg_img = pygame.image.load("./imgs/quanhuangbeijing.jpg")

sWidth = 752
sHeight = 224
screen = pygame.display.set_mode((sWidth , sHeight))

clock = pygame.time.Clock()
currentKey = ""
currentKey2 = ""
myPadding = 120
myVPadding = 20

class Person(pygame.sprite.Sprite):
    def __init__(self , name , img , moveArr = []):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.name = name 
        self.img = pygame.image.load(img).convert_alpha() 
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)

        self.direction = "stop"
        self.speed = 1
        self.moveArr = moveArr
        self.currentMoveIndex = 0
        self.zou = 0

        if self.name == "left": 
            self.rect.left = myPadding

        else:
            self.rect.left = sWidth - myPadding

        pHeight = self.img.get_height()
        self.rect.top = sHeight - pHeight -myVPadding

    def move(self):
        if self.direction == "up":
            # if self.positionY <= 0:
            #     self.positionY = 0
            # else:
            #     self.positionY -= self.speed
            pass

        if self.direction == "down":
            # if self.positionY >= 90:
            #     self.positionY = 90
            # else:
            #     self.positionY += self.speed
            pass


        if self.direction == "left":
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.speed
        if self.direction == "right":
            if self.rect.left >= 700:
                self.rect.left = 700
            else:
                self.rect.left += self.speed
        if self.direction == "stop" or self.direction == "up" or self.direction == "down":
            self.img = pygame.image.load(self.moveArr[0])
        else:
            self.zou += 1
            if self.zou >= 3000:
                self.zou = 0
            if self.zou % 30 == 0:
                self.currentMoveIndex = (self.currentMoveIndex + 1) % 4
                self.img = pygame.image.load(self.moveArr[self.currentMoveIndex])
            

        screen.blit(self.img , ( self.rect.left , self.rect.top , 100 , 100))

p1MoveArr = []
for i in range(4):
    tempString = "./imgs/king/r_" + str(i + 1) + ".png"
    p1MoveArr.append(tempString)

p2MoveArr = []
for i in range(4):
    tempString = "./imgs/k/l_" + str(i + 1) + ".png"
    p2MoveArr.append(tempString)



p1 = Person("left" , "./imgs/king/l_1.png" , p1MoveArr)   
p2 = Person("right" , "./imgs/K/l_1.png" , p2MoveArr)  


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                p1.direction = "up"
            if event.key == K_s:
                p1.direction = "down"
            if event.key == K_a:
                p1.direction = "left"
            if event.key == K_d:
                p1.direction = "right"
                currentKey = "right"
            if event.key == K_UP:
                p2.direction = "up"
            if event.key == K_DOWN:
                p2.direction = "down"
            if event.key == K_LEFT:
                p2.direction = "left"
                currentKey2 = "left"
            if event.key == K_RIGHT:
                p2.direction = "right"
            

        if event.type == KEYUP:

            if event.key == K_a or event.key == K_d:
                p1.direction = "stop"
                currentKey = ""
            if event.key == K_LEFT or event.key == K_RIGHT:
                p2.direction = "stop"
                currentKey2 = ""
    screen.blit(bg_img , (0 , 0 , 752 , 244))
    # screen.blit(p1.img , ( 0 , 0 , 100 , 100))
    p1.move()
    p2.move()
#碰撞检测
    if pygame.sprite.collide_mask(p1 , p2):
        if currentKey == "right" and currentKey2 == "":
            p2.direction = "stop"
            p2.rect.left = p1.rect.left + p1.img.get_width()
        if currentKey2 == "left" and currentKey == "":
            p1.direction = "stop"
            p1.rect.left = p2.rect.left - p1.img.get_width()

        if currentKey == "right" and currentKey2 == "left":
            p1.direction = "stop"
            p2.direction = "stop"
    pygame.display.flip()
    clock.tick(100)
    