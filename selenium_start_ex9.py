from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

"""put any video's url you want to extract description and title of"""
url = "https://youtu.be/dQw4w9WgXcQ?si=Xo4gqNCSccsHVpJX"

option = webdriver.ChromeOptions()
option.add_argument('--headless')


s = Service("C:/Users/Hamza/Documents/web_scraping/chromedriver.exe")
driver = webdriver.Chrome(service= s,options=option)
driver.get(url)

driver.find_element(By.XPATH, """/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]""").click()
des = driver.find_element(By.XPATH,"""/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander""")
dis = des.find_element(By.XPATH,"""/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/yt-attributed-string""")

for_title = driver.find_element(By.XPATH,"""/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1""")

title = for_title.text
description = dis.text


info = [title,description]
for i in info:
    print(i)

