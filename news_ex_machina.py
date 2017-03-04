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
    next_page = 'https://news.ycombinator.com/newest'
    news_str = []
    junk = ["from?", "item?"]
    i = 0
    while next_page != '' and i < 3:
        i += 1
        news_html = rq.get(next_page).content

        tt = []

        soup = BeautifulSoup(news_html, "html.parser")

        for tag in soup.find_all("td", {"class": "title"}):
            t = tag.find_all("a")
            for tg in t:
                if all(_ not in tg['href'] for _ in junk):
                    tt.append(tg.string + ' - ' + str(tg['href']) + '\n')

        next_page = 'https://news.ycombinator.com/' + tt[-1].split(' - ')[1]
        news_str.append(tt[:-1])
        print(next_page)
    for i in news_str:
        for j in i:
            print(j)

    # with open('C:\\Users\\Ant\\Desktop\\news.txt', 'wb') as news_file:
    #     news_file.write(news_str.encode('utf-8'))

get_news()
learn_my_taste()
