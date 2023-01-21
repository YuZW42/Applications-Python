from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, url_for, request
app = Flask(__name__)



@app.route('/')
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

    return render_template("index.html", news=news)


if __name__ == "__main__":
    app.run(debug=True)
