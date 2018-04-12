from pyquery import PyQuery as pq
doc = pq(filename='look.html')
try:
    for i in doc('.hot-search ul li a').items():
        print i('a').attr('href') 
except:
    pass
