import urllib.request
import re
import ssl
import os
import tool
import json
# import urlparse

class Spider:
    def __init__(self):
        self.siteUrl = 'http://mm.taobao.com/json/request_top_list.htm';
        self.tool = tool.Tool();

    def getPage(self , pageIndex):
        url = self.siteUrl + '?page=' + str(pageIndex);
        context = ssl._create_unverified_context();
        response = urllib.request.urlopen(url , context=context);
        return response.read().decode("gbk");

    # 获取MM个人详情页面
    def getDetailPage(self , infoUrl):
        context = ssl._create_unverified_context();
        response = urllib.request.urlopen(infoUrl , context=context);
        return response.read().decode("gbk");

    # 获取个人文字简介
    def getBrief(self , mm_infoUrlId):

        context = ssl._create_unverified_context();
        infoUrl = "https://mm.taobao.com/self/info/model_info_show.htm?user_id=" + mm_infoUrlId;
        response = urllib.request.urlopen(infoUrl , context=context);
        content = response.read().decode("gbk");
        pattern = re.compile(r'<label.*?>(.*?)<\/label>[\s]*<span>(.*?)<\/span>');
        items = pattern.findall(content);
        return items;

    # 获取页面所有图片
    def getAllImg(self , mm_infoUrlId , name):
        images = [];
        context = ssl._create_unverified_context();
        infoUrl = "https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=" + mm_infoUrlId;
        response = urllib.request.urlopen(infoUrl , context=context);
        content = response.read().decode("gbk");
        res = r'<h4>(.*?)</h4>';
        mm = re.findall(res , content , re.S|re.M);

        for item in mm:
            # print(item);
            # 相册地址
            res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')";
            link = re.findall(res , item , re.I|re.S|re.M);
            # print(link[0]);

            # 相册名字
            res = r'<a .*?>(.*?)</a>';
            title = re.findall(res , item , re.S|re.M);
            # print(title[0].strip());


            albumPath = name + title[0].strip();
            self.mkdir(name + "/" + albumPath);

            # 开始根据相册地址请求相册
            albumUrl = "http:" + link[0];
            result = urllib.parse.urlparse(albumUrl);
            params = urllib.parse.parse_qs(result.query , True);

            pageNumber = 1;
            imagesUrl = "https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=" + params["user_id"][0] + "&album_id=" + params["album_id"][0] + "&top_pic_id=0&page=" + str(pageNumber) + "&callback=jsonp233"

            imagesResult = urllib.request.urlopen(imagesUrl , context=context);
            # encoding = imagesResult.info().get_content_charset('utf8')  # JSON default
            # data = json.loads(raw_data.decode(encoding))
            result = imagesResult.read().decode("gbk");
            resultJson = json.loads(result.replace('\r' , '').replace('\t' , '').replace('\n' , '')[9:-1]);

            for index , image in enumerate(resultJson["picList"]):
                if(os.path.exists(name + "/" + albumPath + "/" + str(index) + ".jpg")):
                    print("已经有" + name + "/" + albumPath + "/" + str(index) + ".jpg" + "了.....");
                    continue;
                # print(index);
                # print(image["picUrl"]);
                oneImageUrl = "http:" + image["picUrl"];
                oneImageData = urllib.request.urlopen(oneImageUrl , context=context).read();
                print("正在保存: " + name + "/" + albumPath + "/" + str(index) + ".jpg");

                f = open(name + "/" + albumPath + "/" + str(index) + ".jpg" , "wb");
                f.write(oneImageData);
                f.flush();
                f.close();

            



    # 保存多张写真图片
    def saveImgs(self, images, name):
        number = 1
        print (u"发现", name, u"共有", len(images), u"张照片");
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageURL, fileName)
            number += 1

    # 保存头像
    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL, fileName)

    # 保存个人简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print (u"正在偷偷保存她的个人信息为", fileName);
        f.write(content.encode('utf-8'))
        f.close();

    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print (u"正在悄悄保存她的一张图片为", fileName);
        f.close()

    def getContents(self , pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append([item[0], item[1], item[2], item[3], item[4]])
        # contents.append([items[0][0] , items[0][1] , items[0][2] , items[0][3] , items[0][4]]);
        return contents

    # 写入图片
    def saveImage(self , imageUrl , fileName):
        u = urllib.request.urlopen(imageUrl);
        data = u.read();
        f = open(fileName , "wb");
        f.write(data);
        f.close();

    # 写入文本
    def saveBrief(self , content , name):
        fileName = name + "/" + name + ".txt";
        f = open(fileName , "wb");
        print (u"正在偷偷的保存她的信息为:" , fileName)
        str = "";
        for item in content:
            str += item.__str__();
        # content = " ".join(content);
        f.write(str.encode("utf-8"));
        f.close();

    # 创建新的目录
    def mkdir(self , path):
        path = path.strip();
        isExists = os.path.exists(path);
        if not isExists:
            os.makedirs(path);
            return True;
        else:
            return False;

    # 将一页淘宝MM的信息保存起来
    def savePageInfo(self, pageIndex):
        # 获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        print(contents);
        for item in contents:
            # item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print (u"发现一位模特,名字叫", item[2], u"芳龄", item[3], u",她在", item[4]);
            print (u"正在偷偷地保存", item[2], "的信息");
            print (u"又意外地发现她的个人地址是", item[0]);
            pattern = re.compile(r'\d+');
            mm_infoUrlId = pattern.findall(item[0])[0];

            # 个人详情页面的URL
            detailURL = 'https://mm.taobao.com/self/model_info.htm?user_id=' + mm_infoUrlId + '&is_coment=false';
            # 得到个人详情页面代码
            detailPage = self.getDetailPage(detailURL);

            # # 获取个人简介
            # brief = self.getBrief(mm_infoUrlId)
            # self.mkdir(item[2])
            # # 保存个人简介
            # self.saveBrief(brief, item[2])


            # 获取所有图片列表
            images = self.getAllImg(mm_infoUrlId , item[2])

            # # 保存头像
            # self.saveIcon(item[1], item[2])
            # # 保存图片
            # self.saveImgs(images, item[2])

    # 传入起止页码，获取MM图片
    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print (u"正在偷偷寻找第", i, u"个地方，看看MM们在不在");
            self.savePageInfo(i)


spider = Spider();
# spider.getContents(1);
spider.savePagesInfo(1 , 12);
