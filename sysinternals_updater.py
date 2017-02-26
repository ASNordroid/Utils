# Download SysinternalsSuite if newer version is out
import requests
import zipfile as zp


print (help(zp))
html = str(requests.get('https://technet.microsoft.com/ru-ru/sysinternals/bb842062').text)
# print(html)
for i in html:
    if 'Updated' in i:
        print(i)
file = zp.ZipFile()
file.extractall()
