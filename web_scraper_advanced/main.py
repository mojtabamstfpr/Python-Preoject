import requests
from bs4 import BeautifulSoup
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("a", class_="titlelink")
for article in articles:
    print(article.text, "-", article['href'])