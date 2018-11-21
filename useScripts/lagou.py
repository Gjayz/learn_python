import requests

import bs4
from bs4 import BeautifulSoup

global headers
global cookies

def get_total_page():
    kd = ['python工程师', 'python数据分析']
    city = ['北京', '上海', '深圳', '广州', '杭州', '成都', '南京', '武汉', '西安', '厦门', '长沙', '苏州', '天津']
    urls_kd = ['https://www.lagou.com/jobs/list_{}?px=default&city='.format(one) for one in kd]
    for urls in urls_kd:
        urls_city = [urls + one for one in city]
        for url in urls_city:
            response = requests.get(url, headers=headers, cookies=cookies)
            location = url.split('&')[-1].split('=')[1]
            key = url.split('/')[-1].split('?')[0].split('_')[1]
            soup = BeautifulSoup(response.text, 'lxml')
            pages = soup.find('span', {'class': 'span totalNum'}).get_text()
            print('职业：{}获取城市{}'.format(key, location))
            create_url(pages, location, key)

def create_url(pages, city, kd):
    for i in range(1, int(pages)+1):
        url='https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(city)
        get_data(url,i,kd)

def get_data(url,i,kd):
    print('第{}页数据'.format(i))
    formdata ={
        'first':'true',
        'pn':i,
        'kd':kd
    }
    response=requests.post(url,headers=headers,cookies=cookies,data=formdata)
    print(response);