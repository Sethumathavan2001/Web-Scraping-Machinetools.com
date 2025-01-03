import requests
burl = "https://www.machinetools.com"
url = burl+"/en/machinery"

from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
# url = "your_target_url_here"
# url = "https://www.amazon.in/dp/B09GSC45FS"
h={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
# 'Cookie': 'breakpoint=xlarge; _machinetools.com=m3ge1QYPDhgSkOJWza09pXY7eoR5GvZZUKiO6MgJKKm1w%2Bz2CH%2FE2HgcCLnU8dnj7IeQk24DhvFIB86VxlKp5APNJJ937oIXdfaLtn6cvEWKDViRG%2Fd03m%2BXOCMed0jH6W7%2BEt8u%2FC0ZF1y7sR7m2OgNgUoVlWU9n48NJc%2FpnIpKXVfruDbe0Gi9Bnsrevq1OxTnAVAjeDChzuazQSkdSDIgxFRdxh45m08apVptXdlWIRYmXzZyF%2F2eEF1hNzQay6TzoZqRI4883twz76Lr3TUYXDHP8NPUSw%3D%3D--So0UBUfoRUsXhT8O--sw6EM11SFCG4umhXYLuntQ%3D%3D; _gcl_au=1.1.1158505543.1733145959; _gid=GA1.2.896092194.1733145962; _gat_UA-1392039-4=1; _ga_48T6WSL1GL=GS1.1.1733145961.1.0.1733145961.0.0.0; _ga=GA1.1.210174018.1733145962; _fbp=fb.1.1733145961906.21520154942814509; _uetsid=f98b0830b0b011efba4d77ba630ea5bc; _uetvid=f98b2310b0b011ef84747581a0d71a9d; _ga_T1G146JZ1T=GS1.2.1733145962.1.0.1733145962.60.0.0',
'Cookie': '_gcl_au=1.1.977732413.1733143070; __stripe_mid=6442f912-20c3-47c0-9136-a161d7ca498ac15426; _fbp=fb.1.1733144919760.767941378258953322; __gads=ID=f831f14fafe4ff5a:T=1733576875:RT=1733577412:S=ALNI_MYx9YxmtJJhIS1Q6vepvVIUFGIjHQ; __gpi=UID=00000f86ecc3ce29:T=1733576875:RT=1733577412:S=ALNI_MaRE6dFiwxkuRD7czxyPG6SdZkoXQ; __eoi=ID=671590210ec3d9f9:T=1733576875:RT=1733577412:S=AA-AfjZqwhiniwF2EO6PDt1N6iXR; _ga=GA1.1.1487794060.1733143071; _ga_T1G146JZ1T=GS1.2.1734083553.23.1.1734083802.60.0.0; breakpoint=xlarge; _ga_48T6WSL1GL=GS1.1.1734701476.74.1.1734701478.0.0.0; _machinetools.com=SzOtFQDSyf9bNsExkPbb29C16k4P1sifqsoWtBMuNmLKJeD%2Biy0iESTrUohObz7GAuPqosiFZy%2BelaQ0%2BjJ4R2ngVp%2BIFM6KqTDvN6rT7PyqKC1EyOiqLGmMsmSe0F7kPFaZUsZN2L5i4n%2FqD%2B5KN2DYkTJWqcesQ889MkYVzX%2FcmNRpPqgSXkuNM2nDjg9OM6f3VnZcjEBb9ySG9UFpxLb9OqtVcQ08j7L6kYfuiQbU5PZHKvQUSKWGFmVx1TbwCjoCTQyUCD8fMKZ8DvbiBRniWrpVdILCfg%3D%3D--aQOuBgm1lfLom9rf--k5CbvdGoKCz0XqngDmqSWw%3D%3D; _uetsid=8dd31300bec711efb42af92f63e37a04; _uetvid=3e6ee210b0aa11efb60fc33bbe65d470; __stripe_sid=b5020a07-0711-48b1-978c-337976cf4a200a0b83',
'Host': 'www.machinetools.com',
'If-None-Match': 'W/"b4c1098fb8fbc7ad76b48539b464ba64"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"'
   }
