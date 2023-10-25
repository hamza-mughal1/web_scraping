"""         ** EXPLAINATION OF THIS PROGRAM **

    Q: What does this program do?

    A: This program scrapes data from the website "daraz.pk" and saves it to an Excel file.

    Q: How does it do it?

    A: 1. Opens Chrome using the ChromeDriver.
    2. Goes to "daraz.pk" to scrape data.
    3. Searches for the prompt that the user wants data for.
    4. Extracts each product object from the web page into a list.
    5. Extracts the information required by the user from each element of the list.
    6. Loops through this extraction for the pages that the user wants to scrape data from.
    7. Loads the data into a Pandas DataFrame.
    8. Saves the Pandas DataFrame to an Excel file.

"""



"""importing modules"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

"""     defining function   """

"""(text to num) extracts numbers from string and converts it into integer"""
def text_to_num(text):
    """checks if the element of (text) is a number then append it to a variable then converts into integer"""
    
    n = "0123456789"
    result = ""
    for i in text:
        if i in n:
            result += i
    return int(result)

"""(func) checks if the element is present on page, if it is then return it. if not then returns (None)"""
def func(name,function,element):
    """func is useful to check if something like 'discount' or 'rating' is available on page,
    so if not then don't raise an error. except return None and continue to next"""

    try:
        if function == 0:    
            result = name.find_element(*element)
            return result
        elif function == 1:
            result = name.find_elements(*element)
            return result
    except:
            return None

"""(main) extracts data from single page at once, when it gets called"""
def main(title,price,original_price,discount_percent,rating_no,link):
    """(main) is useful to to extract data from one page then move it to next then call this function again.
    this way it avoids errors and complexity"""

    """it takes a list of all products div or object as 'd', then by looping in all the elements of list
    it extracts information of each product from div or object"""

    d = func(driver,1,(By.CSS_SELECTOR, "div[class='gridItem--Yd0sa'][data-qa-locator='product-item'][data-tracking='product-card']"))
    for i in d:
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
            price.append(text_to_num(px.text))

        dx = func(i,0,(By.CSS_SELECTOR,"div[class='priceExtra--ocAYk']"))
        dx2 = func(dx,0,(By.CSS_SELECTOR,"span[class='origPrice--AJxRs']"))
        dx3 = func(dx2,0,(By.CSS_SELECTOR,"del[class='currency--GVKjl']"))
        if dx3 == None:
            original_price.append(text_to_num(px.text))
        else:
            original_price.append(text_to_num(dx3.text))
        dx4 = func(dx,0,(By.CSS_SELECTOR,"span[class='discount--HADrg']"))
        if dx4 == None:
            discount_percent.append(0)
        else:
            discount_percent.append((text_to_num(dx4.text))/100)

        rx = func(i,0,(By.CSS_SELECTOR,"div[class='rateAndLoc--XWchq']"))
        rx2 = func(rx,0,(By.CSS_SELECTOR,"div[class='rating--ZI3Ol rate--DCc4j']"))
        rx4 = func(rx2,0,(By.CSS_SELECTOR,"span[class='rating__review--ygkUy']"))
        if rx4 == None:
            rating_no.append(0)
        else:
            rating_no.append(text_to_num(rx4.text))

"""     starting scraping and saving it into file    """

if __name__ == "__main__":

    """url of website"""
    url = "https://www.daraz.pk"

    """ 'option' is used to run chrome in (headless or CLI) mode"""
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')

    """initializing the chrome driver"""
    s = Service("C:/Users/Hamza/Documents/web_scraping/chromedriver.exe")
    driver = webdriver.Chrome(service= s)
    driver.get(url)
    driver.minimize_window()

    """finding the search bar and passing user's prompt into it"""
    search = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[1]/input[1]")
    
    print("\n\t**if you get any error related to element not found or not clickable at that moment or such, try increasing wait time!\n")
    
    wait_time = input("enter time to wait to load every page (put large number if your pc is slow - mostly 3 seconds are ok) in seconds : ")
    key_word = input("enter the prompt : ")
    number_of_pages = input("enter a number for how many pages to scrap : ")
    
    search.send_keys(key_word)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[2]/button").click()
    
    """defining global variables"""
    title = []
    price = []
    original_price = []
    discount_percent = []
    rating_no = []
    link = []

    """starting loop numbers of times that how many pages user wants to scrap data from. 
    each loop for each page"""
    for i in range(int(number_of_pages)):
        main(title,price,original_price,discount_percent,rating_no,link)

        """checking if loop is on last page then stop moving to next page"""
        if i != int(number_of_pages)-1:
            driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div[1]/div[3]/div/div/ul/li[9]/a").click()
            time.sleep(int(wait_time))


    """creating 'pandas' dataframe to save data into file"""
    df = pd.DataFrame({"Title":title,
                    "price":price,
                    "original price":original_price,
                    "discount percentage":discount_percent,
                    "rating numbers":rating_no,
                    "link":link})
    
    """saving data into 'excel' file. And saving it's name using 'daraz_' and then (user's prompt)
    but changing spaces ' ' to underscore '_' so that file will save without an error"""
    df.to_excel(f"daraz_{key_word.replace(' ','_')}.xlsx")