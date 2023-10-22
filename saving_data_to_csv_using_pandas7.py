import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
respones = requests.get(url)
soup = BeautifulSoup(respones.text,"lxml")

country = soup.find_all("div",class_ = "col-md-4 country")
country_name = []
country_capital = []
country_population = []
country_area = []

for i in country:
    name = i.find("h3",class_ = "country-name")
    country_name.append(name.text.strip())

    capital = i.find("span",class_ = "country-capital")
    country_capital.append(capital.text)

    population = i.find("span",class_ = "country-population")
    country_population.append(float(population.text))

    area = i.find("span",class_ = "country-area")
    country_area.append(float(area.text))

df = pd.DataFrame({"country name":country_name,
                   "country_capital":country_capital,
                   "country_population":country_population,
                   "country_area":country_area})

df.to_excel("country_data_scraped.xlsx")