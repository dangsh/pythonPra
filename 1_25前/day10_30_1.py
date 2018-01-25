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
	starnameurl = urllib.parse.quote(starname) #把明星的名字编码成url编码
	url = "http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=" + starnameurl + "&page=1&pagesize=10&showtype=1&callback=kgJSONP238513750"
	result = urllib.request.urlopen(url)
	a = result.read()
	a = a.decode("utf-8")
	b = a[a.index("(") + 1 : -1]
	# print(b)
	c =json.loads(b)

	songNameList.delete(0 , END)

	for i in c["data"]["info"]:
		songNameList.insert(END , i["songname"])
		page1.allc.append(i["songname"])
	songNameList.pack()

def nextPgeFn():
	pass

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

    inputname = page1.allc[selectIndex]
    for i in c["data"]["info"]:
    	if i["songname"] == inputname:
    		songhash = i["hash"]
    		url2 = "http://m.kugou.com/app/i/getSongInfo.php?hash=" + songhash +"&cmd=playInfo"
    		result2 = urllib.request.urlopen(url2)
    		a2 = result2.read()
    		a2 = a2.decode("utf-8")
    		page1.a2dict = json.loads(a2)
    		print(page1.a2dict)


root = Tk()
root.title("Music Download")
root.geometry("600x400")
l = Label(root , text = '---Music Download---' , bg = 'green' , font = ("Arial" , 12) , width = 600 , height = 2)
l.pack()


nameLabel = Label(root , text="歌星姓名")
nameLabel.pack()

var_name = StringVar()
nameEntry = Entry(root , textvariable = var_name)
nameEntry.pack()

nameBtn = Button(root , text = "搜索" , command = nameBtnFn)
nameBtn.pack()
nextPgeBtn = Button(root , text = "下一页" , command = nextPgeFn)
nextPgeBtn.pack()

songNameList = Listbox(root)
songNameList.pack()

showMessageBtn = Button(root , text = "下载" , command = showMessage)
showMessageBtn.pack()

root.mainloop()