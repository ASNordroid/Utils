# Get new hackernews post and decide if I should read'em
import database
import requests as rq
from bs4 import BeautifulSoup


# if found new is approved by me add words to best
# if found new is not approved by me delete words from best (?)

# add rating for words: if line with this word is approved by me rating+=1, else -=1


def get_stop_title():
    db = database.read_from_base(database.main_db)
    print(db)
    if db != '':
        return db[-1].split(' ^ ')[1]
    else:
        return 'hello'


# def save_stop_title():



def get_news():
    next_page = 'https://news.ycombinator.com/newest'
    stop = get_stop_title()
    news = []
    depth = 0
    max_depth = 8

    while depth < max_depth:
        depth += 1
        soup = BeautifulSoup(rq.get(next_page).content, 'html.parser')

        for tag in soup.find_all('tr', {'class': 'athing'}):
            entry_id = tag['id']
            comments = 'https://news.ycombinator.com/item?id=' + entry_id
            link = tag.find_all('td', {"class": "title"})[1].a['href']
            title = tag.find_all('td', {"class": "title"})[1].a.string
            rating = tag.next_sibling.find('td', {'class': 'subtext'}).find_all('span')[0].string
            timestamp = tag.next_sibling.find('td', {'class': 'subtext'}).find_all('span')[1].string
            num_of_comm = tag.next_sibling.find('td', {'class': 'subtext'}).find_all('a')[-1].string
            if num_of_comm == 'discuss':
                num_of_comm = '0 comments'

            news_item = entry_id + ' ^ ' + title + ' ^ ' + ' '.join((comments, link, num_of_comm, timestamp, rating)) + '\n'
            if title != stop:
                news.append(news_item)
            else:
                next_page = 'false'
                break

        if next_page != 'false':
            next_page = 'https://news.ycombinator.com/' + soup.find('a', {'class': 'morelink'})['href']
        else:
            database.write_to_base((news[0]))
            break

    return news
