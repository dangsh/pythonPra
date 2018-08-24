import xlrd
import os
import requests
import re

def download_image(name , list):
    homedir = os.getcwd()
    filePath = homedir + '\\' + name + '1' + '\\'
    dirs = os.listdir(homedir)
    i = 1
    for dir in dirs:
        title = dir[:-1]
        if name == title:
            i = i + 1
    filePath = homedir + '\\' + name + str(i)  + '\\'
    if not os.path.exists(filePath):
        os.makedirs(filePath)

    for i in range(len(list)):
        tail = list[i].split('.')[-1]
        pic_path = (filePath + name + str(i) + '.'+tail)
        try:
            pic = requests.get(list[i])
            f = open(pic_path, 'wb')
            f.write(pic.content)
            f.close()
        except:
            pass
homedir = os.getcwd()
dirs = os.listdir(homedir)  
xls = ''  
for i in dirs:
    a , b = i.split('.')
    if b == 'xls' or b == 'xlsx':
        xls = i
book = xlrd.open_workbook(xls)
sheet = book.sheet_by_name('已签到')
line_index = 0
beizhu_index = 0
tu_index = 0
for i in range(sheet.nrows):
    # print(sheet.row_values(i))
    if '手机标识' in sheet.row_values(i):
        line_index = i
        list = sheet.row_values(i)
        beizhu_index = list.index('备注')
        tu_index = list.index('图1')
for i in range(line_index+1 ,sheet.nrows):
    list = sheet.row_values(i)
    beizhu = ""
    tu_list = []
    try:
        beizhu = list[beizhu_index]
    except:
        pass
    for j in range(10):
        tu = ""
        tu = sheet.hyperlink_map.get((i,tu_index+j))
        if tu:
            tu = tu.url_or_path
            tu_list.append(tu)
    print('正在下载-->'  , beizhu)
    download_image(beizhu , tu_list)

