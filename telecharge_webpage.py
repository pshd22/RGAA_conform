import os
import urllib.request
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import shutil

df = pd.read_excel('list_access.xlsx', index_col=0)
df = pd.concat([df, pd.DataFrame(columns=['Access'])], axis=1)
urls = df['Access_URL']
#urls = ['http://pidila.gitlab.io/info-site/accessibilite.html']
for i, j in enumerate(urls):
    print(type(j))
    if type(j) != float:
        #url = j
        # j = j.strip('\'')
        url = j[2:len(j)-2]
        url = url.split(', ')
        print(url)
        file_name = str(i)
        path = os.path.join(os.path.abspath('.'), file_name)
        print(path)
        #check if it's downloaded
        if not os.path.exists(path):
            os.makedirs(path)
            for m, jj in enumerate(url):
                jj = jj.strip('\'')
                try:
                    ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
                    req = urllib.request.Request(jj, headers=ua_headers)
                    resp = urllib.request.urlopen(req)
                except:
                    df.iloc[i, 5] = 'NO'
                    continue
                df.iloc[i, 5] = 'YES'
                # open page with selenium
                options = webdriver.ChromeOptions()
                # prefs = {"profile.default_content_settings.popups" : 0, 'download.default_directory': path}
                # options.add_experimental_option('prefs', prefs)
                driver = webdriver.Chrome(executable_path='/Users/pascal/Downloads/chromedriver', chrome_options=options)
                driver.get(jj)
                action = ActionChains(driver).move_by_offset(0, 0).context_click().perform()
                pyautogui.typewrite(['e', 'enter'])
                time.sleep(2)
                pyautogui.typewrite(['enter'])
                time.sleep(10)
                driver.close()
                download_path = '/Users/pascal/Downloads'
                filelist = os.listdir(download_path)
                # print(filelist)
                for file in filelist:
                    #print(file)
                    if file[len(file)-3:len(file)] == 'htm':
                        src1 = os.path.join(download_path, file)
                        src2 = os.path.join(download_path, file[:len(file)-4] + '_files')
                        dst1 = os.path.join(path, file)
                        dst2 = os.path.join(path, file[:len(file)-4] + '_files')
                        print(src1)
                        print(dst1)
                        if os.path.exists(dst1):
                            dst1 = os.path.join(path, file[:len(file) - 4] + str(m) + '.htm')
                            dst2 = os.path.join(path, file[:len(file) - 4] + '_files' + str(m))
                            shutil.move(src1, dst1)
                            shutil.move(src2, dst2)
                        else:
                            shutil.move(src1, dst1)
                            shutil.move(src2, dst2)
        else:
            continue
df.to_excel('Acess_status.xlsx')