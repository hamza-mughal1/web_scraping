"""importing modules"""

import requests
from bs4 import BeautifulSoup


"""defing function to fatch data from single div at a time"""
def foo(main_div,spec_count = False,specific = []):
    """args : {main div : div which have to fetch data from}"""

    """variables : {info div : descriptive information from 'main_div',
    title : name of the (div or title) aka country name,
    all_name : list of keys of all descriptive information,
    all_value : list of values of all descriptive information}"""

    info_div = main_div.find("div",{"class":"country-info"})
    title = main_div.h3.text

    if spec_count:
        t = title.strip()
        if  t in specific:
            print(f"country: {title.strip()}")

            all_name = info_div.find_all("strong")
            all_value = info_div.find_all("span")

            for i in range(len(all_name)):
                print(all_name[i].text,all_value[i].text)
            
            return True
        else:
            return False
            
    else:
        print(f"country: {title.strip()}")

        all_name = info_div.find_all("strong")
        all_value = info_div.find_all("span")

        for i in range(len(all_name)):
            print(all_name[i].text,all_value[i].text)
        
        return True

"""checking if file is directly called"""

if __name__ == "__main__":

    """seting up soup"""

    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"lxml")

    """fetching data from single div"""

    # main_div = soup.find("div",{"class":"col-md-4 country"})
    # info_div = main_div.find("div",{"class":"country-info"})

    # title = main_div.h3.text
    # print(title.strip())

    # capital_name = info_div.find("strong")
    # capital_value = info_div.find("span",{"class":"country-capital"})

    # population_name = info_div.find("strong")
    # population_value = info_div.find("span",{"class":"country-population"})

    # area_name = info_div.find("strong")
    # area_value = info_div.find("span",{"class":"country-area"})

    # print(capital_name.text,capital_value.text)
    # print(population_name.text,population_value.text)
    # print(area_name.text,area_value.text)

    # all_name = info_div.find_all("strong")
    # all_value = info_div.find_all("span")

    # for i in range(len(all_name)):
    #     print(all_name[i].text,all_value[i].text)


    """fetching data from mutiple divs"""

    """variables : {specific_country : if you want data of some specific countries,
    div_lis : list of all divs from data is to fetch}"""

    specific_country = ["Pakistan","India","Israel","Palestine","United States"]
    div_lis = soup.find_all("div",{"class":"col-md-4 country"})
    print(len(div_lis),"\n")

    for pos,i in enumerate(div_lis):
        res = foo(i,spec_count=True,specific=specific_country)
        if res:
            print("\n")

