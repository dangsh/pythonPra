# 站立
def standArr():
    arr = [];
    for item in range(10):
        tempstr = "./imgs/king/kingStand/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;

# 前进
def qianArr():
    arr = [];
    for item in range(10):
        tempstr = "./imgs/king/kingMove/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;


# 后退
def backArr():
    arr = [];
    for item in range(8):
        tempstr = "./imgs/king/kingBack/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;

# 动作1
def action1Arr():
    arr = [];
    for item in range(15):
        tempstr = "./imgs/king/kingAttact/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;

# 动作2
def action2Arr():
    arr = [];
    for item in range(28):
        tempstr = "./imgs/king/kingAction2/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;

# 蹲下去
def downArr():
    arr = [];
    for item in range(5):
        tempstr = "./imgs/king/kingDown/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;

# 站起来
def upArr():
    arr = [];
    for item in range(5):
        tempstr = "./imgs/king/kingUp/a_" + str(item) + ".png";
        arr.append(tempstr);
    return arr;


