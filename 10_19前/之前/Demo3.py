import urllib.request
import json
import ssl
import os
context=ssl._create_unverified_context();

urlString ="https://wenku.baidu.com/browse/getbcsurl?doc_id=1dc6b92fed630b1c59eeb535&pn=1&rn=99999&type=ppt&callback=jQuery11010517763534630248_1502612840328&_=1502612840329";
response=urllib.request.urlopen(urlString); #做网络请求
#print(response.read().decode());
resultStr=response.read().decode();#解码
resultArr=resultStr.split("(");#将你的字符串按照某个字符来分割
result=resultArr[1].split(")")[0];#去除右括号分割的前部分
#print(result);
jsonData=json.loads(result);
listArr=jsonData["list"];#取出list部分
#print(listArr);

def saveImage(oneImageUrl,urlIndex):
    oneImageData=urllib.request.urlopen(oneImageUrl,context=context).read();
    
    mkpath="C:\Users\张霄港\Desktop\python";
    mkdir(mkpath); 
    
    print("正在保存>>>>>>>>>>>"+str(urlIndex));

    #mkdir(mkpath);
    
    f=open("liuyifei"+str(urlIndex)+".jpg","wb");
    
    f.write(oneImageData);
    f.flush;
    f.close;

def mkdir(path):
    isExists=os.path.exists(path);
    if not isExists:
        os.makedirs(path);
        print path+'创建成功'
        return True;
    else:
        print path+'目录已存在'
        return False;

for item in listArr:
   # print(item["zoom"]);
   page=item["page"];
   pageUrl=item["zoom"];
   saveImage(pageUrl,page);