# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 下午4:13
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows


import talib as ta
import tushare as ts
import datetime
from email_notice import mail
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def return_constraintdict(stockcodelist,email ):


    for stockcode in stockcodelist:
        rs = ts.get_hist_data(stockcode, start='2019-03-20', end='2019-03-21')
        # malist = ta.MA(np.array(rs), timeperiod=20)
        dd = ts.get_sina_dd(stockcode,'2019-03-21')
        # print (dd)
        ff = ts.get_realtime_quotes(stockcode)
        for row in ff.itertuples(index=True, name='Pandas'):
            print getattr(row,"name"),"股票名字"
            print getattr(row,"open"),'开盘价格'
            print getattr(row,"pre_close"),"昨日收盘价"
            print getattr(row,"price"),"当前价格"
            print getattr(row,"high"),"今日最高价"
            print getattr(row,"low"),"今日最低价"
            print getattr(row,"bid"),"买一"
            print getattr(row,"ask"),"卖一"
            name = getattr(row,"name")
            open = getattr(row,"open")
            close_pre = getattr(row,"pre_close")
            price = getattr(row,"price")
            bid = getattr(row,"bid")
            ask = getattr(row,"ask")
            bid_clo = float(bid)-float(close_pre)
            op_cl = float(open)-float(close_pre)
            # pct = chajia / float(close_pre) * 100  # 当日买一和昨日收盘价的比值
            # opct = (float(open)-float(close_pre))/float(close_pre) * 100  # 当日开盘价和昨日收盘价的比值
            message = "股票代码:"+str(stockcode)+\
                      "股票名:"+str(name)+\
                      "开盘价:"+str(open)+\
                      "收盘价:"+str(close_pre)+\
                      "当前价:"+str(price)+\
                      "买一:"+str(bid)+\
                      "卖一:"+str(ask)+\
                      "差价:"+str(bid_clo)+\
                      "pct:"+str(op_cl)
            if op_cl>0:
                mail(email , message)


def my_func(stockcodelist , emails):
    """
    1：open，今日开盘价
    2：pre_close，昨日收盘价
    3：price，当前价格
    4：high，今日最高价
    5：low，今日最低价
    6：bid，竞买价，即“买一”报价
    7：ask，竞卖价，即“卖一”报价
    8：volumn，成交量 maybe you need do volumn/100
    9：amount，成交金额（元 CNY）
    10：b1_v，委买一（笔数 bid volume）
    11：b1_p，委买一（价格 bid price）
    12：b2_v，“买二”
    13：b2_p，“买二”
    14：b3_v，“买三”
    15：b3_p，“买三”
    16：b4_v，“买四”
    17：b4_p，“买四”
    18：b5_v，“买五”
    19：b5_p，“买五”
    """
    result = ""
    for stockcode in stockcodelist:
        df = ts.get_realtime_quotes(stockcode)
        # dd = ts.get_sina_dd(stockcode, '2019-03-22')
        # print dd
        for data , row in df.iterrows():
            name = row["name"]
            open = row["open"]
            pre_close = row["pre_close"]
            price = row["price"]
            high = row["high"]
            low = row["low"]
            bid = row["bid"]
            ask = row["ask"]
            volume = row.get("volume" , "")
            amount = row["amount"]

            bid_clo = float(bid) - float(pre_close)  # 买一和昨日收盘价的差值
            op_cl = float(open) - float(pre_close)  # 今日开盘价和昨日收盘价的差值
            pct = bid_clo / float(pre_close) * 100  # 当日买一和昨日收盘价的比值
            opct = op_cl / float(pre_close) * 100  # 当日开盘价和昨日收盘价的比值
            avg = (float(high) + float(low)) / 2  # 今日股价实时均值
            p_a = float(price) - float(avg)  # 当前值和均值的差值
            stua = p_a / float(avg) * 100  # 当前股价和平均价格的比值

            message = "  股票代码:"+str(stockcode) + '\n'+\
                      " 股票名:"+str(name) + '\n'+\
                      " 今日开盘价:"+str(open) + '\n'+\
                      " 昨日收盘价:"+str(pre_close) + '\n'+\
                      " 当前价格:"+str(price) + '\n'+\
                      " 今日最高价:"+str(high) + '\n'+\
                      " 今日最低价:"+str(low) + '\n'+\
                      " 买一:"+str(bid) + '\n'+\
                      " 卖一:"+str(ask) + '\n'+\
                      " 成交量:"+str(volume) + '\n'+\
                      " 成交金额:"+str(amount) + '\n'

            if abs(pct) > 1.3 or abs(opct) > 2 or abs(stua) > 0.6 :
                for email in emails:
                    print email
                    print mail(email, message)


if __name__ == '__main__':
    stockcodelist = ['000725' , '600104']
    emails = ["zhangxiaogang@gongchang.com" , "894781617@qq.com"]
    my_func(stockcodelist , emails)