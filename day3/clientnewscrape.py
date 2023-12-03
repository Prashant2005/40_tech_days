import requests
import re
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
wb = Workbook()
# url="https://www.yep.co.za/search?category=81522"
# r=requests.get(url)
# htmlContent=r.content
# # print(htmlContent)
# soup=BeautifulSoup(htmlContent, 'html.parser')

# urls=[]
# divcoll=soup.find_all('div', class_='serviceResultCard_service_result_card__vdO1S')
# for i in divcoll:
#     a=i.find('a')
#     try:
#         if 'href' in a.attrs:
#             url='https://www.yep.co.za'+str(a.get('href'))
#             urls.append(url)
#     except:
#         pass
# print(urls)
def get_links(url):
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    urls=[]
    divcoll=soup.find_all('div', class_='serviceResultCard_service_result_card__vdO1S')
    for i in divcoll:
        a=i.find('a')
        try:
            if 'href' in a.attrs:
                url='https://www.yep.co.za'+str(a.get('href'))
                urls.append(url)
        except:
            pass
    return urls
def get_content(urls):
    r=requests.get(urls)
    pagecontent=r.content
    soup=BeautifulSoup(pagecontent, 'html.parser')
    details=[]
    divcoll=soup.find_all('div', class_='Header_sf_info__ymMGk')
    for i in divcoll:
        a=i.find('h2')
        b=i.find('p')
        c=i.find('a')
        d=soup.find_all('a')
        
        try:
            text=a.get_text()
            # descrip=b.get_text()
            # weburl=c.get('href')
            # i.get('title')
            # email=re.findall('\S+@\S+', d)
            details.append(text)
            # details.append(descrip)
            # details.append(weburl)
            # # details.append(email)

        except:
            details.append(" ")
        try:
            descrip=b.get_text()
            details.append(descrip)
        except:
            details.append(" ")
        try:
            weburl=c.get('href')
            details.append(weburl)
        except:
            details.append(" ")
        try:
            xy=set()
            
            
            for ap in d:
                xy.add(ap)

            
            match = re.findall(r'[\w\.-]+@[\w\.-]+', str(xy))
            email=match[0]
            
            details.append(email)
        except:
            details.append(" ")
    return details
    # paras1=soup.find('font')
    # # title=paras1.get_text()
    # return soup
count=1
def whichpage(num):
    prep=[]
    global count
    if num==1:
        url='https://www.yep.co.za/search?category=81522'
    else:
        url='https://www.yep.co.za/search?category=81522&pageNumber='+str(num)
    x=get_links(url)
    a=0
    for con1 in x:
        content=get_content(con1)
        prep.append(content)
    return prep
sheet1=wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
style = xlwt.easyxf('font: bold 1')
b=1
def excel(items):
    global b
    sheet1.write(0, 1, 'Serial No.', style)
    sheet1.write(0, 2, 'Name', style)
    sheet1.write(0, 3,'Address', style)
    sheet1.write(0, 4, 'Website', style)
    sheet1.write(0, 5, 'Email', style)
    for i in items:
        
        sheet1.write(b, 1, b)
        sheet1.write(b, 2, i[0])
        
        sheet1.write(b, 3, i[1])
        
        sheet1.write(b, 4, i[2])
        
        sheet1.write(b, 5, i[3])
        b+=1
# x=get_links('https://www.yep.co.za/search?category=81522')
# y=get_content(x[0])
# xy=set()
# for i in y:
#     xy.add(i)
#     # print(y, len(y),sep="\n\n\n\n")
    
# match=re.findall(r'[\w\.-]+@[\w\.-]+', str(xy))
# for i in range(1, 745):
#     do=whichpage(i)
#     excel(do)
# wb.save('clientfile.xls')

for i in range(1, 745): #scrapping 251-500 out of 744
    do=whichpage(i)
    excel(do)
    print("PageScrapped:", i,"\n")
wb.save('clientfilefinal.xls')
