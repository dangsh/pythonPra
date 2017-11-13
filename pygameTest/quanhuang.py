import pygame 
from pygame.locals import *
import sys
import kFire
import threading
import kingFire

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
    def reset(self):
        self.isActive = False
        self.actionTimer.cancel()
        self.actionTimer = threading.Timer(1 , self.reset)
        self.wanbi = False

    def bloodReset(self):
        self.isblooding = False
        self.bloodTimer.cancel()
        self.bloodTimer = threading.Timer(1 , self.bloodReset)

    def hited(self):
        self.hp -= 10
        self.isblooding = True
        self.bloodTimer.start()
        print(self.hp)

    def __init__(self , name , img , moveArr = []):



        self.wanbi = False
        
        pygame.sprite.Sprite.__init__(self)
        
        self.isActive = False

        self.hp = 100
        self.isblooding = False
        self.bloodTimer = threading.Timer(1 , self.bloodReset)
        #控制动作cd
        self.actionTimer = threading.Timer(1 , self.reset)

        #动作1
        self.at1 = 0
        self.currentAt1Index = 0

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
        if self.isActive == True and self.wanbi == False:
            self.direction = "action1"

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
            if self.isActive == False:
                self.zou += 1
                if self.zou >= 3000:
                    self.zou = 0
                if self.zou % 30 == 0:
                    self.currentMoveIndex = (self.currentMoveIndex + 1) % 4
                    self.img = pygame.image.load(self.moveArr[self.currentMoveIndex])

        if self.direction == "action1":   
            self.at1 += 1
            if self.at1 % 10 == 0:
                self.img = pygame.image.load(self.action1[self.currentAt1Index])
                if self.name =="right":
                    self.img = pygame.transform.flip(self.img , True , False)
                self.currentAt1Index = self.currentAt1Index + 1
                if self.currentAt1Index == len(self.action1):
                    #一秒之后isActive == falselse
                    self.actionTimer.start()
                    self.wanbi = True
                    self.currentAt1Index = 0
                    self.direction = "stop"
                
        else:
            self.at1 = 0
            self.currentAt1Index = 0
        
        self.mask = pygame.mask.from_surface(self.img)
        screen.blit(self.img , ( self.rect.left , self.rect.top , 100 , 100))
        
        startx = 0 if self.name == "left" else sWidth * 2 / 3
        endxx = sWidth / 3 if self.name == "left" else sWidth
        xuetiaoWidth =sWidth / 3
        endx = startx + self.hp / 100 * xuetiaoWidth


        pygame.draw.line(screen , (100 , 100 , 100) , (startx , 0) , (endxx , 0) , 50)
        pygame.draw.line(screen , (0 , 255 , 0) , (startx , 0) , (endx , 0) , 50)

p1MoveArr = []
for i in range(4):
    tempString = "./imgs/king/r_" + str(i + 1) + ".png"
    p1MoveArr.append(tempString)

p2MoveArr = []
for i in range(4):
    tempString = "./imgs/k/l_" + str(i + 1) + ".png"
    p2MoveArr.append(tempString)



p1 = Person("left" , "./imgs/king/l_1.png" , p1MoveArr)   
p1.action1 = kingFire.action1()
p2 = Person("right" , "./imgs/K/l_1.png" , p2MoveArr)  
p2.action1 = kFire.action1()

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

            if event.key == K_1:
                if p2.isActive == False:
                    p2.direction = "action1"
                    p2.isActive = True

            if event.key == K_j:
                if p1.isActive == False:
                    p1.direction = "action1"
                    p1.isActive = True
                

            if event.key == K_UP:
                p2.direction = "up"
            if event.key == K_DOWN:
                p2.direction = "down"
            if event.key == K_LEFT:
                if p2.isActive == False:
                    p2.direction = "left"
                    currentKey2 = "left"
            if event.key == K_RIGHT:
                if p2.isActive == False:
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

        if p1.isActive == True and p2.isActive == False:
            if p2.isblooding == True:
                pass
            else:
                p2.hited()

        if p2.isActive == True and p1.isActive == False:
            if p1.isblooding == True:
                pass
            else:
                p1.hited()   

        if p2.isActive == True and p2.isActive == False:
            if p1.isblooding == True:
                pass
            else:
                p1.hited()
            if p2.isblooding == True:
                pass
            else:
                p2.hited()
        # if currentKey == "right" and currentKey2 == "":
        #     p2.direction = "stop"
        #     p2.rect.left = p1.rect.left + p1.img.get_width()
        # if currentKey2 == "left" and currentKey == "":
        #     p1.direction = "stop"
        #     p1.rect.left = p2.rect.left - p1.img.get_width()

        # if currentKey == "right" and currentKey2 == "left":
        #     p1.direction = "stop"
        #     p2.direction = "stop"
    pygame.display.flip()
    clock.tick(100)
    