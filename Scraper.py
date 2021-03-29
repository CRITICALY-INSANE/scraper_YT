#Youtube scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import requests
from threading import Thread as tt
from bs4 import BeautifulSoup

 
driver =webdriver.Chrome('C:/Project OverLoad/Automation/chromedriver.exe')
driver.get('https://www.youtube.com/')
x=input("enter the link = ")

resp=requests.get(x)
soup = BeautifulSoup(resp.content, 'html.parser')

def anchor():
    for link in soup.find_all('a'):
        print(link.get('href'))


if resp.status_code==200:
    
    print('valid link')
    anchor()
    #print(resp.content)
    #print(soup.prettify())
    
elif resp.status_code==404:
    pass
    #repeat
else:
    
    print('invalid link')
    
