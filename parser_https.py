import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

ua = UserAgent()


def run(proxys_list,proxys_valid,counts=0):
    __parse_proxies_one(proxys_list)
    __parse_proxies_two(proxys_list)
    __parse_proxies_three(proxys_list)
    __parse_proxies_four(proxys_list)
    __parse_proxies_five(proxys_list)
    __parse_proxies_six(proxys_list)
    check_ip(proxys_list,proxys_valid,counts)

def __parse_proxies_one(proxys_list):
    r = requests.get('https://www.sslproxies.org/')
    html = BS(r.content, 'lxml')
    for el in html.select('.form-control'):
        ssl = el.text.split()[9:40]
        for i in ssl:
            proxys_list.append(i)
            
def __parse_proxies_two(proxys_list):
    r = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=500&country=all').text.split()
    for i in r:
        proxys_list.append(i)
   
def __parse_proxies_three(proxys_list):
    r = requests.get('https://free-proxy-list.net/anonymous-proxy.html')
    html = BS(r.content, 'lxml')
    for el in html.select('.form-control'):
        ssl = el.text.split()[9:40]
        for i in ssl:
                proxys_list.append(i)
            
def __parse_proxies_four(proxys_list):     
    r = requests.get('https://free-proxy-list.net/')
    html = BS(r.content, 'lxml')
    for el in html.select('.form-control'):
        ssl = el.text.split()[9:40]
        for i in ssl:
            proxys_list.append(i)

def __parse_proxies_five(proxys_list):     
    r = requests.get('https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt').text.split()[:40]
    for i in r:
        proxys_list.append(i)

def __parse_proxies_six(proxys_list):
    r = requests.get('https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt').text.split()[:40]
    for i in r:
        proxys_list.append(i)
    
def check_ip(proxys_list,proxys_valid,counts):
    #g = time.time()
    for i in proxys_list:
        try:
            proxies = {
            'http': f'http://{i}',
            'https': f'http://{i}'
            }
            headers = {
                'User-Agent': ua.random
            }
            url_google = 'https://www.google.com'
            google_reguest = requests.get(url_google,proxies=proxies,headers=headers,timeout=0.25)
            if google_reguest.status_code == 200:
                print(i)
                proxys_valid.append(i)
                if len(proxys_valid) == counts:
                    break
        except:
                pass
#http://icanhazip.com/  
#http://ip-api.com/json/
#http://ip-api.com/json/?fields=8217
