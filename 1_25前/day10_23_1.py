from tkinter import *
import urllib.parse
import urllib.request
import json


class Page:
    page = 1
    a2dict = {}
    allc = []

page1 = Page()


def nameBtnFn():
    page1.page = 1
    starname = var_name.get()
    # print(starname)
    starnameurl = urllib.parse.quote(starname)
    url = "http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=" + starnameurl + "&page=1&pagesize=10&showtype=1&callback=kgJSONP238513750"
    result = urllib.request.urlopen(url)
    a = result.read()
    a = a.decode("utf-8")
    b = a[a.index("(") + 1:-1]
    c = json.loads(b)
    
    songNameList.delete(0 , END)

    for i in c["data"]["info"]:
        songNameList.insert(END , i["songname"]);
        page1.allc.append(i["songname"])
    songNameList.pack()

    

def showMessage():
    
    selects = songNameList.curselection();
    selectIndex = selects[0];


    # print(allc[selectIndex])    获取所点击的歌曲名

    starname = var_name.get()
    # print(starname)
    starnameurl = urllib.parse.quote(starname)
    print(page1.page);
    url = "http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=" + starnameurl + "&page=" + str(page1.page) + "&pagesize=10&showtype=1&callback=kgJSONP238513750"
    result = urllib.request.urlopen(url)
    a = result.read()
    a = a.decode("utf-8")
    b = a[a.index("(") + 1:-1]
    c = json.loads(b)
    c = json.loads(b)
    # print(type(c))   转化成dict

    inputname = page1.allc[selectIndex]
    for i in c["data"]["info"]:
        # print(i["songname"] , inputname);
        if i["songname"] == inputname:
            # print("进来了。。。。。");
            # print(i["hash"])  获取歌曲的hash值
            songhash = i["hash"]
            url2 = "http://m.kugou.com/app/i/getSongInfo.php?hash=" + songhash +"&cmd=playInfo"
            result2 = urllib.request.urlopen(url2)
            a2 = result2.read()
            # print(a2)
            a2 = a2.decode("utf-8")
            # print(a2)
            page1.a2dict = json.loads(a2)
            print(page1.a2dict["url"]) #*******************************************************最终的url
        # else:
        #     print("没进来。。。。");
    # print(page1.a2dict);
    
    f = urllib.request.urlopen(page1.a2dict["url"])   
    with open("%s.mp3" % (page1.allc[selectIndex]), "wb") as code:  
        code.write(f.read())   

def nextPgeFn():

    page1.a2dict = {}

    page1.page = page1.page + 1

    starname = var_name.get()
    # print(starname)
    starnameurl = urllib.parse.quote(starname)
    url = "http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=" + starnameurl + "&page=" + str(page1.page) + "&pagesize=10&showtype=1&callback=kgJSONP238513750"
    result = urllib.request.urlopen(url)
    a = result.read()
    a = a.decode("utf-8")
    b = a[a.index("(") + 1:-1]
    c = json.loads(b)
    
    songNameList.delete(0 , END)

    # print("---------------------------");

    # print(allc);
    page1.allc = [];
    for i in c["data"]["info"]:
        # print("进入for循环....");
        songNameList.insert(END , i["songname"]);
        page1.allc.append(i["songname"])

    # print("*(*************************************");
    # print(allc);
    songNameList.pack()
    print(page1.page);




#********************************************************************************方法



root = Tk()
root.title("MUSIC DOWNLOAD")
root.geometry('600x400')
l = Label(root , text = '---MUSIC DOWNLOAD---' , bg = 'green' , font = ("Arial" , 12) , width = 600 , height = 2)
l.pack()
# root.resizable(width = True , height = True)
#********************************************************************************标题

nameLabel = Label(root , text="歌星姓名");
nameLabel.pack();

var_name = StringVar()
nameEntry = Entry(root , textvariable = var_name);
nameEntry.pack();

nameBtn = Button(root , text="搜索" , command=nameBtnFn);
nameBtn.pack();

nextPgeBtn = Button(root , text = "下一页" , command = nextPgeFn)
nextPgeBtn.pack()


songNameList = Listbox(root);
songNameList.pack();

showMessageBtn = Button(root , text="下载" , command=showMessage);
showMessageBtn.pack();


#********************************************************************************界面代码



root.mainloop()