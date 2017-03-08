# Read new hackernews post and decide if I should read'em
import requests as rq
from bs4 import BeautifulSoup


def learn_my_taste():
    with open('C:\\Users\\Ant\\Desktop\\best.txt', 'rb') as my_taste_file:
        my_taste = my_taste_file.read().decode()
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
    l = 0  # temp, for testing
    save_page = ''

    while l < 3:
        l += 1
        links = []
        news_html = rq.get(next_page).content
        soup = BeautifulSoup(news_html, "html.parser")

        for tag in soup.find_all("td", {"class": "title"}):
            for tg in tag.find_all("a"):
                if all(_ not in tg['href'] for _ in junk):
                    links.append(tg.string + ' - ' + str(tg['href']) + '\n')

        # if next_page == 'https://news.ycombinator.com/newest':
        #     print(links[0])
        #     save_page = links[0]
        # else:
        #     with open('C:\\Users\\Ant\\Desktop\\news.txt', '+b') as news_file:
        #         temp = news_file.read().decode()
        #         print('tmp' + temp[0])
        #         load_page = temp[0]
        #         news_file.write(temp[1:].encode())
        #     for i in links:
        #         if load_page == i:
        #             print('broke')
        #             break

        next_page = 'https://news.ycombinator.com/' + links[-1].split(' - ')[1]
        news_str.append(links[:-1])
        print(next_page)
    for i in news_str:
        for j in i:
            print(j)

    # with open('C:\\Users\\Ant\\Desktop\\news.txt', 'rb') as news_file:
    #     temp = news_file.read().decode()
    # with open('C:\\Users\\Ant\\Desktop\\news.txt', 'wb') as news_file:
    #     save_page += temp
    #     news_file.write(save_page.encode())
    #     for i in news_str:
    #         for j in i:
    #             news_file.write(j.encode())

get_news()
learn_my_taste()
