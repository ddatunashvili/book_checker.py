import random
import time
import unidecode
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  csv
# prefer
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
PATH=r'/home/davit/Desktop/book_influence.py/chromedriver'
driver = webdriver.Chrome(executable_path=PATH,chrome_options=chrome_options)



driver.get("https://reversedictionary.org/wordsfor/science%20fiction")

words=[]
# top 60  
top = 300

for i in driver.find_elements_by_class_name('item'):
    words.append(i.text)
    if top > 0:
        top-=1  
    else:
        break    
 
translated = []
# top 60  
top = 0
for word in words:     
        try:
            driver.get('https://any.ge/translate/')
            driver.find_element_by_name('text').send_keys(word)
            driver.find_element_by_id('targmna').click()
            time.sleep(1)
            if driver.find_element_by_css_selector("div[submit-success]").text in translated:
                pass
            if len(driver.find_element_by_css_selector("div[submit-success]").text) > 2:
                translated.append(driver.find_element_by_css_selector("div[submit-success]").text)
                if top < 100:
                    top+=1
                else:
                    break
                # driver.close()
            else:
                pass
        except:
            pass




# importing pandas as pd  
import pandas as pd  
       
df = pd.DataFrame() 
df['scienceFilter'] = translated
    
# saving the dataframe 
df.to_csv('/home/davit/Desktop/book_influence.py/filter.csv',index = False) 







