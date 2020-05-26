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
    from selenium.webdriver.common.touch_actions import TouchActions

    path = cdi.install(file_directory='c:\\data\\chromedriver\\', verbose=True, chmod=True, overwrite=False,
                       version=None)
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    #options.add_argument("headless")
    driver = webdriver.Chrome("c:\\data\\chromedriver\\chromedriver.exe", chrome_options=options)
    driver.implicitly_wait(100)
    #driver.set_page_load_timeout(2)

    driver.get("https://www.amazon.com/gp/profile/amzn1.account.AG7BVCPAJAA55B2TAVXEEKUDBSVA?preview=true")
    #data = driver.find_element_by_class_name('a-profile-content')

    scroll(driver, 30)
    # Once scroll returns bs4 parsers the page_source
    soup = BeautifulSoup(driver.page_source, 'lxml') #lxml is faster than html
    # Them we close the driver as soup_a is storing the page source
    driver.close()

    # Empty array to store the links
    links = []
    # Looping through all the a elements in the page source
    for link in soup.find_all('a'):
        link.get('href')
        links.append(link.get('href'))
    return render(request, 'gohere.html', {'done': links})

###################################################

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        import time
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height