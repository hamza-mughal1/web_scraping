import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def selenium_to_load_full_page(url):
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')

    s = Service("C:/Users/Hamza/Documents/web_scraping/chromedriver.exe")
    driver = webdriver.Chrome(service= s,options=option)
    driver.get(url)
    older = driver.execute_script("return document.body.scrollHeight")
    while True:
        time.sleep(1)
        old_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        new_height = driver.execute_script("return document.body.scrollHeight")
        if (old_height == new_height) and (older == new_height):
            return driver.page_source
        older = old_height
        
def list_of_products(url):
    lis = []
    response = selenium_to_load_full_page(url)
    soup = BeautifulSoup(response,"lxml")
    div = soup.find("div",id="search_resultsRows")
    products = div.find_all("a",class_ = "search_result_row ds_collapse_flag")
    print("lenght = ",len(products))

    for i in products:
        lis.append(i.get("href"))
    return lis

def extract_data_of_game(product_url):
    title = ""
    genre = ""
    release_date = ""
    developer = ""
    publisher = ""
    franchise = ""
    website = ""
    twitter = ""
    youtube = ""
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text,"lxml")

    details_div = soup.find("div",class_ = "block_content_inner")
    top = details_div.find("div",id="genresAndManufacturer",class_ = "details_block")
    bottom = details_div.find("div",class_ = "details_block",style="padding-top: 14px;")

    

    detail_text = top.text.split("\n")
    for i in detail_text:
        if "Title: " in i:
            title = i.replace("Title: ","")
        elif "Genre: " in i:
            genre = i.replace("Genre: ","")
        elif "Release Date: " in i:
            release_date = i.replace("Release Date: ","")

    
    dev_Row = details_div.find_all("div",class_ = "dev_row")
    for i in dev_Row:
        if i.find("b").text == "Developer:":
            developer = i.find("a").text
        elif i.find("b").text == "Publisher:":
            publisher = i.find("a").text
        elif i.find("b").text == "Franchise:":
            franchise = i.find("a").text
    
    

    links = bottom.find_all("a")

    for i in links:
        t = i.text
        if "website" in i.text:
            website = i.get("href")
        elif "Twitter" in i.text:
            twitter = i.get("href")
        elif "YouTube" in i.text:
            youtube = i.get("href")

    return title,genre,developer,publisher,franchise,release_date,website,twitter,youtube

def main(url,titles,genre,developers,publishers,franchises,release_dates,websites,twitter,youtube,links):
    products = list_of_products(url)

    for pos,i in enumerate(products):
        print(pos)
        extract = extract_data_of_game(i)
        titles.append(extract[0])
        genre.append(extract[1])
        developers.append(extract[2])
        publishers.append(extract[3])
        franchises.append(extract[4])
        release_dates.append(extract[5])
        websites.append(extract[6])
        twitter.append(extract[7])
        youtube.append(extract[8])
    
    links[:] = products

if __name__ == "__main__":
    url = "https://store.steampowered.com/search/?filter=popularcomingsoon&ndl=1"
    titles = []
    genre = []
    developers = []
    publishers = []
    franchises = []
    release_dates = []
    websites = []
    twitter = []
    youtube = []
    links = []

    main(url,titles,genre,developers,publishers,franchises,release_dates,websites,twitter,youtube,links)
    print(len(titles),len(genre),len(developers),len(publishers),len(franchises),len(release_dates),len(websites),len(twitter),len(youtube),len(links))

    df = pd.DataFrame({"titles":titles,
                       "genre":genre,
                       "developers":developers,
                       "publishers":publishers,
                       "franchise":franchises,
                       "release_dates":release_dates,
                       "websites":websites,
                       "twitter":twitter,
                       "youtube":youtube,
                       "links":links})
    
    df.to_excel("steam_upcoming_games.xlsx")

    