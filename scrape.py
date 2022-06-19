from bs4 import BeautifulSoup
import requests
from csv import writer 

url = "https://www.pararius.com/apartments/amsterdam?ac=1"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

sectionList = soup.findAll('section', class_= "listing-search-item")

with open('housing.csv', 'w', encoding='utf8',newline='') as f:
    writerControl = writer(f)
    header= ['Title','Location', 'Price', 'SurfaceArea']
    writerControl.writerow(header)      

    for section in sectionList:
        title = section.find('a', class_="listing-search-item__link--title").text.replace('\n','')
        location = section.find('div', class_="listing-search-item__location").text.replace('\n','')
        price = section.find('span', class_="listing-search-item__price").text.replace('\n','')
        surfaceArea = section.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
        info= [title, location, price, surfaceArea]
        writerControl.writerow(info)  
  
    