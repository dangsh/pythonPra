import json
import redis
def read_data():
	with open('goods_url.json',encoding='utf-8') as f:
		for i in range(54263949):
		# for i in range(10):
			line=f.readline()
			a = line[:-2]
			d = json.loads(a)
			url = d["goods_url"][0]
			new_url = 'https:' + url
			r.lpush("hcSpider:start_urls",new_url)

if __name__ == "__main__":
	r=redis.Redis(host='192.168.8.88',port='6379',db=0,decode_responses=True)
	read_data()