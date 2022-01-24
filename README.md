# kuji_rakuten

https://rakucoin.appspot.com/rakuten/kuji/

```
% pip install chromedriver-binary==YOUR CHROME VERISON
```

edit code bellow

```
# 楽天会員ログイン情報
EMAIL = ""
PASSWORD = ""
```

do

```
% python kuji.py
```

update list example

```
import urllib.request
from bs4 import BeautifulSoup

url = 'https://rakucoin.appspot.com/rakuten/kuji/'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req)
bs = BeautifulSoup(html, "html.parser")
aa = bs.find_all('a')
for a in aa:
    str = "{'url':'" + a.get('href') + "','name':'" + a.text + "'},"
    print(str)

```
