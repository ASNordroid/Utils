# Read new hackernews post and decide if I should read'em
import requests as rq
from bs4 import BeautifulSoup


def learn_my_taste():
    with open('C:\\Users\\Ant\\Desktop\\best.txt', 'rb') as my_taste_file:
        my_taste = my_taste_file.read().decode('utf-8')
    sentences = my_taste.split('\n')

    words = []
    for sentence in sentences:
        temp = [i.lower() for i in sentence.split()]
        for word in temp:
            s = ''
            if word.endswith('\'s') or word.endswith('’s'):
                word = word[:-2]
            for i in word:
                if i.isalnum():
                    s += i
            if len(s) > 1 and not s.isnumeric():
                words.append(s)

    print(words)

    # filter common words, same stuff, delete brackets and same
    # count number of prepared words in sentence for every new sentence
    # if found new is approved by me add words to best
    # if found new is not approved by me delete words from best (?)


def get_news():
    news_html = rq.get('https://news.ycombinator.com/newest').content

    soup = BeautifulSoup(news_html, "html.parser")
    junk = ["from?", "newest?", "item?"]

    all_td = soup.find_all("td", {"class": "title"})
    news_str = ''

    for tag in all_td:
        t = tag.find_all("a")
        for tg in t:
            if all(_ not in tg['href'] for _ in junk):
                news_str = news_str + tg.string + ' - ' + str(tg['href']) + '\n'

    with open('C:\\Users\\Ant\\Desktop\\news.txt', 'wb') as news_file:
        news_file.write(news_str.encode('utf-8'))

# get_news()
learn_my_taste()
