from bs4 import BeautifulSoup
import requests

responce = requests.get("https://news.ycombinator.com/")
yc_web_page = responce.text


soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="span", class_="titleline")
print(article_tag.get("href"))
