# Download SysinternalsSuite if newer version is out
import os
import time
import datetime
import requests as rq
import zipfile as zp


def download_and_extract():
    zip_file = rq.get('https://download.sysinternals.com/files/SysinternalsSuite.zip').content
    extracted_file = zp.ZipFile(zip_file).extractall()

html = rq.get('https://technet.microsoft.com/ru-ru/sysinternals/bb842062').text

# get update date from site
start = html.find('Updated:') + 9
end = start + html[start:start + 40].find('<')
time_of_site_upd = datetime.datetime.strptime(html[start:end], "%B %d, %Y").date()

# get update date of local files
local_time = os.path.getmtime('C:\\Users\\Ant\\Desktop\\SysinternalsSuite')
time_of_local_upd = datetime.datetime.strptime(time.ctime(local_time), "%a %b %d %H:%M:%S %Y").date()

if time_of_site_upd > time_of_local_upd:
    print("1")
else:
    print("No newer version. :(")
