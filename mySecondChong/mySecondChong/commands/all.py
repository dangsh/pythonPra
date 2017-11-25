from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerRunner

#将列表容器中的数据做成字典 方便使用
from scrapy.utils.conf import arglist_to_dict



class Command(ScrapyCommand):
    requires_project = True #依赖工程
    



    def syntax(self):
        """
        Command syntax (preferably one-line). Do not include command name.
        """
        return "your self pinxie"

    def short_desc(self):
        return "your self pinxie"

    
    def add_options(self, parser):
        ScrapyCommand.add_options(self , parser)
        
        parser.add_option("-a", dest="mySparks", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")


    def process_options(self, args, opts):
        ScrapyCommand.process_options(self , args , opts)
        try:
            opts.mySparks = arglist_to_dict(opts.mySparks)
        except ValueError:
            raise UserWarning("你的值有问题")

    def run(self, args, opts):
        allSpider = self.crawler_process.spider_loader
        for spiderName in allSpider.list():
            print("current spiderName = %s .........................."% spiderName)
            self.crawler_process.crawl(spiderName , **opts.mySparks)

        
        self.crawler_process.start()
