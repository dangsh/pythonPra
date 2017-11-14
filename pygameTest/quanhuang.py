import pygame 
from pygame.locals import *
import sys
import kFire
import kingFire

import threading

bg_img = pygame.image.load("./imgs/quanhuangbeijing.jpg")

sWidth = 752
sHeight = 224
screen = pygame.display.set_mode((sWidth , sHeight))

clock = pygame.time.Clock()
currentKey = ""
currentKey2 = ""
myPadding = 120
myVPadding = 70

class Person(pygame.sprite.Sprite):
    # 键盘弹起事件
    def keyUpFn(self):
        self.direction = "stop"
        self.zou = 0;
        self.currentMoveIndex = 0;

    # 绘制血条方法
    def drawBloodLine(self):
        starx = 0 if self.name == "left" else  sWidth * 2 / 3;
        endxx = sWidth / 3 if self.name == "left" else sWidth;
        xuetiaoWidth = sWidth / 3;
        endx = starx + self.hp / 100 * xuetiaoWidth;
        pygame.draw.line(screen , (100 , 100 , 100) , (starx , 0) , (endxx , 0) , 40);
        pygame.draw.line(screen , (0 , 255 , 0) , (starx , 0) , (endx , 0) , 40);

    # 激活动作
    def beginActive(self , actionName , actionIndex):
        if self.isActive == False:
            self.direction = actionName;
            self.isActive = True;
            self.currentAction = actionIndex;

    # 执行动作方法
    def actionFn(self , arr):
        self.at1 += 1;
        if self.at1 % 8 == 0:
            self.img = pygame.image.load(arr[self.currentAt1Index])
            if self.name == "right":
                self.img = pygame.transform.flip(self.img , True , False);
            self.currentAt1Index = self.currentAt1Index + 1;
            if self.currentAt1Index == len(arr):
                self.actionTimer.start();
                self.wanbi = True;
                self.currentAt1Index = 0;
                self.direction = "stop";

    # 按频率执行动作
    def serialAction(self , arr):
        self.zou += 1
        if self.zou >= 3000:
            self.zou = 0
        if self.zou % 30 == 0:
            self.currentMoveIndex = (self.currentMoveIndex + 1) % len(arr)
            self.img = pygame.image.load(arr[self.currentMoveIndex])
            if self.name == "right":
                self.img =  pygame.transform.flip(self.img , True , False);

    # 重置动作
    def reset(self):
        self.isActive = False;
        self.wanbi = False;
        self.actionTimer.cancel();
        self.actionTimer = threading.Timer(1 , self.reset)

    # 被打击之后的重置方法
    def bloodReset(self):
        self.isblooding = False;
        self.bloodTimer.cancel();
        self.bloodTimer = threading.Timer(1 , self.bloodReset);

    # 被打击方法
    def hited(self):
        self.hp -= 10;
        self.isblooding = True;
        self.bloodTimer.start();
        print(self.hp);
    
    # 初始化方法
    def __init__(self , name , img , qianArr = []):
        
        pygame.sprite.Sprite.__init__(self)

        self.isActive = False;

        self.isDown = False;

        self.wanbi = False;

        self.hp = 100;
        self.isblooding = False;

        self.bloodTimer = threading.Timer(1 , self.bloodReset);

        # 控制动作cd
        self.actionTimer = threading.Timer(1 , self.reset);

        # 动作1
        self.at1 = 0;
        self.currentAt1Index = 0;
        
        self.name = name 
        self.img = pygame.image.load(img).convert_alpha() 
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)

        self.direction = "stop"
        self.speed = 1
        self.qianArr = qianArr

        # 移动
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
            if self.currentAction == "111":
                self.direction = "action1";
            if self.currentAction == "222":
                self.direction = "action2";
            

        # 上
        if self.direction == "up":
            pass

        # 下
        if self.direction == "down":
            if self.isActive == False:
                self.serialAction(self.downArr);

        # 左
        if self.direction == "left":
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.speed

            if self.isActive == False:
                self.serialAction(self.qianArr);
        
        # 右
        if self.direction == "right":
            if self.rect.left >= 700:
                self.rect.left = 700
            else:
                self.rect.left += self.speed
            if self.isActive == False:
                self.serialAction(self.qianArr);
       
        # 停止不动
        if self.direction == "stop":
            self.serialAction(self.standArr);
        
        # 动作1
        if self.direction == "action1":
            self.actionFn(self.action1Arr);

        # 动作2
        if self.direction == "action2":
            self.actionFn(self.action2Arr);
      

        # 绘制英雄    
        self.mask = pygame.mask.from_surface(self.img)
        screen.blit(self.img , ( self.rect.left , self.rect.top , 100 , 100))
        

        # 绘制血条
        self.drawBloodLine();




p1 = Person("left" , "./imgs/king/l_1.png" , kingFire.qianArr())  
p1.backArr = kingFire.backArr();
p1.upArr = kingFire.upArr();
p1.downArr = kingFire.downArr();
p1.standArr = kingFire.standArr();
p1.action1Arr = kingFire.action1Arr();
p1.action2Arr = kingFire.action2Arr();


p2 = Person("right" , "./imgs/K/l_1.png" , kFire.qianArr())
p2.backArr = kFire.backArr();
p2.upArr = kFire.upArr();
p2.downArr = kFire.downArr();
p2.standArr = kFire.standArr();
p2.action1Arr = kFire.action1Arr();
p2.action2Arr = kFire.action2Arr();



while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            # 动作
            # 英雄1
            if event.key == K_j:
                p1.beginActive("action1" , "111");
            if event.key == K_k:
                p1.beginActive("action2" , "222");
            # 英雄2
            if event.key == K_KP1:
                p2.beginActive("action1" , "111");
            if event.key == K_KP2:
                p2.beginActive("action2" , "222");
            

            # 方向
            # 英雄1
            if event.key == K_w:
                p1.direction = "up"
            if event.key == K_s:
                p1.direction = "down"
                p1.currentMoveIndex = 0;
            if event.key == K_a:
                p1.direction = "left"
            if event.key == K_d:
                p1.direction = "right"
                currentKey = "right"
            # 英雄2
            if event.key == K_UP:
                p2.direction = "up"
            if event.key == K_DOWN:
                p2.direction = "down"
                p2.currentMoveIndex = 0;
            if event.key == K_LEFT:
                p2.direction = "left"
                currentKey2 = "left"
            if event.key == K_RIGHT:
                p2.direction = "right"  
            

        # 键盘弹起事件
        if event.type == KEYUP:
            # 英雄1
            if event.key == K_a or event.key == K_d or event.key == K_w or event.key == K_s:
                p1.keyUpFn();
                currentKey = ""
            # 英雄2
            if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
                p2.keyUpFn();
                currentKey2 = ""
                    
    screen.blit(bg_img , (0 , 0 , 752 , 244))
    p1.move()
    p2.move()

    #碰撞检测
    if pygame.sprite.collide_mask(p1 , p2):

        # p1攻击 p2没攻击
        if p1.isActive == True and p2.isActive == False:
            if p2.isblooding == True:
                pass;
            else: 
                p2.hited();

        # p2攻击 p1没攻击
        if p2.isActive == True and p1.isActive == False:
            if p1.isblooding == True:
                pass;
            else: 
                p1.hited();

        # p1 ， p2 都攻击
        if p2.isActive == True and p2.isActive == False:
            if p1.isblooding == True:
                pass;
            else: 
                p1.hited();

            if p2.isblooding == True:
                pass;
            else: 
                p2.hited();
            

        # print("pengdaole ....");
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
    clock.tick(200)
    