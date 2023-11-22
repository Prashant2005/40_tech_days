#Using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
driver=webdriver.Chrome()
url=input("Enter url: ")
driver.get(url)
get_res=driver.find_element(By.TAG_NAME, 'body')

print(get_res.text)
