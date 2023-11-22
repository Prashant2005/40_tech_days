#simple program to scrape content using beautifulsoup and requests



import requests
from bs4 import BeautifulSoup
url=input("Enter url: ")
r=requests.get(url)
contents=r.content
soup=BeautifulSoup(contents, 'html.parser')

print(soup.find('body').text) 
