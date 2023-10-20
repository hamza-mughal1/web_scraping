import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

info = soup.strong.text
print(info)