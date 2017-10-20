import urllib.request
import json
import os
import ssl



# python基础知识培训_旋风竹影
url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=06f386163868011ca300a6c30c2259010202f3b6&pn=1&rn=99999&type=ppt&callback=jQuery110102743184720724776_1502329681659&_=1502329681660";

# python 基础培训
url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=7f25793443323968011c92dc&pn=1&rn=99999&type=ppt&callback=jQuery1101014181073525434473_1502337821248&_=1502337821249";
f = urllib.request.urlopen(url);#做网络请求
response = f.read().decode();#解码
# print(response.split("(")[1].split(")")[0]);
data = json.loads(response.split("(")[1].split(")")[0]);#取（）的中间部分
# print(data["list"]);

path = "./python基础培训";#路径和文件名
if(os.path.exists(path)):
    print("存在了,不用创建了");
else:
    print("不存在,需要创建新的");
    os.mkdir( path );

for item in data["list"]:
    # print("index----:" , index);
    imageData = urllib.request.urlopen(item["zoom"]);
    pageNumber = item["page"];

    # fh = open(path + "/" + str(pageNumber) + ".jpg" , "w+");
    # fh.write(imageData.read().decode("utf-8"));
    # fh.close();

    oneImageUrl = item["zoom"];
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

    

    

    # print("item.zoom-----:" , item["zoom"]);
    # print("item.page-----:" , item["page"]);
