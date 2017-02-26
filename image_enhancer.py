# Enhance image resolution by downloading from iqdb.org image search (and analogues)
import requests
import os
from bs4 import BeautifulSoup


def send_image(file):
    request = requests.post('http://iqdb.org/', files={'file': open(file, 'rb')})
    return request.text


def download(*links):
    for i in links:
        new_img_html = requests.get(i)
        soup_new = BeautifulSoup(new_img_html, 'html.parser')

# def get_google():
# def get_tineye():
# def get_zerochan():
# def get_danbooru():


source_folder = 'C:\\Users\\Ant\\Desktop\\test\\'

for image_file in os.listdir(source_folder):
    print(image_file)
    html_doc = send_image(source_folder + image_file)

    soup = BeautifulSoup(html_doc, 'html.parser')
    global_div = soup.find('div', {'class': 'pages'})
    arr = []
    links = []
    for nested_div in global_div.children:
        for i in BeautifulSoup(str(nested_div), 'html.parser').find_all(['th', 'td', 'a']):
            if i.name == 'a':
                if 'http:' in i['href']:
                    links.append(i['href'])
                else:
                    links.append('http:' + i['href'])
            else:
                #for _ in i.strings:
                    arr.append(i.string)

    arr = arr[3:] # delete info about old picture
    # for t in range(len(arr)):
    #     print(arr[t])
    #     if (t+1) % 5 == 0: print()
    print(arr)

    html_f = 'C:\\Users\\Ant\\Desktop\\'
    with open(html_f + image_file + '.html', 'wb') as ht:
        ht.write(soup.prettify().encode('utf-8'))