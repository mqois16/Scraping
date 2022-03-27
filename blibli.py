import requests
from bs4 import BeautifulSoup

url = 'https://www.blibli.com/backend/search/products?sort=&page=1&start=0&searchTerm=samsung&intent=false&merchantSearch=true&multiCategory=true&category=TA-1000003&category=HA-1000002&customUrl=&channelId=mobile-web&showFacet=false&userIdentifier=undefined&isMobileBCA=false'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
items = soup.findAll('div', 'product__list')
for item in items:
    productName = item.find(
        'div', 'product__item product__item__list-view').text
    productPrice = item.find('div', 'product__body__price__display').text
    print(productName, " | ", productPrice)
