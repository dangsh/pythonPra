import urllib.request
import json
import os
import ssl


# python 基础培训
url = "https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=687471686&album_id=301381083&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2F687471686%2FTB1jlwCHXXXXXcvXXXXXXXXXXXX_!!687471686-0-tstar.jpg&page=2&_ksTS=1502681447738_154&callback=jsonp155";
f = urllib.request.urlopen(url);#做网络请求
response = f.read().decode();#解码
# print(response.split("(")[1].split(")")[0]);
data = json.loads(response.split("(")[1].split(")")[0]);#取（）的中间部分
# print(data["list"]);

path = "./淘女郎";#路径和文件名
if(os.path.exists(path)):
    print("存在了,不用创建了");
else:
    print("不存在,需要创建新的");
    os.mkdir( path );

for item in data["picList"]:
    # print("index----:" , index);
    imageData = urllib.request.urlopen(item["http:"+"picUrl"]);
    pageNumber = item["picId"];

    oneImageUrl = item["picUrl"];
    context = ssl._create_unverified_context();
    oneImageData = urllib.request.urlopen(oneImageUrl , context=context).read();
    print("正在保存: " + str(pageNumber) + ".jpg");
    if os.path.exists(path + "/" + str(pageNumber) + ".jpg"):
        print(path + "/" + str(pageNumber) + ".jpg" + "已经存在...");
    else :
        f = open(path + "/" + str(pageNumber) + ".jpg" , "wb");
        f.write(oneImageData);
        f.flush();
        f.close();
        print(str(pageNumber) + "写入成功");
