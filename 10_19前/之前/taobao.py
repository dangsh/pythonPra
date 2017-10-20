import tool
import urllib.request
import re
import os
import json
# 创建一个类
class Spider:
    def __init__(self):
        self.homeUrl = "https://mm.taobao.com/json/request_top_list.htm";
        self.tool = tool.Tool();

    def savePagesInfo(self , pageIndex):
        urlString = self.homeUrl + "?page=" + str(pageIndex);

        response = urllib.request.urlopen(urlString).read().decode("gbk");

        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S);

        itemArr = re.findall(pattern , response);

        contents = [];
        for item in itemArr:
            contents.append([item[0] , item[1] , item[2] , item[3] , item[4]]);

        for item in contents:
            # print("有一个模特叫：" , item[2] , "年龄：" , item[3] , "家住:" , item[4] , "个人信息：" , item[0]);
            mm_name = item[2];
            mm_url = item[0];
            pattern = re.compile(r'\d+');
            mm_id = pattern.findall(mm_url)[0];
            # print(mm_id);

            # 相册地址
            albumsUrl = "https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=" + mm_id;

            albumReponse = urllib.request.urlopen(albumsUrl);
            albumReponse = albumReponse.read().decode("gbk");
            # print(albumReponse);

            resStr = r"<h4>(.*?)</h4>";

            mmAlbums = re.findall(resStr , albumReponse , re.I|re.S|re.M);

            # print(mmAlbums);

            for item in mmAlbums:
                # 相册的名字
                res = r"<a .*?>(.*?)</a>";
                albumName = re.findall(res , item , re.S|re.I|re.M);
                # print(albumName[0].strip());
                albumName = albumName[0].strip();
                # print(mm_name + "的" + albumName + "相册");

                # 相册的id
                # 获取相册的地址
                res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')";
                mm_link = re.findall(res , item , re.I|re.M|re.S)[0];
                # print(mm_link);

                # 根据人和相册的名字去创建文件夹
                # xxx/豹纹相册
                albumName = albumName.replace("..." , "");
                albumPath = mm_name + "/" + albumName;
                albumPath = albumPath.strip();
                # 根据路径来创建文件夹
                isExist = os.path.exists(albumPath);
                if not isExist:
                    os.makedirs(albumPath);
                else :
                    print("已经存在了 不需要创建.....");

                mm_link = "http:" + mm_link;

                # url 解析
                result = urllib.parse.urlparse(mm_link);
                params = urllib.parse.parse_qs(result.query , True);

                pageNumber = 1;
                mm_link = "https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=" + params["user_id"][0] + "&album_id=" + params["album_id"][0] + "&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2F687471686%2FTB1jlwCHXXXXXcvXXXXXXXXXXXX_!!687471686-0-tstar.jpg&page=" + str(pageNumber) + "&_ksTS=1502652171209_154&callback=jsonp15";                

                images = urllib.request.urlopen(mm_link);
                images = images.read().decode("gbk");
                # print(images);

                imagesJson = json.loads(images.strip()[9:-1]);

                imagesList = imagesJson["picList"];
                for index , oneImage in enumerate(imagesList):
                    if (os.path.exists(albumPath + "/" + str(index) + ".jpg")):
                        print(albumPath + "/" + str(index) + ".jgp 已经存在了...");
                        continue;
                    

                    oneImageUrl = "http:" + oneImage["picUrl"];
                    print("正在保存" + albumPath + "/" + str(index) + ".jpg....");
                    f = open(albumPath + "/" + str(index) + ".jpg" , "wb");
                    oneImageData = urllib.request.urlopen(oneImageUrl).read();
                    f.write(oneImageData);
                    f.flush();
                    f.close();




# 通过类创建对象
spider = Spider();

# 开始请求
spider.savePagesInfo(2);