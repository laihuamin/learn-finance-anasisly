# code: utf-8
import urllib2

import ssl
import requests
import cookielib
# import json

ssl._create_default_https_context = ssl._create_unverified_context

cookie = cookielib.CookieJar()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 Hexin_Gphone/9.58.07 (Royal Flush) hxtheme/1 innerversion/G037.08.296.1.32 userid/-440578591'
}


article_url = 'https://news.10jqka.com.cn/m604177678/'

article_url2 = 'https://api.xueqiu.com/statuses/show.json?_t=1MEIZUa649722081a9f5283f0ccc7a140f6e37.8350916862.1524781289394.1524781299289&_s=961787&card_addition=1&x=0.410&id=106055282&_src=ptl'

article_url3 = 'https://api.xueqiu.com/statuses/show.json?_t=1MEIZUa649722081a9f5283f0ccc7a140f6e37.8350916862.1524781289394.1524781418720&_s=d50344&card_addition=1&x=0.58&id=106115786&_src=ptl'
# req = urllib.Request(url=article_url2, headers=headers)
# response = urllib.urlopen(req)
# req = urllib2.Request(article_url)
# req.add_header('User-Agent','Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX5 Build/LMY47I)')
# response = urllib2.urlopen(req)
# html = response.read().decode('utf-8')
# print(html)
session = requests.Session()
session.headers = {
    'User-Agent': 'Xueqiu Android 10.5'
}
session.get('https://api.xueqiu.com')
r = session.get(article_url)
print r.text
