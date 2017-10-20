import random
a = [3 , 4 , 1 , 8 , 2 , 8 , 11]
b = [0 , 0 , 0 , 0 , 0 , 0 , 0]

randNumber = random.randint(0,len(a)-1)
for i in a:
    if b[randNumber] == 0:
       b[randNumber] = i
    else:
        while b[randNumber] != 0:
            randNumber = random.randint(0,len(a)-1)
        b[randNumber] = i
print(b)

