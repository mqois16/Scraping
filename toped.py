from numpy import dtype
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.tokopedia.com/samsung/product'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
items = soup.findAll('div', 'css-qa82pd')
for item in items:
    productName = item.find('div', 'css-1b6t4dn').text
    productPrice = item.find(
        'div', 'css-1ksb19c').text.replace('.', '').replace('Rp ', '')
    productSold = item.find('span', 'css-1duhs3e').text.replace('Terjual ', '')
    #Rating = item.find('span', 'css-t70v7i').text.replace('.', '')
    Rating = 4
    Toko = "Samsung Official Store"
    Lokasi = "Jakarta"
    Date = datetime.today().strftime('%Y-%m-%d')

    kirim = {'idx': '', 'Produk': productName, 'Harga': int(productPrice), 'Terjual': int(
        productSold), 'Rating': int(Rating), 'Toko': Toko, 'Lokasi': Lokasi, 'Date': Date}

    reqPost = requests.post(
        'http://127.0.0.1/pmldi2api/crawl.php?function=insert_data', data=kirim)
    print(reqPost)
    print(reqPost.json())
    #print(productName, " | ", productPrice, " | ", productSold," | ", Rating, " | ", Toko, " | ", Lokasi, " | ", Date)
