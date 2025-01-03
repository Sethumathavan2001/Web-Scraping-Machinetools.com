import re, pandas as pd, requests
from time import time,sleep
from bs4 import BeautifulSoup as bs
import multiprocessing

burl = "https://www.machinetools.com"
# df4 = pd.read_csv(r"D:\Projects\Sujit\All\New folder\indlink.csv")
# df4 = df4[df4['Main_Category'] == 'Machining Centers']
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
'email': '',#put your email id here
'existing': 'yes',
'password': '',#put your password here
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

# Function to check URL and return the BeautifulSoup object
def check(url):
    retries = 3
    for i in range(retries):
        try:
            pg = requests.get(url, headers=h, timeout=120)
            print(pg)
            s1 = bs(pg.content, 'html.parser')
            return s1
        except:
            print(f"Attempt {i + 1}")
            sleep((i + 1) * 10)  # Wait before retrying


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
    retries = 3
    for i in range(retries):
        try:
            pg3 = session.get(url,headers=h2,cookies=pg2.cookies)
            s1 = bs(pg3.content,'html.parser')
            return s1
        except:
            print(f"Attempt {i + 1} ")
            sleep((i + 1) * 10)  # Wait before retrying
def login_check_json(url,csrftoken,xpid):
    h2 = {
'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8',
'Connection': 'keep-alive',
# 'Cookie': '_gcl_au=1.1.977732413.1733143070; __stripe_mid=6442f912-20c3-47c0-9136-a161d7ca498ac15426; _gid=GA1.2.598426562.1733144919; _fbp=fb.1.1733144919760.767941378258953322; breakpoint=xlarge; _ga_T1G146JZ1T=GS1.2.1733386622.12.1.1733387516.60.0.0; __stripe_sid=c95c3a68-2deb-467e-8c33-f073acb1900ce98ce3; _mt_suid=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWXlPRGMwT1NJPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLl9tdF9zdWlkIn19--007fc233014dc210a8d2d2d7f279beb13e3a37db; _mt_sutoken=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqZGpPVEEyTmpjNU1EUTJNRGhqTURJd09Ea3pZbUpoTmpCbE16Um1NaUk9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX210X3N1dG9rZW4ifX0%3D--a4d5bf07915517b42a9cf20b91399990245b36f3; _ga=GA1.1.1487794060.1733143071; _mt_uat-v2=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWmpPV1UxTWpjNE5qTTJZMkUzWVRnd1lXRmtOamM1TURsbU9UVTBOemMwTUdSak5tTmhZVGcyT1RrM1lqRTJZell6WkRRMFptRXdNRFJtTURNM05UUWkiLCJleHAiOiIyMDI1LTAzLTA1VDEyOjQxOjE5LjI5NVoiLCJwdXIiOiJjb29raWUuX210X3VhdC12MiJ9fQ%3D%3D--92846c5aed10cd0ff196d5e4a8b6152504964783; _ga_48T6WSL1GL=GS1.1.1733401329.23.1.1733402533.0.0.0; _machinetools.com=wdu6AA6JVtN1In2bz57qldJmxZc3Ddf7qZzdktBVaObcPE2%2Fr6IEK%2FI9j6ACHfiCVQ%2FQhJqUSxRAyKMHIV6i1JgcvNagHMT9vw5emLtUHY5tmJk8Y6AA2v9B59kKHYJh87rLYEjdvmIcZ%2FX4E46NE7damPG5kMBpR8sdPWa3t8wJvC4P623CvoOjBbU0Qrke3t9Ow3PwBmAhfrP%2FyiN34XS9X8LgKCVrYhMb%2BG4KQLh77RNRIfbeLATMqmZV8ujx1aLsfPtelvH57efww4XUaILU60AUH3bsoA%3D%3D--%2F%2FoqyTD%2FXrajW13R--e3J0dgsz2qyPFk21jXUvaw%3D%3D; _uetsid=3e6eacd0b0aa11efa96c61e63bcb88f8; _uetvid=3e6ee210b0aa11efb60fc33bbe65d470',
'DNT': '1',
'Host': 'www.machinetools.com',
'If-None-Match': 'W/"b4c1098fb8fbc7ad76b48539b464ba64"',
'Referer': 'https://www.machinetools.com/en/companies/4988-elb-america-inc-aba-grinding-technologies-gmbh',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
'X-CSRF-Token': csrftoken,
'X-NewRelic-ID': xpid,
'X-Requested-With': 'XMLHttpRequest',
'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"'
          }
    retries = 3
    for i in range(retries):
        try:
            pg3 = session.get(url,headers=h2,cookies=pg2.cookies)
            return pg3.json()
        except:
            print(f"Attempt {i + 1}")
            sleep((i + 1) * 10)  # Wait before retrying
    # s1 = bs(pg3.content,'html.parser')
    # return s1

