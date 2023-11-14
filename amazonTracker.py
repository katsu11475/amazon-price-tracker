import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.jp/%E4%BC%8A%E8%97%A4%E5%9C%92-%E3%83%A9%E3%83%99%E3%83%AB%E3%83%AC%E3%82%B9-%E3%81%8A%E3%83%BC%E3%81%84%E3%81%8A%E8%8C%B6-460ml%C3%9730%E6%9C%AC-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%9C%E3%83%88%E3%83%AB/dp/B0C654Z5PC/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1WDGN311MD7D0&keywords=%E6%BF%83%E3%81%84%E3%81%8A%E8%8C%B6%2B%E3%81%8A%E3%83%BC%E3%81%84%E3%81%8A%E8%8C%B6&qid=1699554345&sprefix=%E6%BF%83%E3%81%84%2B%E3%81%8A%E3%83%BC%E3%81%84%E3%81%8A%E8%8C%B6%2Caps%2C205&sr=8-5&th=1"

def amazon_tracking_price():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup)

    title = soup.find(id = "productTitle").get_text()
    #print(title)
    
    price = soup.find("span", class_ ="a-size-base").get_text()
    #print(price)
    
    priceLen = int(len(price)/2)
    #print(priceLen)
    
    convertedPrice = int(price[1:priceLen].replace(",", ""))
    print(convertedPrice)
    
def 
    
        
amazon_tracking_price()