import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
wb = Workbook()

url1='https://www.***.org.za/register_of_registrants/registered_cp.php'
# url2=''
# url=url1+url2
# fetchAndSaveToFile(url, "data/fetched.html")
def get_content(url2):
    
    url=url1+url2

    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    paras=soup.find_all('td')
    return paras

def func(value):
    return ''.join(value.splitlines())
def create_list(fullname, tradename, phone, fax, finalregdate, ncrreg, legalreg, address, town, status):
    tem_list1=[fullname, tradename, phone, fax, finalregdate, ncrreg, legalreg, address, town, status]
    # credit_providers.append(tem_list1)
    return 'done'


# a=0
def fetch_contents(num):
    credit_providers=[]
    if num==1:
        url2=""
    else:
        url2="?page="+str(num)
    paras02=get_content(url2)
    # print(paras02)
    sep_list=[]
    for text in paras02:
        text_01=text.get_text().strip()
        credit_providers.append(func(text_01))
    credit_providers.pop(0)
    credit_providers.pop(0)
    for i in range(10):
        credit_providers.pop(0)
        credit_providers.pop(1)
        credit_providers.pop(2)
        credit_providers.pop(3)
        credit_providers.pop(4)
        credit_providers.pop(5)
        credit_providers.pop(5)
        credit_providers.pop(5)
        credit_providers.pop(5)
        credit_providers.pop(5)
        credit_providers.pop(6)
        credit_providers.pop(7)
        credit_providers.pop(8)
        credit_providers.pop(9)
        sep_list.append(credit_providers[:10])
        del credit_providers[:10]
    return sep_list

def prep_sep(item):
    lst_to_return=item
    for i in range(10):
        unwanted = [0, 2, 4, 6, 8, 10, 11, 12, 13, 15, 17, 18, 20]
        for ele in sorted(unwanted, reverse = True):
            del lst_to_return[ele]

    return lst_to_return
b=1
sheet1=wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
style = xlwt.easyxf('font: bold 1')
def excel_sheet(items, num):
    global b
    
    sheet1.write(0, 1, 'Serial No.', style)
    sheet1.write(0, 2, 'Full Name', style)
    sheet1.write(0, 3,'Trading Name', style)
    sheet1.write(0, 4, 'Phone', style)
    sheet1.write(0, 5, 'Fax', style)
    sheet1.write(0, 6, 'Final Registration Date', style)
    sheet1.write(0, 7, 'NCR Registration No.', style)
    sheet1.write(0, 8, 'Legal Registration No.', style)
    sheet1.write(0, 9, 'Physical Address', style)
    sheet1.write(0, 10, 'Town', style)
    sheet1.write(0, 11, 'Status', style)
    a=b
    c=0
    for i in items:
        sheet1.write(a, 1, b)
        sheet1.write(a, 2, i[0])
        c+=1
        sheet1.write(a, 3, i[1])
        c+=1
        sheet1.write(a, 4, i[2])
        c+=1
        sheet1.write(a, 5, i[3])
        c+=1
        sheet1.write(a, 6, i[4])
        c+=1
        sheet1.write(a, 7, i[5])
        c+=1
        sheet1.write(a, 8, i[6])
        c+=1
        sheet1.write(a, 9, i[7])
        c+=1
        sheet1.write(a, 10, i[8])
        c+=1
        sheet1.write(a, 11, i[9])
        c+=1
        b+=1
        a+=1
    
    




# x=fetch_contents(1)
# excel_sheet(x, 1)
for i in range(1, 689):
    x=fetch_contents(i)
    excel_sheet(x, i)
wb.save('credit provider.xls')
