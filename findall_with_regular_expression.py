import requests
from bs4 import BeautifulSoup
import regex as re


url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

title = soup.find_all(class_ = re.compile("country-capital"))

for i in title:
    print(i.string)