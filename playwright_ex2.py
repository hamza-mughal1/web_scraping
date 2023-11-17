from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context(locale="en-US")
    page = context.new_page()
    page.goto("https://www.fotmob.com/matches/liverpool-vs-everton/2hagld#4193544")
    soup = BeautifulSoup(page.content(),"lxml")
    browser.close()
    element = soup.find("ul",class_ = "css-wmbkk6-BenchContainer elhbny510")
    print(element.get_text())
    