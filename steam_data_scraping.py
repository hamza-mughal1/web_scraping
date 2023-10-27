"""
    q) what this program does?
    
    a) this program takes all upcoming games info like 
    (name,genre,studio,developer,publisher,franchise,release date,twitter,youtube,game link) 
    on steam and save it into an excel file.
    
    q) how this program works?
    
    a) this program first opens upcoming list page of steam in selenium
    then loads whole page by scrolling to bottom
    then passes the html of web page to beautiful soup
    then beautiful soup opens every game on that list
    then beautiful soup scraps data from games
    then by pandas creates a framework 
    then saves framework into excel file
"""


"""importing modules"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

"""defing functions"""
def selenium_to_load_full_page(url):
    """
    this function opens web page into selenium then loads it and returns html
    """

    """
    option makes selenium to open chrome in headless mode or CLI mode
    """
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')

    """creating chrome driver and opening web page using selenium"""
    s = Service("C:/Users/Hamza/Documents/web_scraping/chromedriver.exe")
    driver = webdriver.Chrome(service= s,options=option)
    driver.get(url)

    """checking if we are at bottom of the page by scrolling in loop"""
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
    """
    this function takes a url and pass into 'selenium_to_load_full_page' function
    which gives html and from that html it extracts each game div into a list and returns that list 'lis'
    """
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
    """this function takes game's link once at a time then extracts data from that game and returns it"""
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
    """this function does combining work for all functions
    first it calls 'list_of_products' function which returns list then by looping that list it calls 
    extract_data_of_game which returns data of game then it appends that data into different lists"""
    products = list_of_products(url)

    for i in enumerate(products):
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

"""strating main"""
if __name__ == "__main__":
    """defining url of web page and global variables"""
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

    """calling 'main' function which will append data into lists which are passing as arguments"""
    main(url,titles,genre,developers,publishers,franchises,release_dates,websites,twitter,youtube,links)

    """creating pandas data frame"""
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
    
    """saving dataframe into excel file"""
    df.to_excel("steam_upcoming_games.xlsx")

    