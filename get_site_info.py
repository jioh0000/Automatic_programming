import requests
from bs4 import BeautifulSoup

"""
url = "https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#s_content > div.section > ul > li > dl > dd.txt_inline')
    
    for eachTitle in title:
        print(eachTitle.text)
"""

url = "https://www.cntmart.com/product/productList.do"

response = requests.get(url)
titleList = []
priceList = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#product_list > li > a > cite')
    price = soup.select('#product_list > li > a > span.periodic > em')

    for eachTitle in title:
        eachTitle = eachTitle.text.replace('\t','')
        eachTitle = eachTitle.replace('\n','')
        eachTitle = eachTitle.replace(' ','')
        titleList.append(eachTitle)

    for eachPrice in price:
        eachPrice = (eachPrice.text).replace('\t','')
        eachPrice = eachPrice.replace('\n','')
        eachPrice = eachPrice.replace(' ','')
        priceList.append(eachPrice)
    

    for i in range(0,len(title)):
        print(titleList[i])
        print(priceList[i],end="---------")