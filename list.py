import urllib.request
import urllib.error
import re
import pandas as pd

file1 = open('listesitesaccessibles.txt')
file2 = open('listesitesaccessibles1.txt')
url_list = []
for i in file1:
    if len(i) > 3:
        url_list.append(i[:len(i)-2])
for i in file2:
    if len(i) > 3:
        if i not in url_list:
            url_list.append(i[:len(i)-2])
print(url_list)
for i in url_list:
    req = urllib.request.Request(i)
    try:
        resp = urllib.request.urlopen(req)
        content = resp.read().decode('utf-8')
        # print(content)
        res = r"<a.*?href=.*?<\/a>"
        mm = re.findall(res, content, re.S | re.M)
        print(mm)
        urls = []
        for i in mm:
            if i.find('Access') != -1:
                urls.append(re.search(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", i, re.I | re.S | re.M))
        print(urls)
    except urllib.error.HTTPError as e:
        print(e.code)
