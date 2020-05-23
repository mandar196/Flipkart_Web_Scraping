# -*- coding: utf-8 -*-
"""
Created on Sat May 23 08:45:27 2020

@author: Acer
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\Acer\\OneDrive\\Desktop\\BHP\\chromedriver.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('C:\\Users\\Acer\\OneDrive\\Desktop\\BHP\\products.csv', index=False, encoding='utf-8')