# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 下午3:51
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_user = 'xxx'  # 收件人邮箱账号，我这边发送给自己


def mail(email , data):
    if '8947' in email:
        my_sender = '894781617@qq.com'  # 发件人邮箱账号
        my_pass = 'ezdsqqxgrtcrbdjf'  # 发件人邮箱密码
    else:
        my_sender = '954316227@qq.com'  # 发件人邮箱账号
        my_pass = 'ogbhphuvxamqbegj'  # 发件人邮箱密码

    ret = True
    try:
        msg = MIMEText(data, 'plain', 'utf-8')
        msg['From'] = formataddr(["股票信息", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", email])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "今日份股票快讯"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [email, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

if __name__ == "__main__":
    ret = mail("894781617@qq.com" , "123")
    print ret
