# Get new hackernews post and decide if I should read'em
import requests as rq
from bs4 import BeautifulSoup


# filter common words, same stuff, delete brackets and same - DONE
# count number of prepared words in sentence for every new sentence - DONE
# if found new is approved by me add words to best
# if found new is not approved by me delete words from best (?)


# function for deleting special symbols from string
def normalize(string):
    sentences = string.split('\n')
    words = []
    junk = ['the', 'for', 'of', 'as', 'you', 'your', 'in', 'on', 'be', 'by', 'is', 'are', 'am', 'to', 'or', 'and',
            'like', 'does', 'doesnt', 'not', 'have', 'should', 'never', 'been', 'it', 'do', 'at', 'their', 'an', 'with']

    for sentence in sentences:
        temp = [i.lower() for i in sentence.split()]

        for word in temp:
            s = ''
            if word.endswith('\'s') or word.endswith('’s'):
                word = word[:-2]
            for i in word:
                if i.isalnum():
                    s += i
            if len(s) > 1 and not s.isnumeric() and s not in junk:
                words.append(s)

    return words


def learn_my_taste():
    with open('C:\\Users\\Ant\\Desktop\\best.txt', 'rb') as my_taste_file:
        my_taste = my_taste_file.read().decode()

    print(normalize(my_taste))
    return normalize(my_taste)


def get_news():
    next_page = 'https://news.ycombinator.com/newest'
    news_str = []
    # news_file = open('C:\\Users\\Ant\\Desktop\\news.txt', 'rb')
    l = 0  # debug
    c1 = 0  # debug

    while l < 3:
        l += 1
        links = []
        soup = BeautifulSoup(rq.get(next_page).content, "html.parser")

        for tag in soup.find_all("td", {"class": "title"}):
            for tg in tag.find_all("a"):
                if "from?" not in tg['href']:
                    if "item?" in tg['href']:
                        links.append(tg.string)
                    else:
                        links.append(tg.string + ' - ' + str(tg['href']))
        c = 0
        for tag in soup.find_all("span", {"class": "age"}):
            links[c] += ' - ' + 'https://news.ycombinator.com/' + str(tag.find('a')['href']) + '\n'
            c += 1

        # if next_page != 'https://news.ycombinator.com/newest':
        #     temp = news_file.read().decode().split('\n')
        #     print('tmp: ' + temp[len(temp) - 89])  # debug
        #     for i in links:
        #         if temp[len(temp) - 89] == i:
        #             news_file.close()
        #             print('broke')  # debug
        #             break

        next_page = 'https://news.ycombinator.com/' + links[-1].split(' - ')[1]
        for i in links[:-1]:
            news_str.append(i)

    #     print(next_page)  # debug
    # for i in news_str:
    #     for j in i:
    #         c1 += 1
    #         print(c1, j)  # debug

    with open('C:\\Users\\Ant\\Desktop\\news.txt', 'ab') as news_file:
        for i in news_str:
            # for j in i:
            news_file.write(i.encode())

    return news_str


def exclude_irrelevant_news(f_titles, key_words):
    relevant_news = []
    titles = [i.split(' - ')[0] for i in f_titles]
    print('t: ', titles)
    cou = 0
    for title in titles:
        t = normalize(title)

        print(t)
        rating = 0
        for i in t:
            if i in key_words:
                rating += 1

        if rating > 0:
            relevant_news.append(f_titles[cou][:-1])
        cou += 1
    return relevant_news


w = learn_my_taste()
print(get_news())
print(exclude_irrelevant_news(get_news(), w))
