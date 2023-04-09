from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import urllib.request as req
import bs4
from modeles import dictionary1 as dic
import json

options = Options()
options.add_argument('log-level=3')
options.chrome_executable_path =r'C:\Users\user\Desktop\py_training\chromedriver.exe'
driver=webdriver.Chrome(options=options)

url='https://englishprofile.org/wordlists/evp'
driver.get(url)
dictionary={}

for p in range(20):
    links=(driver.find_elements(By.LINK_TEXT,'Details'))
    links[p].click()
    try:
        word=driver.find_element(By.CLASS_NAME,'headword')
        defi=driver.find_element(By.CLASS_NAME,'definition')
        KK=driver.find_element(By.CLASS_NAME,'written')
        dictionary.setdefault(word.text,[defi.text,KK.text])
        backlink=driver.find_element(By.LINK_TEXT,'Back to Report')
        backlink.click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(0.1)
    except Exception:
        backlink=driver.find_element(By.LINK_TEXT,'Back to Report')
        backlink.click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(0.1)
        continue
for j in range(780):
    try:
        nextpage=driver.find_element(By.LINK_TEXT,'Next')
        nextpage.click()
        for i in range(20):
            links=(driver.find_elements(By.LINK_TEXT,'Details'))
            links[i].click()
            try:
                word=driver.find_element(By.CLASS_NAME,'headword')
                defi=driver.find_element(By.CLASS_NAME,'definition')
                KK=driver.find_element(By.CLASS_NAME,'written')
                dictionary.setdefault(word.text,[defi.text,KK.text])
                backlink=driver.find_element(By.LINK_TEXT,'Back to Report')
                backlink.click()
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(0.1)
            except Exception:
                backlink=driver.find_element(By.LINK_TEXT,'Back to Report')
                backlink.click()
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(0.1)
                continue
    except Exception:
        print(i,j,'錯誤')
        break  
driver.close()
print(len(dictionary))
with open("diction.json",mode="w") as file:
     json.dump(dictionary, file)

