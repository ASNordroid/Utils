# Get new hackernews post and decide if I should read'em
import database
import requests as rq
from bs4 import BeautifulSoup


# if found new is approved by me add words to best
# if found new is not approved by me delete words from best (?)

# add rating for words: if line with this word is approved by me rating+=1, else -=1


def get_next_page():
    stop = database.read_from_base(database.base)


def get_news():
    next_page = 'https://news.ycombinator.com/newest'
    news = []
    l = 0

    while l < 1:
        l += 1
        soup = BeautifulSoup(rq.get(next_page).content, 'html.parser')

        for tag in soup.find_all('tr', {'class': 'athing'}):
            comments = 'https://news.ycombinator.com/item?id=' + tag['id']
            link = tag.find_all('td', {"class": "title"})[1].a['href']
            title = tag.find_all('td', {"class": "title"})[1].a.string
            rating = tag.next_sibling.find('td', {'class': 'subtext'}).find_all('span')[0].string
            timestamp = tag.next_sibling.find('td', {'class': 'subtext'}).find_all('span')[1].string
            num_of_comm = tag.next_sibling.find('td', {'class': 'subtext'}).find_all('a')[-1].string
            if tag.next_sibling.find('td', {'class': 'subtext'}).find_all('a')[-1].string == 'discuss':
                num_of_comm = '0 comments'

            news.append(' '.join((title, comments, link, num_of_comm, timestamp, rating)) + '\n')

    return news