h2 = {
'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '351',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': '_gcl_au=1.1.977732413.1733143070; __stripe_mid=6442f912-20c3-47c0-9136-a161d7ca498ac15426; _gid=GA1.2.598426562.1733144919; _fbp=fb.1.1733144919760.767941378258953322; _ga_T1G146JZ1T=GS1.2.1733247765.7.1.1733248028.60.0.0; breakpoint=xlarge; __stripe_sid=bc3a5e95-cf4b-4eec-b51f-45c39458640bf55db0; _ga=GA1.1.1487794060.1733143071; _uetsid=3e6eacd0b0aa11efa96c61e63bcb88f8; _uetvid=3e6ee210b0aa11efb60fc33bbe65d470; _ga_48T6WSL1GL=GS1.1.1733305618.11.1.1733309965.0.0.0; _machinetools.com=8KVk84FU4ucTrdVm8dA0F0IgSJ5DSUHLxjzFtyjRPiRvJ2zRNyufXckI1tSRyNC%2BxWejubQJsYC8trjJMWl6%2FTUKJKpDehLDfmSvwzoDlVVaxRl3FsUGxk159Tq5qH8H22GmkBipcEoRp4HdIVDtZ0xtYNF1jAVn7JMWeTfdbIg6V43jtAWE%2FFYyB%2F8FY08TwYVokl08%2BFvQJt5suIKnXXrfwJaPAUP7qHZm4KzfPz3h%2FSFnh5%2FwZigT6bi01UlzPzXiABXpXjA8zeDLuWhkPOyN%2B%2Bgq%2BSB%2FiA%3D%3D--rIKkt6IDZZaR5cfX--7SD8VVaHBqBvgUENX7Os7A%3D%3D',
'DNT': '1',
'Host': 'www.machinetools.com',
'Origin': 'https://www.machinetools.com',
'Referer': 'https://www.machinetools.com/en/for-sale/611536-eaton-leonard-vb50hp-pipe-tube-and-bar-benders',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
'X-CSRF-Token': 'JpkLNrDztqLaXxuN0YxAa7fLQ8y7TXNCD1hzdoUTMAJLxxr1j-5aigD_GqQ_ZjzRxsMat-Opqry2_6o0yOc_9Q',
'X-NewRelic-ID': 'VwIOUVBSGwEEUVhTDgI=',
'X-Requested-With': 'XMLHttpRequest',
'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"'
      }
def check(url):
    retries = 3
    for i in range(retries):
        try:
            pg = requests.get(url,headers=h, timeout=120)
            print(pg)
            s1 = bs(pg.content,'html.parser')
            return s1
            # pg.raise_for_status()  # Raises an error for bad status codes (4xx, 5xx)
            # print(pg.text)  # Process the response data as needed
            break  # Exit loop if successful
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i + 1} failed: {e}")
            sleep(5)  # Wait before retrying
#%%

s1 = bs(pg.content,'html.parser')
s2 = s1.findAll('a',{'class':'type underline-hover'})
l = []
for i in s2:
    print(i.text)
    v = dict(
    link = i['href'],
    title = i['title'],
    count = int(i.find(attrs={'class':'count'}).text.replace(',',''))
    )
    l.append(v)
    # break
df = pd.DataFrame(l)
#%%
l2 = []
for j in df.values:
    print(j[1])
    # print('____________________________________________________')
    url2 = burl+j[0]
    soup = check(url2)
    all_types = soup.find(attrs = {'class':'other-types'})
    
    for tyti,tyli in zip(all_types.findAll('div',{'class':'type-title'}),all_types.findAll('ul',{'class':'type-links'})):
        # print(tyti.text)
        type_t = tyti.text.strip()
        
        
        for k in tyli.findAll('li'):
            data = {
                "Main_Category":j[1],
                "Main_Category_Link":j[0],
                "Main_Category_Count":j[2]
                }
            data['Sub_Category'] = type_t
            # print(k)
            type_link = k.find('a')['href']
            type_h = k.find('a').text.strip()
            type_c = int(k.text.replace(type_h,"").replace('(',"").replace(')',"").strip())
            # print(type_h)
            data['Type'] = type_h
            data['Type_Link'] = type_link
            data['Type_Count'] = type_c
            # print(data)
            l2.append(data)
            # data.pop('Type')
            # data.pop('Type_Link')
            # data.pop('Type_Count')
            # break
        # break
        
    # break
