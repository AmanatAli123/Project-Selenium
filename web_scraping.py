from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome()
query="laptop"
quote_list=[]

for i in range(1,20):
    driver.get(f"https://www.daraz.pk/catalog/?q={query}&page={i}")
    search_box = driver.find_elements(By.CLASS_NAME, "Bm3ON")
    for p in search_box:
        quote={}
        quote['product']=p.text
        inner_img=p.find_element(By.TAG_NAME,"img")
        inner_a=p.find_element(By.TAG_NAME,"a")
        quote['image']=inner_img.get_attribute("src")
        quote['title']=inner_a.get_attribute("alt")
        quote['link']=inner_a.get_attribute("href")
        quote_list.append(quote)

        filename=f"listname.csv"
        with open(filename,'w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=['product','image','title','link'])
            w.writeheader()
            w.writerows(quote_list)
            for quote in quote_list:
                w.writerow(quote)

    
    time.sleep(2)

driver.quit()