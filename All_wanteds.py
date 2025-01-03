import requests
from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd

burl = "https://www.machinetools.com"
url = burl+"/en/machinery"

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
soup = check("https://www.machinetools.com/en/wanteds")
#%%
l = []
for i in soup.findAll('section',{'class':'types-table section-margin-lg'}):
    for j in i.findAll('a'):
        
        url = f"{burl}{j['href']}"
        soup2 = check(url)
        try:
            for k in soup2.find('section',{'class':'types-table'}).findAll('a',{'class':'type underline-hover'}):
                d = {"Main_Category":j.find('div',{'class':'name'}).text,
                 "Main_Category_Link":j['href']}
                d['Sub_Category'] = k.find('div',{'class':'name'}).text
                d['Sub_Category_Link'] = k['href']
                l.append(d)
                # break
        except:
            d = {"Main_Category":j.find('div',{'class':'name'}).text,
             "Main_Category_Link":j['href']}
            d['Sub_Category'] = j.find('div',{'class':'name'}).text
            d['Sub_Category_Link'] = j['href']
            l.append(d)
            
        # break
    # break
#%%
c=1
l3 = []
for i3 in l:
    # print(i3)
    print(c,len(l))
    c+=1
    url = f"{burl}{i3['Sub_Category_Link']}?_page_size=200"
    soup = check(url)
    for i4 in soup.findAll('h3',{'class':'hover bold'}):
        # print(i4.text)
        
        l3.append(i3|{"Product_Name":i4.text,
         "Product_Link":i4.find('a')['href']
         })
        #%%
def scraper_for_newmachinery(url):
    soup = check(url)
    a = soup.find('div',{'class':'listing-details'})
    d = {}
    if a:
        for key,val in zip(a.findAll('div',{'class':'label'}),a.findAll('div',{'class':'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    b = soup.find('div',{'class':'listing-specs'})
    if b:
        for key,val in zip(b.findAll('div',{'class':'label'}),b.findAll('div',{'class':'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    print(d)
    d['Description'] = soup.find('div',{'class':'text-block'})
    if d['Description']:
        d['Description'] = d['Description'].text.replace('\r\n'," ")
    distributors = sales_offices = service_offices = []
    overview = about_company = None
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
    d['Distributors'] = distributors
    d['Sales Office'] = sales_offices
    d['Service Office'] = service_offices
    d['Overview'] = overview
    d['About Company'] = about_company
    return d