# df4.rename(columns={'Type': 'Segment'}, inplace=True)

def scraper_for_industry(url):
    soup = check(url)
    csrftoken = soup.find('meta',{'name':'csrf-token'})['content']
    for i in soup.findAll('script',{'type':'text/javascript'}):
        if 'xpid' in i.text:
            xpid = i.text.split('xpid:"')[1].split('"')[0]
            break
    website_get = p = None
    # try:
    #     website_get = login_check_json(f"{url}/website_request",csrftoken,xpid)['url']
    # except:pass
    # try:
    #     phone_dict = login_check_json(f"{url}/phone_request",csrftoken,xpid)
    #     p = bs(phone_dict['update'])
    # except:pass
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
    if p:
        for key,val in zip(p.findAll('div',{'class':'label'}),p.findAll('div',{'class':'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    print(d)
    # d['Website'] = website_get
    brand = Company_Specialties = typelist = []
    discription  = pdf_link = None
    try:
        discription = soup.find('section',{'class':'content-divisor section-margin'}).find('p').text
    except:pass
    try:
        Company_Specialties = [i.text for i in soup.find('ul',{'class':'types'}).findAll('li')]
    except:pass
    try:
        brand = [{'Brand Name':i.text,'Brand Link':i.find('a')['href']} for i in soup.find('ul',{'class':'brands'}).findAll('li')]
    except:pass
    try:
        typelist = [{'Type Name':i.text,'Type Link':i.find('a')['href']} for i in soup.find('ul',{'class':'product-lines'}).findAll('li')]
    except:pass
    # try:
    #     locations = soup.find('div',{'id':'about-company'}).find('p').text
    # except:pass
    try:
        pdf_link = soup.find('a',{'class':['pdf']})['href']
    except:pass
    d['PDF_Link'] = pdf_link
    d['Discription'] = discription
    d['Company Specialties'] = Company_Specialties
    d['Brand'] = brand
    d['TypesList'] = typelist
    # d['About Company'] = about_company
    return d

def process_row(i5):
    # print(i5['Product_Name'])
    # print()
    url = f"{burl}{i5['Product_Link']}"
    # if i5['Segment'] == 'Used' or i5['Segment'] == 'New In-Stock':
    data = scraper_for_industry(url)
    # else:
    #     data = scraper_for_newmachinery(url)
    return i5|data
if __name__ == '__main__':
    print("Start")
    results = []
    c = 1
    for link in missingl:
        if pd.isna(link):
            continue
        print(c,'https://www.machinetools.com'+link)
        c+=1
        data = scraper_for_industry('https://www.machinetools.com'+link)
        print(data)
        
        results.append({"Url":link}|data)
        # break
    # with multiprocessing.Pool(processes=multiprocessing.cpu_count()//2) as pool:
    #     results = pool.map(process_row, df4.to_dict(orient='records'))
    
    # Create DataFrame from the results and save it to Excel
    df5 = pd.DataFrame(results)
    # df5.to_csv(r'"D:\Projects\Sujit\All\New folder\indlink_data.csv"', index=False)