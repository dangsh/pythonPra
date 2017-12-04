from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    username = models.CharField(max_length=100); # 昵称
    headimg = models.CharField(max_length=100); # 头像
    phone = models.CharField(max_length=100); # 手机号
    pwd = models.CharField(max_length=100); # 密码
    wxid = models.CharField(max_length=100); # 微信id
    accounntmoney = models.CharField(max_length=100); # 账户余额
    rewardmoney = models.CharField(max_length=100); # 抽奖余额
    activecode = models.CharField(max_length=100); # 激活码
    redpack = models.CharField(max_length=100); # 红包
    upperson = models.CharField(max_length=100); # 上级
    downperson = models.CharField(max_length=100); # 下级
    rebate = models.CharField(max_length=100); # 返利
    integral = models.CharField(max_length=100); # 积分
    bankcard = models.CharField(max_length=100); # 银行卡
    power = models.CharField(max_length=100); # 权限
    address = models.CharField(max_length=100); # 收货地址
    registetime = models.DateTimeField(auto_now_add=True); # 注册时间




# 浏览记录表 lookhistory
class Lookhistory(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    userid = models.CharField(max_length=100); # 用户id
    goodsid = models.CharField(max_length=100); # 商品id
    looktime = models.DateTimeField(auto_now_add=True); # 浏览时间


# 商品表 goods
class Goods(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    rebate = models.CharField(max_length=100); # 返利
    lookhistoryid = models.CharField(max_length=100); # 浏览记录id
    standard = models.CharField(max_length=100); # 规格
    images = models.CharField(max_length=1000); # 配图
    details = models.CharField(max_length=1000); # 详情
    shopname = models.CharField(max_length=100); # 所属商家
    status = models.CharField(max_length=100); # 状态
    uptime = models.DateTimeField(auto_now_add=True); # 上架时间
    downtime = models.DateTimeField(auto_now_add=True); # 下架时间



# 购物车表 carts
class Carts(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    number = models.IntegerField(default=0); # 数量
    goodsid = models.CharField(max_length=100); # 商品id
    userid = models.CharField(max_length=100); # 用户id


# 订单表 ordertable
class Goods(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    userid = models.CharField(max_length=100); # 用户id
    goodsid = models.CharField(max_length=100); # 商品id
    ordertime = models.CharField(max_length=100); # 时间
    isaudit = models.BooleanField(default=True); # 是否审核
    ispass = models.BooleanField(default=True); # 是否通过
    iscancel = models.BooleanField(default=True); # 是否取消
    ispay = models.BooleanField(default=True); # 是否付款
    issend = models.BooleanField(default=True); # 是否发货
    ispaydone = models.BooleanField(default=True); # 付款是否完成
    isclose = models.BooleanField(default=True); # 订单是否关闭



# 订单记录表 orderlist
class Orderlist(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    orderid = models.CharField(max_length=100); # 订单id
    userid = models.CharField(max_length=100); # 用户id



# 积分记录表 score
class Score(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    userid = models.CharField(max_length=100); # 用户id
    getpath = models.CharField(max_length=100); # 获得方式
    scorecount = models.CharField(max_length=100); # 积分数量
    scoretime = models.DateTimeField(auto_now_add=True); # 时间



# 搜藏表 favorite
class Favorite(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    goodsid = models.CharField(max_length=100); # 商品id
    userid = models.CharField(max_length=100); # 用户id
    favtime = models.DateTimeField(auto_now_add=True); # 搜藏时间



# 充值表 recharge
class Recharge(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    userid = models.CharField(max_length=100); # 用户id
    rechargetime = models.DateTimeField(auto_now_add=True); # 充值时间
    money = models.CharField(max_length=100); # 金额
    status = models.CharField(max_length=100); # 状态




# 返利表 rewardtable
class Rewardtable(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    userid = models.CharField(max_length=100); # 用户id






# 好友表 friends
class Friends(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    friendid = models.CharField(max_length=100); # 好友id




# 红包表 redpacktable
class Friends(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    redtime = models.DateTimeField(auto_now_add=True); # 时间


# 福袋表 lucky
class Lucky(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    goodsid = models.CharField(max_length=100); # 商品id


# 广告表 ad
class Ad(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    adtime = models.DateTimeField(auto_now_add=True); # 时间



# 活动表 activetable
class Activetable(models.Model):
    id = models.CharField(max_length=100 , primary_key=True); # id
    activetime = models.DateTimeField(auto_now_add=True); # 时间
    activedetail = models.CharField(max_length=1000); # 详情





    




