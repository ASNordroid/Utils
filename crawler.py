import database
import requests as rq
from bs4 import BeautifulSoup


def get_stop_title():
    return database.read_from_base(database.save_db)


def save_stop_title(title):
    database.write_to_base(database.save_db, (title))


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
            title = tag.find_all('td', {"class": "title"})[1].a.string
            if any(('Ask HN: ', 'Show HN: ')) in title.split():
                link = comments
            else:
                link = tag.find_all('td', {"class": "title"})[1].a['href']
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
            save_stop_title(news[0])
            break

    return news
