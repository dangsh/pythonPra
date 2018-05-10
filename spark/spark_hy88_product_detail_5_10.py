# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 10
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hy88_get_product_detail').getOrCreate()
sc = spark.sparkContext

rdd = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.14.90/final_field.hy88").load()
def map_func(iter_x):
    from pyquery import PyQuery as pq
    from gcpy_utils.spider.handle import data_to_online
    for x in iter_x:
        _id = ""
        cate_name_3 = ""
        cate_name_2 = ""
        price_unit = ""
        telephone = ""
        to_area = ""
        keywords = ""
        thumb = ""
        title = ""
        detail = ""
        seller = ""
        min_price = ""
        cate_name_1 = ""
        brand = ""
        fax = ""
        thumb_2 = ""
        price = ""
        thumb_1 = ""
        attrs_kv = ""
        min_amount = ""
        source_url = ""
        ww = ""
        wechat = ""
        com_addr = ""
        qq = ""
        mobile = ""
        com_url = ""
        from_area = ""
        update_time = ""
        max_price = ""
        com_name = ""
        scan = ""
        data = x.asDict()
        try:
            _id = data['_id']
            cate_name_3 = data['cate_name_3']
            cate_name_2 = data['cate_name_2']
            price_unit = data['price_unit']
            telephone = data['telephone']
            to_area = data['to_area']
            keywords = data['keywords']
            thumb = data['thumb']
            title = data['title']
            detail = data['detail']
            seller = data['seller']
            min_price = data['min_price']
            cate_name_1 = data['cate_name_1']
            brand = data['brand']
            fax = data['fax']
            thumb_2 = data['thumb_2']
            price = data['price']
            thumb_1 = data['thumb_1']
            attrs_kv = data['attrs_kv']
            min_amount = data['min_amount']
            source_url = data['source_url']
            ww = data['ww']
            wechat = data['wechat']
            com_addr = data['com_addr']
            qq = data['qq']
            mobile = data['mobile']
            com_url = data['com_url']
            from_area = data['from_area']
            update_time = data['update_time']
            max_price = data['max_price']
            com_name = data['com_name']
            scan = data['scan']
        except:
            pass
        try:
            doc = pq(detail)
        except:
            pass
        doc.find('embed').remove()
        doc.find('script').remove()
        doc('#showMore').remove()
        detail = doc.html()
        if doc('#textMore'):
            detail = doc('#textMore').html(method='html')
        if doc('.text-more'):
            detail = doc('.text-more').html(method='html')
        final_data = {
            'cate_name_3' : cate_name_3 ,
            'cate_name_2' : cate_name_2 ,
            'price_unit' : price_unit ,
            'telephone' : telephone ,
            'to_area' : to_area ,
            'keywords' : keywords ,
            'thumb' : thumb ,
            'title' : title ,
            'detail' : detail ,
            'seller' : seller ,
            'min_price' : min_price ,
            'cate_name_1' : cate_name_1 ,
            'brand' : brand ,
            'fax' : fax ,
            'thumb_2' : thumb_2 ,
            'price' : price ,
            'thumb_1' : thumb_1 ,
            'attrs_kv' : attrs_kv ,
            'min_amount' : min_amount ,
            'source_url' : source_url ,
            'ww' : ww ,
            'wechat' : wechat ,
            'com_addr' : com_addr ,
            'qq' : qq ,
            'mobile' : mobile ,
            'com_url' : com_url ,
            'from_area' : from_area ,
            'update_time' : update_time ,
            'max_price' : max_price ,
            'com_name' : com_name ,
            'scan' : scan ,
        }
        data_to_online("hy88_product", _id, final_data)
rdd.foreachPartition(map_func)