class Small:
    hp = 50
    daojv = "无"

    def __init__(self):
        self.lostHpNum = 3

    def run(self):
        print('僵尸在跑,生命值是：',self.hp,'道具是',self.daojv)
    
    
class Mid(Small):
    hp = 80
    daojv = "路障"
    def __init__(self):
        self.lostHpNum = 2



class Big(Small):
    hp = 120
    daojv = "铁桶"
    def __init__(self):
        self.lostHpNum = 1

z = Small()

while True:
    print('打僵尸游戏开始')
    print('*****************')
    print('僵尸类型：：：')
    print('1.普通僵尸')
    print('2.路障僵尸')
    print('3.铁桶僵尸')
    print('4.退出游戏')
    print('*****************')
    choice = input('请选择要攻击的僵尸类型')
    if choice == '1':
        z = Small()
        z.run()
    elif choice == '2':
        z = Mid()
        z.run()
    elif choice == '3':
        z = Big()
        z.run()
    elif choice == '4':
        quit()



    while True:
        a = input('如果要攻击僵尸请按\'k\'键并回车')
        if a == 'k':
            z.hp = z.hp - z.lostHpNum
            if z.hp > 0:
                print('我是僵尸，我现在的生命值是：',z.hp)
            else: 
                print('我是僵尸，我死了')
                print('*****************')
                print('*****************')
                print('*****************')
                break
        elif a == '4':
            print('退出游戏')
            quit()