df2 = pd.DataFrame(l2)
df3 = df2
l3 = []
c=1
for i3 in df3.to_dict(orient='records'):
    # print(i3)
    print(c,'1930')
    c+=1
    url = f"{burl}{i3['Type_Link']}?_page_size={i3['Type_Count']+10}"
    soup = check(url)
    for i4 in soup.findAll('h3',{'class':'hover bold title'}):
        # print(i4.text)
        
        l3.append(i3|{"Product_Name":i4.text,
         "Product_Link":i4.find('a')['href']
         })
        
    # break
df4 = pd.DataFrame(l3)
#%%
def clean_string(value):
    if isinstance(value, str):
        # Replace characters that are not in the ASCII range
        return ''.join([char for char in value if ord(char) < 128])
    return value  # return the value unchanged if it's not a stringord(c) < 128)

# Apply this function to all string columns
for col in df4.select_dtypes(include='object'):
    df4[col] = df4[col].apply(lambda x: clean_string(str(x)))
    
import xlsxwriter

# Create an Excel file and write the DataFrame using xlsxwriter
with pd.ExcelWriter(r'D:\Projects\Sujit\All_Links.xlsx', engine='xlsxwriter') as writer:
    df4.to_excel(writer, index=False, sheet_name='Sheet1')

url = "https://www.machinetools.com/en/for-sale/606407-daito-cr4816-beam-coping-machines"
#%%
import re
from time import time
df4 = df4[df4['Main_Category'] == 'Production Lines & Plants']

h={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'breakpoint=xlarge; _machinetools.com=m3ge1QYPDhgSkOJWza09pXY7eoR5GvZZUKiO6MgJKKm1w%2Bz2CH%2FE2HgcCLnU8dnj7IeQk24DhvFIB86VxlKp5APNJJ937oIXdfaLtn6cvEWKDViRG%2Fd03m%2BXOCMed0jH6W7%2BEt8u%2FC0ZF1y7sR7m2OgNgUoVlWU9n48NJc%2FpnIpKXVfruDbe0Gi9Bnsrevq1OxTnAVAjeDChzuazQSkdSDIgxFRdxh45m08apVptXdlWIRYmXzZyF%2F2eEF1hNzQay6TzoZqRI4883twz76Lr3TUYXDHP8NPUSw%3D%3D--So0UBUfoRUsXhT8O--sw6EM11SFCG4umhXYLuntQ%3D%3D; _gcl_au=1.1.1158505543.1733145959; _gid=GA1.2.896092194.1733145962; _gat_UA-1392039-4=1; _ga_48T6WSL1GL=GS1.1.1733145961.1.0.1733145961.0.0.0; _ga=GA1.1.210174018.1733145962; _fbp=fb.1.1733145961906.21520154942814509; _uetsid=f98b0830b0b011efba4d77ba630ea5bc; _uetvid=f98b2310b0b011ef84747581a0d71a9d; _ga_T1G146JZ1T=GS1.2.1733145962.1.0.1733145962.60.0.0',
'Host': 'www.machinetools.com',
'If-None-Match': 'W/"b4c1098fb8fbc7ad76b48539b464ba64"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"'
   }
session = requests.Session()
url = "https://www.machinetools.com/en/sessions/new?modal=true"
url2 = 'https://www.machinetools.com/en/sessions'
pg = session.get(url,headers=h)
# print(pg)
s1 = bs(pg.content,'html.parser')
token = s1.find(attrs={'name':'authenticity_token'})['value']
subject = s1.find(attrs={'name':'bt[subject]'})['value']
d = {
'authenticity_token': token,
'bt[body]': '',
'bt[message]': '',
'bt[content]': '',
'bt[subject]': subject,
'all_types': 'true',
'from_modal': 'true',
'email': '',
'existing': 'yes',
'password': '',
'first_name': '',
'last_name': '',
'company_name': '',
'phone': '',
'country_id': '105',
'state_id': '',
'address_1': '',
'address_2': '',
'city': '',
'zip': '',
'industry_simple': '',
'industry_other': '',
'g-recaptcha-response': '',
'commit': 'Log In',
'login_redirect': '/en',
'with-processing-download': int(time()*1000)
     }
