# coding:utf-8
__author__ = 'qinman'
# create by qinman on 2018/3/28
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_field_pick').getOrCreate()
# sc = SparkContext(spark.sparkContext)
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_2",
        "hbase.client.scanner.timeout.period":"1000000", "hbase.mapreduce.scan.cachedrows": "10000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)


def url_func(x):
    import re
    if re.search(r'huangye88.com/[a-z]+/\d+_?\d+\.html', x[0]):
        return x

rdd = rdd.map(url_func).filter(lambda x: x != None)


def map_func(iter_x):
    import hashlib
    import urlparse
    import pymongo
    import happybase
    from happybase_monkey.monkey import monkey_path;monkey_path()
    import pyquery
    import json
    import collections
    import re
    from celery.app import Celery
    app = Celery(broker="redis://192.168.8.137:6379/7")
    app.conf.task_queue_max_priority = 255
    app.conf.task_ignore_result = True
    def md5(str, hex=True):
        '获取字符串的md5校验'
        m = hashlib.md5()
        m.update(str)
        if hex == True:
            return m.hexdigest()
        else:
            return m.digest()
    def img_url_handle(img_url):
        try:
            _ = img_url.split(".")
            a, b = ".".join(_[:-1]), _[-1]
            if b.startswith("jpg"):
                return a + ".jpg"
            if b.startswith("jpeg"):
                return a + ".jpeg"
            if b.startswith("png"):
                return a + ".png"
            if b.startswith("gif"):
                return a + ".gif"
            if b.startswith("JPEG"):
                return a + ".JPEG"
            if b.startswith("JPG"):
                return a + ".JPG"
            raise Exception()
        except:
            return img_url
    def image_to_upyun(page_url, img_url):
        try:
            img_url = urlparse.urljoin(page_url, img_url)
            url_md5 = md5(img_url)
            new_url = "//imgse.cn.gcimg.net/" + url_md5 + "." + img_url.split(".")[-1]
            while 1:
                try:
                    app.send_task("rawhttp.image_spider.crawl_to_upyun", (
                        img_url,), kwargs={"page_url": page_url},
                                  queue="rawhttp.image_spider")
                except:
                    pass
                else:
                    break
        except:
            new_url = ''
        return new_url
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return s
    def get_num(s, key):
        res = ''
        try:
            params = s.split('?')[-1].split('&')
        except:
            params = []
        for i in params:
            if key in i:
                res = i.split('=')[-1]
        return res
    def get_int(s):
        try:
            return int(float(str(s).split('.')[0]))
        except:
            return 0
    for x in iter_x:
        try:
            content = ''
            try:
                content = json.loads(x[1])["value"]
            except:
                pass
            if not content:
                continue
            try:
                content = get_unicode(content)
            except:
                pass
            doc = pyquery.PyQuery(content)
            for i in doc('img').items():
                if not i.attr('src'):
                    i.remove()
            source_url = x[0]
            try:
                title = re.search(u'【(.*)】', doc('title').text()).groups()[0]
            except:
                title = doc('title').text()
            cate_name_1, cate_name_2, cate_name_3 = '', '', ''
            price = 0
            price_unit = ''
            brand = ''
            keywords = ''
            wechat = ''
            telephone = ''
            com_addr = ''
            fax = ''
            attrs_kv = collections.OrderedDict()
            to_area = ''
            from_area = ''
            thumb, thumb_1, thumb_2 = '', '', ''
            try:
                update_time = doc('span.update-time').html().strip().split(u'：')[-1]
            except:
                update_time = ''
            if not update_time:
                try:
                    update_time = doc('div.litinfo span.dates').html().strip().split(u'：')[-1]
                except:
                    pass
            if not update_time:
                try:
                    update_time = doc('span.newdate').html().strip().split(u'：')[-1]
                except:
                    update_time = ''
            try:
                price = re.search(r'\d+', doc('ul.info-list span.price').text()).group()
            except:
                pass
            mobile = doc('ul.info-list span.mobile-number').text()
            seller = doc('ul.info-list span.text.mr8').text()
            qq = get_num(doc('a[class="qq-btn"]').attr('href'), 'uin')
            if not qq:
                qq = get_num(doc('p.names a[class="prsonqq"]').attr('href'), 'uin')
            if not qq:
                qq = get_num(doc('p.names a[class="line"]').attr('href'), 'uin')
            if not qq:
                qq = doc('a.line').text()
            if not qq:
                qq = get_num(doc('a[class="qq-ask"]').attr('href'), 'uin')
            ww = get_num(doc('a[class="ww-btn"]').attr('href'), 'uid')
            if not ww:
                ww = get_num(doc('a[class="wang"]').attr('href'), 'uid')
            if not ww:
                ww = doc('a.wang').text()
            price_m = []
            amount_m = []
            for i in doc('ul.info-list tbody tr').items():
                try:
                    price_m.append(re.search(r'(\d+).*(\d+)', i.text()).groups()[-1])
                except:
                    pass
                else:
                    try:
                        amount_m.append(re.search(r'(\d+).*(\d+)', i.text()).groups()[0])
                    except:
                        pass

            if not price_m:
                for i in doc('div.price-wp div.price-block').items():
                    try:
                        price_m.append(re.search(r'(\d+)', i('div.price').text()).groups()[-1])
                    except:
                        pass
                    else:
                        try:
                            amount_m.append(re.search(r'(\d+)', i('div.price-number').text()).groups()[0])
                        except:
                            pass
            min_price = min(price_m) if price_m else 0
            max_price = max(price_m) if price_m else 0
            min_amount = min(amount_m) if amount_m else 1
            for i in doc('ul.info-list li').items():
                if u'关键词' in i('span.label').text():
                    keywords = i('span.text').text()
                if u'微信号' in i('span.label').text():
                    wechat = i('span.text').text()
            if not doc('ul.info-list'):
                try:
                    price_m = [get_int(i.remove('font').text()) for i in doc('div.topprice .pri').items()]
                    min_price = min(price_m)
                    max_price = max(price_m)
                except:
                    pass
                else:
                    try:
                        amount_m = re.search(r'(\d+).?(\d+)', doc('div.topprice .unit').text()).groups()
                        min_amount = min(amount_m)
                    except:
                        pass
                for i in doc('ul.pro li').items():
                    if u'价格' in i('label').text() or u'标准价' in i('label').text():
                        if not price:
                            try:
                                price_all = i('h3').text().strip().split(' ')
                            except:
                                continue
                            else:
                                price = price_all[0]
                                if len(price_all) > 1:
                                    price_unit = price_all[1]
                    if u'品牌' in i('label').text():
                        brand = i('h3').text()
                    if u'关键词' in i('label').text():
                        keywords = i('h3').text()
                    if u'联系人' in i('label').text() and not seller:
                        seller = i('span').text()
                    if u'批发价' in i('label').text():
                        if not min_price:
                            price_m = []
                            amount_m = []
                            try:
                                for j in doc('tbody tr').items():
                                    price_m.append(re.search(r'(\d+).*(\d+)', j.text()).groups()[-1])
                                min_price = min(price_m)
                                max_price = max(price_m)
                            except:
                                pass
                            else:
                                try:
                                    amount_m.append(re.search(r'(\d+).*(\d+)', i.text()).groups()[0])
                                    min_amount = min(amount_m)
                                except:
                                    pass
                    if u'微信号' in i('label').text() and not wechat:
                        wechat = i('span').text()
                    if u'手机' in ''.join(i('label').remove('span').text().split(' ')) and not mobile:
                        mobile = i('span').text()
                    if u'固话' in ''.join(i('label').remove('span').text().split(' ')) and not telephone:
                        telephone = i('span').text()
            if not seller:
                seller = doc('.names').text()
            if not min_price:
                min_price = price
            if not max_price:
                max_price = price
            if not mobile:
                mobile = doc('.iphone span').text()
            com_name = doc('.company-info .cname a').attr('title')
            com_url = doc('.company-info .cname a').attr('href')
            if not com_name:
                com_name = doc('div.gsname a').attr('title')
            if not com_url:
                com_url = doc('div.gsname a').attr('href')
            for i in doc('div.addres p').items():
                if u'地址' in i.text():
                    com_addr = i.text().split(u'：')[-1]
                if u'电话' in i.text():
                    telephone = i('font').text()
                if u'传真' in i.text():
                    fax = i('font').text()
            if not com_name:
                com_name = doc('p.qyname a').attr('title')
            if not com_url:
                com_url = doc('p.qyname a').attr('href')
            if not com_addr:
                for i in doc('ul.zying li').items():
                    if u'地址' in i('label').text():
                        com_addr = i('span').text()
            _ = ''
            for i in doc('div.around div').items():
                if not i.attr('class'):
                    if not com_url:
                        com_url = i('a').attr('href')
                    if not com_name:
                        com_name = i('a').attr('title')
                    _ = i.remove('a').text()
            _ = _.split(' ')
            for i, v in enumerate(_):
                if u'地址' in v and len(_) > i + 1 and not com_addr:
                    com_addr = _[i + 1].split('\n')[0]
                if u'电话' in v and len(_) > i + 1 and telephone:
                    telephone = _[i + 1]
            if not min_amount:
                try:
                    min_amount = re.search(r'\d+', doc('span.unit').text().split(' ')[-1]).group()
                except:
                    pass
            if not telephone:
                telephone = doc('.show-phone-number').text()
            for i in doc('div.detail-info table td').items():
                attrs_kv[get_unicode(i('span.label').text())] = get_unicode(i('span.text').text())
            if not attrs_kv:
                keys = []
                attr = doc('.attributes td')
                for i in attr.items():
                    if i('td[class="attribute"]'):
                        k = get_unicode(i('.attribute').text())
                        if k:
                            keys.append(k)
                    if i('td[class="attribute-value"]'):
                        v = get_unicode(i('.attribute-value').text())
                        if v:
                            attrs_kv[keys[-1]] = v
            if not attrs_kv:
                for i in doc('div.basic-info table td').items():
                    if i('span.first').text() == u'在线联系':
                        res = []
                        try:
                            for ele in i('span.second a').items():
                                params = ele.attr('href').split('?')[-1].split('&')
                                base_url = ele.attr('href').split('?')[0]
                                res.append((params, base_url))
                        except:
                            res = []
                        for ele in res:
                            params = ele[0]
                            base_url = ele[1]
                            for j in params:
                                if 'taobao.com' in base_url and 'uid' in j:
                                    attrs_kv[get_unicode('ww')] = get_unicode(j.split('=')[-1])
                                if 'qq.com' in base_url and 'uin' in j:
                                    attrs_kv[get_unicode('qq')] = get_unicode(j.split('=')[-1])
                                if 'taobao.com' in base_url and 'uid' in j:
                                    attrs_kv[get_unicode('ww')] = get_unicode(j.split('=')[-1])
                    else:
                        attrs_kv[get_unicode(i('span.first').text())] = get_unicode(i('span.second').text())
            for k, v in attrs_kv.items():
                if u'面向地区' in k:
                    to_area = v
                if u'品牌' in k and not brand:
                    brand = v
                if u'产地' in k:
                    from_area = v
                if u'联系人' in k:
                    seller = v
                if u'手机' in k:
                    mobile = v
                if u'微信号' in k:
                    wechat = v
                if u'关键词' in k:
                    keywords = v
                if u'qq' in k:
                    qq = v
                if u'ww' in k:
                    ww = v
            attrs_kv = [('%s|%s' % (k, v)) for k, v in attrs_kv.items()]
            thumbs = set()
            for i in doc('div.smallpic img').items():
                if i.attr('data-src'):
                    thumbs.add(img_url_handle(i.attr('data-src')))
                elif 'none.jpg' not in i.attr('src'):
                    thumbs.add(img_url_handle(i.attr('src')))
                else:
                    pass
            for i, v in enumerate(thumbs):
                if i == 0:
                    thumb = image_to_upyun(source_url, v)
                if i == 1:
                    thumb_1 = image_to_upyun(source_url, v)
                if i == 2:
                    thumb_2 = image_to_upyun(source_url, v)
            if doc('.content img'):
                for i in doc('.content img').items():
                    i.attr('src', image_to_upyun(source_url, i.attr('src')))
            detail = doc('.content').outer_html()
            if not thumb:
                thumb = doc('.content img').attr('src')
            if not detail:
                if doc('.text-more img'):
                    for i in doc('.text-more img').items():
                        i.attr('src', image_to_upyun(source_url, i.attr('src')))
                detail = doc('.text-more').outer_html()
                if not thumb:
                    thumb = doc('.text-more img').attr('src')
            if not detail:
                if doc('.article img'):
                    for i in doc('.article img').items():
                        i.attr('src', image_to_upyun(source_url, i.attr('src')))
                detail = doc('.article').outer_html()
                if not thumb:
                    thumb = doc('.article img').attr('src')

            if re.search(r'huangye88.com/[a-z]+/\d+\.html', x[0]):
                cate = [i('a').attr('title') for i in doc('.breadcrumbs a').items()][1:-1]
                cate = [i('a').attr('title') for i in doc('.breadcrumb a').items()][0:-1] if not cate else cate
                for i, v in enumerate(cate):
                    if i == 0:
                        cate_name_2 = v
                    if i == 1:
                        cate_name_3 = v
            elif re.search(r'huangye88.com/[a-z]+/\d+_\d+\.html', x[0]):
                cate = []
                for i in doc('.head-mid a').items():
                    if i('a').attr('href') and u'黄页88网' not in i('a').text():
                        cate.append(i('a').attr('title'))
                cate = cate[0:-1]
                cate = [i('a').attr('title') for i in doc('.breadcrumb a').items()][0:-1] if not cate else cate
                for i, v in enumerate(cate):
                    if i == 0:
                        cate_name_1 = v
                    if i == 1:
                        cate_name_2 = v
                    if i == 2:
                        cate_name_3 = v
                if cate:
                    res = []
                    for i, v in enumerate(cate_name_1):
                        if v in cate_name_2 and v in cate_name_3 and cate_name_2.index(v) == i and cate_name_3.index(
                                v) == i:
                            res.append(v)
                        else:
                            res.append(' ')
                    res = u''.join(res).split(u' ')
                    if len(res) > 0:
                        res = res[0]
                    try:
                        cate_name_1 = re.search(u'%s(.+)?网' % (res,), cate_name_1).groups()[-1]
                    except:
                        pass
                    if cate_name_2:
                        cate_name_2 = cate_name_2.replace(res, '')
                    if cate_name_3:
                        cate_name_3 = cate_name_3.replace(res, '')

            _ = {
                'source_url': source_url,
                'title': get_unicode(title),
                'price': get_int(price),
                'min_price': get_int(min_price),
                'max_price': get_int(max_price),
                'price_unit': get_unicode(price_unit),
                'min_amount': min_amount,
                'keywords': get_unicode(keywords),
                'brand': get_unicode(brand),
                'to_area': get_unicode(to_area),
                'from_area': get_unicode(from_area),
                'attrs_kv': attrs_kv,
                'cate_name_1': get_unicode(cate_name_1),
                'cate_name_2': get_unicode(cate_name_2),
                'cate_name_3': get_unicode(cate_name_3),
                'thumb': '' if not thumb else thumb,
                'thumb_1': thumb_1,
                'thumb_2': thumb_2,
                'detail': get_unicode(detail),
                'com_name': get_unicode(com_name),
                'com_addr': get_unicode(com_addr),
                'seller': get_unicode(seller),
                'telephone': telephone,
                'mobile': mobile,
                'qq': qq,
                'ww': ww,
                'wechat': wechat,
                'fax': fax,
                'com_url': '' if not com_url else com_url,
                'update_time': get_unicode(update_time)
            }
            conn = happybase.Connection("192.168.14.1", 9090)
            try:
                conn.table('spider_hy88_2_json').put(x[0], {'info:json': json.dumps(_)})
            except:
                try:
                    conn = happybase.Connection("192.168.14.1", 9090)
                    conn.table('spider_hy88_2_json').put((x[0], {'info:json': json.dumps(_)}))
                except:
                    pass
        except Exception as e:
            pass
            mongo_client = pymongo.MongoClient("192.168.14.90", 27017)
            db = mongo_client["qinman"]
            try:
                db['fail'].insert_one({x[0], str(e)})
            except:
                pass

rdd.foreachPartition(map_func)
