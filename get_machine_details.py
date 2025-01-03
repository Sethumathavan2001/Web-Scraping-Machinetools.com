import re, pandas as pd, requests
from time import time,sleep
from bs4 import BeautifulSoup as bs
import multiprocessing

burl = "https://www.machinetools.com"
df4 = pd.read_csv(r"machines_link.csv")
# df4 = df4[df4['Main_Category'] == 'Machining Centers']
h={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_gcl_au=1.1.977732413.1733143070; __stripe_mid=6442f912-20c3-47c0-9136-a161d7ca498ac15426; _fbp=fb.1.1733144919760.767941378258953322; __gads=ID=f831f14fafe4ff5a:T=1733576875:RT=1733577412:S=ALNI_MYx9YxmtJJhIS1Q6vepvVIUFGIjHQ; __gpi=UID=00000f86ecc3ce29:T=1733576875:RT=1733577412:S=ALNI_MaRE6dFiwxkuRD7czxyPG6SdZkoXQ; __eoi=ID=671590210ec3d9f9:T=1733576875:RT=1733577412:S=AA-AfjZqwhiniwF2EO6PDt1N6iXR; _ga=GA1.1.1487794060.1733143071; _ga_T1G146JZ1T=GS1.2.1734083553.23.1.1734083802.60.0.0; _mt_uat-v2=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWmpPV1UxTWpjNE5qTTJZMkUzWVRnd1lXRmtOamM1TURsbU9UVTBOemMwTUdSak5tTmhZVGcyT1RrM1lqRTJZell6WkRRMFptRXdNRFJtTURNM05UUWkiLCJleHAiOiIyMDI1LTAzLTIwVDE2OjA0OjA3LjMzNloiLCJwdXIiOiJjb29raWUuX210X3VhdC12MiJ9fQ%3D%3D--f8b3b936bb0c9e049fbea14314e186dd6ae5960e; __stripe_sid=6736a8cb-e052-476b-9f39-ff4073833fde38502f; breakpoint=xlarge; _machinetools.com=dWVjlfqaF5veWVi93aY5t8I3gKcZI1I%2B79NmUADXDkMane1Fg6bNIpwA5QdEc3SsXXu%2BwbKFvQ1WUc%2FXZHgN3a45enCf0V%2BEE2Gli1OXcaaB35sDkvq9bJb9JkDixEg0KanWm0wghe4XW0352vqD5wAWcYsfmn2guTYuy2wQ8%2BlcM8mzQBQk6AEgORRWZALNwEUsOuftl3IyoGlCKzb4tbdjMqnrM9BleDvZh9SkJkQT59YrUmn9j4TjqVpjTkpBk7iqJ3RvWQZUWAAegYPuBr2L1WpXyNV%2BmQ%3D%3D--900F3Tp%2BZB6COOOi--iAhrhwvJ0QMcfa221BwPZA%3D%3D; _ga_48T6WSL1GL=GS1.1.1734748610.76.1.1734750447.0.0.0; _uetsid=8dd31300bec711efb42af92f63e37a04; _uetvid=3e6ee210b0aa11efb60fc33bbe65d470',
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
        except Exception as e:
            print(f"Attempt {i + 1} failed: {e}")
            sleep((i + 1) * 30)  # Wait before retrying


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
    n=1
    while n<4:
        try:
            pg3 = session.get(url,headers=h2,cookies=pg2.cookies)
            s1 = bs(pg3.content,'html.parser')
            return s1
        except:
            return None
            print('Sleeping')
            # sleep(n*10)
            n+=1
    
# df4.rename(columns={'Type': 'Segment'}, inplace=True)

def scraper_for_used_newinstock(url):
    # soup = login_check(url)
    soup = check(url)
    if not soup:
        return {}
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
    try:
        seller = soup.find('section', id=re.compile(r'^for_sale_')).find('a',{'class':'underline-hover'})
    except:seller = None
    if seller:
        d['Seller_Name'] = seller.text
        d['Seller_Url'] = seller['href']
    try:
        pdf_link = soup.find('a',{'class':['pdf']})['href']
    except:pdf_link = None
    d['PDF_Link'] = pdf_link

    return d
def scraper_for_newmachinery(url):
    soup = check(url)
    if not soup:
        return {}
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
    overview = about_company = pdf_link =  None
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

# l = []
# for i5 in df4.to_dict(orient='records'):
#     print(len(l)+1,len(df4))
#     url = f"{burl}{i5['Product_Link']}"
#     if i5['Segment'] == 'Used' or i5['Segment'] == 'New In-Stock':
#         data = scraper_for_used_newinstock(url)
#     else:
#         data = scraper_for_newmachinery(url)
#     l.append(i5|data)
    # break
# df5 = pd.DataFrame(l)
# df5.to_excel(r'D:\Projects\Sujit\Production Lines & Plants.xlsx',index=False)
def process_row(i5):
    # print(i5['Product_Name'])
    # print()
    url = f"{burl}{i5['Product_Link']}"
    print(url)
    print()
    if i5['Segment'] == 'Used' or i5['Segment'] == 'New In-Stock':
        data = scraper_for_used_newinstock(url)
    else:
        data = scraper_for_newmachinery(url)
    return i5|data
if __name__ == '__main__':
    print("Start")
    before_time = time()
    for i in range(0,len(df4),1000):
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()//2) as pool:
            results = pool.map(process_row, df4.to_dict(orient='records')[i:i+1000])
    
    # Create DataFrame from the results and save it to Excel
        df5 = pd.DataFrame(results)
        df5.to_csv(rf'All_Missing_{i}_{i+1000}.csv', index=False)
    after_time = time()
    print(f"Total Time Taken: {after_time-before_time} Secondes")
