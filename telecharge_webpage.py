import os
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.chrome.options import Options

df = pd.read_excel('list_access.xlsx', index_col=0)
df = pd.concat([df, pd.DataFrame(columns=['Access'])], axis=1)
# urls = df['Access_URL']
urls = ['http://pidila.gitlab.io/info-site/accessibilite.html']
for i, j in enumerate(urls):
    print(type(j))
    if type(j) != float:
        url = j
        # url = j[2:len(j)-2]
        # for jj in j:
        try:
            ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
            req = urllib.request.Request(url, headers=ua_headers)
            resp = urllib.request.urlopen(req)
        except:
            df.iloc[i, 5] = 'NO'
            continue
        df.iloc[i, 5] = 'YES'
        file_name = str(i)
        path = os.path.join(os.path.abspath('.'), file_name)
        print(path)
        # open page with selenium
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': path}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(executable_path='/Users/ethanyang/chromedriver', chrome_options=options)
        driver.get(url)
        action = ActionChains(driver).move_by_offset(0, 0).context_click().perform()
        pyautogui.typewrite(['down', 'down', 'down', 'enter'])
        time.sleep(3)
        pyautogui.typewrite(['enter'])
        time.sleep(3)
        driver.close()
df.to_excel('Acess_status.xlsx')