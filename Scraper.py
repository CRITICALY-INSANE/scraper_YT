#Youtube scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import requests
from threading import Thread as tt
from bs4 import BeautifulSoup
import re

x=""
 
driver =webdriver.Chrome('C:/Project OverLoad/Automation/chromedriver.exe')
driver.get('https://www.youtube.com/')
def strt():
    global resp
    x=(input("enter the link = ")).strip()
    if (x!=None) and (x!=""):
        driver.get(x)
        resp=requests.get(x)
        if (len(driver.window_handles)>1):
            window_name = driver.window_handles[0]
            driver.switch_to.window(window_name=window_name)
            driver.close()
        
    else:
        print("Empty link \n Try again ")
        x=input("Enter the Link = ")
        try:
            driver.get(x)
            resp=requests.get(x)
            window_name = driver.window_handles[0]
            driver.switch_to.window(window_name=window_name)
            driver.close()
        except (Exception):
            pass
    if resp.status_code==200:
        
        #print('valid link')
        
        #driver.get(x)
        time.sleep(4)    
        window_name = driver.window_handles[0]
        driver.switch_to.window(window_name=window_name)
        driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
        anchor()
        #print(resp.content)
        #print(soup.prettify())
        
    elif resp.status_code==404:
        pass
        #repeat
    else:
        print('invalid link')
    

def get_info(big, small):
    return (big.count(small))

def anchor():
    #resp=requests.get(x)
    try:
            players = driver.find_element_by_id('contents')
            #print(players.get_attribute('innerHTML'))
            big_str=players.get_attribute('innerHTML')
            sub_space='<a id="endpoint-link" class="yt-simple-endpoint style-scope ytd-rich-metadata-renderer" href='
            itr=get_info(big_str,sub_space)
            #print('The number of Contents Present are '+str(itr))
            wrk_str=str(big_str)
            for i in range(0,itr-1):
                  w=""
                  k=((re.search(r'\b(href)\b', wrk_str)))
                  ind=k.start()+5
                  i=0
                  #print(str(wrk_str(ind+4)))
                  while True:
                      if((wrk_str[ind]) !='>' ):
                          w+=wrk_str[ind]
                          ind+=1
                      else:
                          print(w.strip())
                          wrk_str=wrk_str[ind:]
                          x=""
                          print()
                          break
            strt()
                
    except Exception as e:
        print(str(e))
        print('No Contents Found on This Page')

    
strt()

