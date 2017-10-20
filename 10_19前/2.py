a = [1 , 2 , 3 , 4 , 5 , 6 ]

s = [0 , 0 , 0 , 0 , 0 , 0 ]

boolDie = [0 , 0 , 0 , 0 , 0 , 0 ]

shu = 1
die = 0

while die < len(a):
    for i in a:
        if boolDie[i-1] != 99:
            if shu % 3 != 0:
                # print(i,'没死')
                shu = shu + 1
                continue

            else:
                print(i,'死了')
                shu = shu + 1
                die = die + 1
                boolDie[i-1]=99
                continue