import requests
from django.shortcuts import render

from bs4 import BeautifulSoup

# Create your views here.
def showlink(request):

    return render(request, 'showlink.html')

###################################################
# VIEW
###################################################
"""def home(request):

      

    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    r = requests.get("https://www.amazon.com/gp/profile/amzn1.account.AG7BVCPAJAA55B2TAVXEEKUDBSVA?preview=true", stream=True, headers=headers)
    #r = requests.get("https://amzn.to/2WHGWv0", headers=headers)
    #r = requests.get("https://smile.amazon.com/gp/profile/amzn1.account.AG7BVCPAJAA55B2TAVXEEKUDBSVA?preview=true", headers=headers)
    #soup = BeautifulSoup(r.content, 'html.parser')
    return render(request, 'showlink.html',
                      {'contents': r.text, 'errorcode': r})

"""
###################################################
def home(request):
    import pyderman as cdi
    path = cdi.install(file_directory='c:\\data\\chromedriver\\', verbose=True, chmod=True, overwrite=False,
                       version=None)
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    #options.add_argument("headless")
    driver = webdriver.Chrome("c:\\data\\chromedriver\\chromedriver.exe", chrome_options=options)
    #driver.set_page_load_timeout(2)

    r = driver.get("https://www.amazon.com/gp/profile/amzn1.account.AG7BVCPAJAA55B2TAVXEEKUDBSVA?preview=true")

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    #i = 1
    #while i==i:
     #   i=1
    return render(request, 'gohere.html', {'done': 'done'})

