# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True);

# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('胡亚洲')[0];
# 发送文本给好友
my_friend.send('Hello WeChat!')
# 发送图片
# my_friend.send_image('1.jpg')

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):

    return 'received: {} ({})'.format(msg.text, msg.type)



# 进入 Python 命令行、让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()