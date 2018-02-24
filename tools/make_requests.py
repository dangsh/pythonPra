import requests
import json

def getText(url):
	response = requests.get(url)
	text = response.text
	return text

def getJsonText(url):
	text = getText(url)
	text = json.loads(text)
	return text

if __name__ == '__main__':
	url = 'http://proxy.nghuyong.top/?num=50'
	print(getText(url))

