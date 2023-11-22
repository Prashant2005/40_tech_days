#simple program to scrape content using beautifulsoup and requests

url=input("Enter url: ")

import requests
from bs4 import BeautifulSoup

r=requests.get(url)
contents=r.content
soup=BeautifulSoup(contents, 'html.parser')

print(soup.find('body').text) 
