ATM = [{'cardNum':'1111' , 'cardPassw':'1111', 'cardMoney':1000} , {'cardNum':'2222' , 'cardPassw':'2222' , 'cardMoney':1000} , {'cardNum':'3333' , 'cardPassw':'3333' , 'cardMoney':1000} , {'cardNum':'4444' , 'cardPassw':'4444' , 'cardMoney':1000} , {'cardNum':'5555' , 'cardPassw':'5555' , 'cardMoney':1000}]

def quqian(j):
    a = input('请输入要取的钱数')
    a = int(a)
    # print(type(j['cardMoney']))
    j['cardMoney'] = j['cardMoney'] - a

def cunqian(j):
    a = input('请输入要存的钱')
    a = int(a)
    j['cardMoney'] = j['cardMoney'] + a

def gaimima(j):
    a = input('请输入要修改的密码')
    j['cardPassw'] = a


while True:
    inputCardNum = input('请输入你的卡号：')
    for i in ATM:   
        # print(inputCardNum)
        # print(i)
        # print(i['cardNum'])
        
        if i['cardNum'] == inputCardNum:
            inputPass = input('请输入你的密码：')
            if i['cardPassw'] == inputPass:
                print('**********************')
                print('请选择功能')
                print('1.查询余额')
                print('2.取钱')
                print('3.存钱')
                print('4.修改密码')
                print('5.退出系统')
                print('**********************')

                while True:
                    choiceNum = input('请选择功能::::')
                    if choiceNum == '1':
                        print(i['cardMoney'])
                        print('**********************')
                        continue
                    elif choiceNum == '2':
                        print('开始取钱')
                        quqian(i)
                        print('**********************')
                        continue
                    elif choiceNum == '3':
                        print('开始存钱')
                        cunqian(i)
                        print('**********************')
                        continue
                    elif choiceNum == '4':
                        print('开始修改密码')
                        gaimima(i)
                        print('**********************')
                        continue
                    elif choiceNum == '5':
                        break
            
            else:
                print("密码错误")
        
        else:
            continue
