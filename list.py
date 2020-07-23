import urllib.request
import urllib.error
import re
import pandas as pd
import chardet
from socket import error as SocketError

file1 = open('listesitesaccessibles.txt')
file2 = open('listesitesaccessibles1.txt')
file3 = open('listeGouvFr.txt')
# extract all the url
url_list = []
for i in file1:
    if len(i) > 3:
        url_list.append('http://' + i[:len(i) - 2])
for i in file2:
    if len(i) > 3:
        if i not in url_list:
            url_list.append('http://' + i[:len(i) - 1])
for i in file3:
    if len(i) > 3:
        if i not in url_list:
            url_list.append(i[:len(i) - 1])
print(url_list)
# url_list = ['https://www.telecom.gouv.fr']
# dataframe
df = pd.DataFrame(columns=['URL', 'Existence', 'Accessbilité', 'Access_URL', 'Commentaire'])
df['URL'] = url_list
# test all the url and write result in dataframe
for i, j in enumerate(url_list):
    print(i, j)
    try:
        ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        req = urllib.request.Request(j, headers=ua_headers)
        resp = urllib.request.urlopen(req)
        df.iloc[i, 1] = 'YES'
        content = resp.read()
        code = chardet.detect(content)['encoding']
        print(code)
        try:
            content = content.decode(code)
            # content = content.decode('utf-8')
        except:
            content = content.decode('utf-8', errors="replace")
        # print(content)
        res = r"<a.*?href=.*?<\/a>"
        mm = re.findall(res, content, re.S | re.M)
        urls = []
        for m in mm:
            if m.find('Access') != -1:
                try:
                    # pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                    # url = re.findall(r'<a href="([a-zA-z]+://[^\s]*)"', m)
                    url = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", m, re.I | re.S | re.M)
                    # print(m)
                    if url[0][0] == '/':
                        print(j + url[0])
                        urls.append(j + url[0])
                    elif url[0][0:3] == 'http':
                        urls.append(url[0])
                    else:
                        urls.append(j + '/' + url[0])
                except:
                    df.iloc[i, 2] = 'INVALID'
                    continue
        if len(urls) > 0:
            df.iloc[i, 2] = 'YES'
            df.iloc[i, 3] = urls
        else:
            df.iloc[i, 2] = 'NO'
        print(urls)
    except urllib.error.HTTPError as e:
        print(e.code)
        df.iloc[i, 1] = 'NO'
        df.iloc[i, 4] = e
    except urllib.error.URLError as e:
        print(e)
        df.iloc[i, 1] = 'NO'
        df.iloc[i, 4] = e
    except SocketError as e:
        print(e)
        df.iloc[i, 1] = 'NO'
        df.iloc[i, 4] = e
    # print(df)
    continue
df.to_excel('Output1.xlsx')