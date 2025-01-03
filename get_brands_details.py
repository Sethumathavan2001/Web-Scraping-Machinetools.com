import requests
from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
import multiprocessing

# Your burl and headers
burl = "https://www.machinetools.com"
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
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i + 1} failed: {e}")
            sleep((i + 1) * 10)  # Wait before retrying

# Your scraper function
def scraper_for_newmachinery(v):
    print(v)
    url = f"{burl}{v['Brand Link']}"
    soup = check(url)
    a = soup.find('div', {'class': 'listing-details'})
    d = {}
    if a:
        for key, val in zip(a.findAll('div', {'class': 'label'}), a.findAll('div', {'class': 'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1
    b = soup.find('div', {'class': 'model-specs'})
    if b:
        for key, val in zip(b.findAll('div', {'class': 'label'}), b.findAll('div', {'class': 'value'})):
            key1 = key.text.strip()
            val1 = val.text.strip()
            d[key1] = val1

    # Adding other fields (distributors, sales offices, etc.)
    distributors = sales_offices = service_offices = typeslist = segmentlist = []
    overview = about_company = description = None
    try:
        distributors = [{'Distribotor Name': i.text, 'Distribotor Link': i['href']} for i in soup.find('div', {'id': 'distributors'}).findAll('a')]
    except: pass
    try:
        sales_offices = [{'SalesOffice Name': i.text, 'SalesOffice Link': i['href']} for i in soup.find('div', {'id': 'offices'}).findAll('a')]
    except: pass
    try:
        service_offices = [{'ServiceOffice Name': i.text, 'ServiceOffice Link': i['href']} for i in soup.find('div', {'id': 'manufacturer_servicers'}).findAll('a')]
    except: pass
    try:
        overview = soup.find('div', {'id': 'model-overview'}).find('p').text
    except: pass
    try:
        about_company = soup.find('div', {'id': 'about-company'}).find('p').text
    except: pass
    try:
        description = soup.find('section', {'class': 'content-divisor section-margin'}).find('p').text
    except: pass
    try:
        typeslist = [{'Type Name': i.text, 'Type Link': i.find('a')['href']} for i in soup.find('ul', {'class': 'product-lines'}).findAll('li')]
    except: pass
    try:
        segmentlist = [{'Segment Name': i.text.replace(i.find('span', {'class': 'count'}).text, ""), 'Segment Link': i.find('a')['href'], "Segment Count": i.find('span', {'class': 'count'}).text} for i in soup.find('ul', {'class': 'button-list section-margin'}).findAll('li')]
    except: pass

    d['Segment List'] = segmentlist
    d['Types_List'] = typeslist
    d['Description'] = description
    d['Distributors'] = distributors
    d['Sales Office'] = sales_offices
    d['Service Office'] = service_offices
    d['Overview'] = overview
    d['About Company'] = about_company

    return v | d

# Main function
def main():
    df = pd.read_excel(r'Brand_Link.xlsx')  # Load your Excel file
    df = df[df.Brand.isna()]
    records = df.to_dict(orient="records")

    # Set up the multiprocessing pool
    num_cpus = multiprocessing.cpu_count()  # Get number of CPU cores
    pool = multiprocessing.Pool(processes=num_cpus // 2)  # Use half of the available CPU cores

    # Use map to distribute the work across processes
    results = pool.map(scraper_for_newmachinery, records)
    # Combine results into a single DataFrame
    final_df = pd.DataFrame(results)
    final_df.to_csv(r'Brand_data.csv', index=False)  # Save the data to a CSV file

    pool.close()  # Close the pool
    pool.join()   # Wait for the pool to finish

if __name__ == '__main__':
    main()
