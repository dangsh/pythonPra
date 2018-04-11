from pyquery import PyQuery as pq
doc = pq(filename='content.html')
try:
    for i in doc('.hotproword a').items():
        print i('a').attr('href') 
except:
    pass