pg2 = session.post(url2,headers=h,data=d)

def login_check(url):
    h2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'www.machinetools.com',
    'If-None-Match': 'W/"b4c1098fb8fbc7ad76b48539b464ba64"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
          }
    pg3 = session.get(url,headers=h2,cookies=pg2.cookies)
    s1 = bs(pg3.content,'html.parser')
    return s1
    
df4.rename(columns={'Type': 'Segment'}, inplace=True)

def scraper_for_used_newinstock(url):
    soup = login_check(url)
    a = soup.find('section',{'class':'overview'})
    d = {}
    if a:
        for key,val in zip(a.findAll('div',{'class':'label'}),a.findAll('div',{'class':'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    b = soup.find('div',{'class':'listing-specs'})
    if b:
        for k2 in b.findAll('tr'):
            v = k2.findAll('td')
            d[v[0].text.strip()] = v[1].text.strip()
    print(d)
    d['Description'] = soup.find('div',{'class':'text-block accordion-content'})
    if d['Description']:
        d['Description'] = d['Description'].text.replace('\r\n'," ")
    d['Specsheet'] = soup.find('div',{'class':'subtext spec-sheet'})
    if d['Specsheet']:
        d['Specsheet'] = d['Specsheet'].text.replace('\r\n'," ").replace('\n'," ").replace('\t'," ")
    seller = soup.find('section', id=re.compile(r'^for_sale_')).find('a',{'class':'underline-hover'})
    if seller:
        d['Seller_Name'] = seller.text
        d['Seller_Url'] = seller['href']
    return d
def scraper_for_newmachinery(url):
    soup = check(url)
    a = soup.find('div',{'class':'listing-details'})
    d = {}
    if a:
        for key,val in zip(a.findAll('div',{'class':'label'}),a.findAll('div',{'class':'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    b = soup.find('div',{'class':'model-specs'})
    if b:
        for key,val in zip(b.findAll('div',{'class':'label'}),b.findAll('div',{'class':'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    print(d)
    distributors = sales_offices = service_offices = []
    overview = about_company = pdf_link = None
    try:
        distributors = [{'Distribotor Name':i.text,'Distribotor Link':i['href']} for i in soup.find('div',{'id':'distributors'}).findAll('a')]
    except:pass
    try:
        sales_offices = [{'SalesOffice Name':i.text,'SalesOffice Link':i['href']} for i in soup.find('div',{'id':'offices'}).findAll('a')]
    except:pass
    try:
        service_offices = [{'ServiceOffice Name':i.text,'ServiceOffice Link':i['href']} for i in soup.find('div',{'id':'manufacturer_servicers'}).findAll('a')]
    except:pass
    try:
        overview = soup.find('div',{'id':'model-overview'}).find('p').text
    except:pass
    try:
        about_company = soup.find('div',{'id':'about-company'}).find('p').text
    except:pass
    try:
        pdf_link = soup.find('a',{'class':['pdf']})['href']
    except:pass
    d['PDF_Link'] = pdf_link
    d['Distributors'] = distributors
    d['Sales Office'] = sales_offices
    d['Service Office'] = service_offices
    d['Overview'] = overview
    d['About Company'] = about_company
    return d

l = []
for i5 in df4.to_dict(orient='records'):
    print(len(l)+1,len(df4))
    url = f"{burl}{i5['Product_Link']}"
    if i5['Segment'] == 'Used' or i5['Segment'] == 'New In-Stock':
        data = scraper_for_used_newinstock(url)
    else:
        data = scraper_for_newmachinery(url)
    l.append(i5|data)
    # break
df5 = pd.DataFrame(l)
df5.to_excel(r'Production Lines & Plants.xlsx',index=False)