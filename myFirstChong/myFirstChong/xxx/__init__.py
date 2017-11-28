from scrapy.exporters import JsonLinesItemExporter
from scrapy import signals 
from scrapy.extensions.feedexport import *
# JsonLinesItemExporter
# class chongxie(object):
#     def __init__(self , file , **kwargs):
#         print("???????????????????????????????????????????")
#         super(chongxie , self).__init__(file , ensure_ascii = None)

    def kaishi(self , spider):
        print("开始爬取。。。。。。。。。。。。。。。。。")
        self.myFile = open("shuju.json" , "wb")
        self.exporter = JsonLinesItemExporter(self.myFile , ensure_ascii = False)
        self.exporter.start_exporting()

    def guanbi(self , spider):
        print("爬取关闭。。。。。。。。。。。。。。。。。")
        self.exporter.finish_exporting()

        self.myFile.close()

        aaa = FTPFeedStorage("ftp://dangsh:5801200@012.3vftp.com/qqq.json")
        self.myFile = open("shuju.json" , "rb")
        aaa.store(self.myFile)


        

    @classmethod   
    def from_crawler(cls , crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.kaishi , signals.spider_opened)
        crawler.signals.connect(pipeline.guanbi , signals.spider_closed)
        return pipeline 

    def process_item(self ,  item , spider):
        self.exporter.export_item(item)
        return item