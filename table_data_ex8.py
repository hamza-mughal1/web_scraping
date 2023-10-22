import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_Data_from_Table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")

    table = soup.find("table",class_ = "table")
    tb_headers = table.find_all("th")
    headers = [i.text.strip() for i in tb_headers]
    tb_teams = [[i.text.strip() for pos,i in enumerate(j) if (pos+1)%2==0] for j in table.find_all("tr",class_ = "team")]

    Team_name = []
    Year = []
    Wins = []
    Losses = []
    OT_Losses = []
    Win_ = []
    Goals_For_GF = []
    Goals_Against_GA_ = []
    plus_or_minus = []

    for i in tb_teams:
        Team_name.append(i[0])
        Year.append(i[1])
        Wins.append(i[2])
        Losses.append(i[3])
        OT_Losses.append(i[4])
        Win_.append(i[5])
        Goals_For_GF.append(i[6])
        Goals_Against_GA_.append(i[7])
        plus_or_minus.append(i[8])



    df = pd.DataFrame({headers[0]:Team_name,
                    headers[1]:Year,
                    headers[2]:Wins,
                    headers[3]:Losses,
                    headers[4]:OT_Losses,
                    headers[5]:Win_,
                    headers[6]:Goals_For_GF,
                    headers[7]:Goals_Against_GA_,
                    headers[8]:plus_or_minus})

    return df

df1 = extract_Data_from_Table("https://www.scrapethissite.com/pages/forms/?page_num=1")

for i in range(2,25):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    df2 = extract_Data_from_Table(url)
    df1 = df1._append(df2)

l = [i for i in range(len(df1))]
df1.insert(0,"idx",l,True)
df1.to_csv("table_Data.csv",index=False)
df1.to_excel("table_Data.xlsx",index=False)
