# Read new hackernews post and decide if I should read'em
import requests as rq
from bs4 import BeautifulSoup

def learn_my_taste():
    with open('C:\\Users\\Ant\\Desktop\\best.txt', 'rb') as my_taste_file:
        #my_taste_file.encoding('utf-8')
        my_taste = my_taste_file.read()
    print(my_taste)


# HN_site = 'https://news.ycombinator.com/newest'
# news_html = rq.get(HN_site).content
# news_file = open('C:\\Users\\Ant\\Desktop\\news.txt', 'wb')
# junk = ["from?", "newest?", "item?"]
# soup = BeautifulSoup(news_html, "html.parser")
#
# all_td = soup.find_all("td", {"class": "title"})
# news_str = ""
#
# for tag in all_td:
#     t = tag.find_all("a")
#     for tg in t:
#         if all(_ not in tg['href'] for _ in junk):
#             news_str = news_str + tg.string + ' - ' + str(tg['href']) + '\n'
#
# news_file.write(news_str.encode('utf-8'))
# news_file.close()

learn_my_taste()