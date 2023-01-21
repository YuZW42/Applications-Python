#this stores various news scrap methods 
from bs4 import BeautifulSoup
import requests

def result():
    url = "https://www.businesstoday.in/latest/economy"
    news = []
    webpage = requests.get(url)
    trav = BeautifulSoup(webpage.content, "html.parser")
    M = 1
    for link in trav.find_all('a'):
        if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
           and len(link.string.strip()) > 35):
            print(link.string)
            
            news.append(link.string)
            M += 1
    return news
def bbc_scraper():
  headers={'User-agent':'Mozilla/5.0'}
  request = requests.get('https://www.bbc.com/news/business', headers=headers)
  html = request.content
  
  soup = BeautifulSoup(html,'html.parser')
  news = []
  for h3 in soup.findAll('h3',class_='gs-c-promo-heading__title'):
      news_title = h3.contents[0].lower()
      if news_title not in news:
          if 'bbc' not in news_title:
              news.append(news_title)
  print(news)
  return news

print(bbc_scraper())