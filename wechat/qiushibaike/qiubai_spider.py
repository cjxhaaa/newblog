import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/'

def get_html(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		'Accept':'text/css,*/*;q=0.1'
	}
	r = requests.get(url,headers=headers)
	r.encoding = 'utf8'
	bsobj = BeautifulSoup(r.text,'lxml')
	return bsobj

def get_jokes(url):
	'''
	获取糗事百科段子
	:param url: 
	:return: 
	'''
	joke_list = []
	soup = get_html(url)
	jokes = soup.find_all('div',class_='article block untagged mb15 typs_hot')
	for joke in jokes:
		article = joke.find('div',class_='content').get_text(strip=True)
		author = joke.find('img')['alt']
		if joke.find('div',class_='thumb'):
			url = joke.find('div',class_='thumb').img['src']
			pic_url = 'http:'+url
			print('作者：{}\n{}\n{}\n'.format(author,article,pic_url))
		else:
			print('作者：{}\n{}\n'.format(author,article))


def spider(url):
	r = requests.get(url)
	page = r.text
	soup = BeautifulSoup(page,'html.parser')
	texts = soup.find_all('div',class_='content')
	jokes = []
	x = 0
	for text in texts:
	    dt = text.get_text().strip('\n')
	    
	    x += 1
	    print(('第{}个笑话：{}').format(x,dt))
	    jokes.append(dt)

if __name__ == '__main__':
	url = 'https://www.qiushibaike.com/'
	spider(url)




