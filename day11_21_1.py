import requests
import json
# response = requests.get("http://www.baidu.com")
# print("--------------")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))

# response.encoding="utf-8"
# print(response.text)

# data = {
#     "name":"zhaofan" ,
#     "age" : 22
# }

# response = requests.get("http://httpbin.org/get" , params = data)
# print(response.url)
# print("--------------")
# print(response.text)



# response = requests.get("http://www.baidu.com")
# print(type(response.text))
# print(response.text)
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))


# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
# }

# response = requests.get("https://www.zhihu.com" , headers = headers)
# print(response.text)

# response = requests.get("http://www.baidu.com")
# print(type(response.status_code) , response.status_code)
# print(type(response.headers) , response.headers)
# print(type(response.cookies) , response.cookies)
# print(type(response.url) , response.url)
# print(type(response.history) , response.history)


# response = requests.get("http://www.baidu.com")
# print(response.cookies)

# for key,value in response.cookies.items():
#     print(key+"="+value)


# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)


proxies = {
    "http" : "http://127.0.0.1:9999" ,
    "https" : "http://127.0.0.1:8888"
}
response = requests.get("https://www.baidu.com" , proxies = proxies)
print(response.text)