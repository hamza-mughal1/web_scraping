from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def func(name,function,element):
        try:
            if function == 0:    
                result = name.find_element(*element)
                return result
            elif function == 1:
                result = name.find_elements(*element)
                return result
        except:
             return None


url = "https://www.daraz.pk/catalog/?spm=a2a0e.home.search.1.35e340761IDnMC&q=gaming%20pc&_keyori=ss&from=search_history&sugg=gaming%20pc_0_1"

option = webdriver.ChromeOptions()
option.add_argument('--headless')


s = Service("C:/Users/Hamza/Documents/web_scraping/chromedriver.exe")
driver = webdriver.Chrome(service= s)
driver.get(url)


d = func(driver,1,(By.CSS_SELECTOR, "div[class='gridItem--Yd0sa'][data-qa-locator='product-item'][data-tracking='product-card']"))


title = []
price = []
discount = []
stars = []
rating_no = []
link = []
for i in d:
    lis = []
    tx = func(i,0,(By.CSS_SELECTOR,"div[class='title--wFj93']"))
    if tx == None:
        title.append(None)  
    else:   
        title.append(tx.text)
    a = func(tx,0,(By.CSS_SELECTOR,"a"))
    if a == None:
        link.append(None)
    else:
        link.append(a.get_attribute("href"))
    px = func(i,0,(By.CSS_SELECTOR,"div[class='price--NVB62']"))
    if px == None:
        price.append(None)
    else:
        price.append(px.text)

    dx = func(i,0,(By.CSS_SELECTOR,"div[class='priceExtra--ocAYk']"))
    dx2 = func(dx,0,(By.CSS_SELECTOR,"span[class='origPrice--AJxRs']"))
    dx3 = func(dx2,0,(By.CSS_SELECTOR,"del[class='currency--GVKjl']"))
    if dx3 == None:
        lis.append(None)
    else:
        lis.append(dx3.text)
    dx4 = func(dx,0,(By.CSS_SELECTOR,"span[class='discount--HADrg']"))
    if dx4 == None:
        lis.append(None)
    else:
        lis.append(dx4.text)
    discount.append(lis)

    rx = func(i,0,(By.CSS_SELECTOR,"div[class='rateAndLoc--XWchq']"))
    rx2 = func(rx,0,(By.CSS_SELECTOR,"div[class='rating--ZI3Ol rate--DCc4j']"))
    rx3 = func(rx2,1,(By.CSS_SELECTOR,"span"))
    rx4 = func(rx2,0,(By.CSS_SELECTOR,"span[class='rating__review--ygkUy']"))
    if rx4 == None:
        rating_no.append(None)
    else:
        rating_no.append(rx4.text)
    if rx3 == None:
        stars.append(None)
    else:
        stars.append(len(rx3)-1)


df = pd.DataFrame({"Title":title,
                   "price":price,
                   "discount":discount,
                   "stars":stars,
                   "rating numbers":rating_no,
                   "link":link})


df.to_excel("daraz_data.xlsx")