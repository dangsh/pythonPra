import urllib.request
import urllib.parse
import json


a = urllib.parse.quote("刘德华")

url = "http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=" + a + "&page=1&pagesize=10&showtype=1&callback=kgJSONP238513750&qq-pf-to=pcqq.group"
req = urllib.request.Request(url)

url2 = "http://m.kugou.com/app/i/getSongInfo.php?hash={0}&cmd=playInfo"

result = urllib.request.urlopen(req)
reqString = result.read().decode('utf-8')
reqString = reqString[reqString.index("(") + 1:-1]
hjson = json.loads(reqString)
for key in hjson["data"]["info"]:
    url_one = url2.format(key["hash"])
    req_one = urllib.request.Request(url_one)
    result_one = urllib.request.urlopen(req_one)
    reqString_one = result_one.read().decode('utf-8')
    hjson_one = json.loads(reqString_one)
    print(hjson_one["url"])








