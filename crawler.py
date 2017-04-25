# Get new hackernews post and decide if I should read'em
import requests as rq
from bs4 import BeautifulSoup


# filter common words, same stuff, delete brackets and same - DONE
# count number of prepared words in sentence for every new sentence - DONE
# if found new is approved by me add words to best
# if found new is not approved by me delete words from best (?)

# add rating for words: if line with this word is approved by me rating+=1, else -=1

# TODO: add ability to save new key words - ?


# function for deleting special symbols from string
def normalize(string):
    sentences = string.split('\n')
    words = []
    junk = ['the', 'for', 'of', 'as', 'you', 'your', 'in', 'on', 'be', 'by', 'is', 'are', 'am', 'to', 'or', 'and',
            'like', 'does', 'doesnt', 'not', 'have', 'should', 'never', 'been', 'it', 'do', 'at', 'their', 'an', 'with']

    for sentence in sentences:
        temp = sentence.lower().split()

        for word in temp:
            s = ''
            if word.endswith('\'s') or word.endswith('’s'):
                word = word[:-2]
            for letter in word:
                if letter.isalnum():
                    s += letter
            if len(s) > 1 and not s.isnumeric() and s not in junk:
                words.append(s)

    return words


def learn_my_taste():
    with open('C:\\Users\\Ant\\Desktop\\best.txt', 'rb') as my_taste_file:
        my_taste = my_taste_file.read().decode()

    # print(normalize(my_taste))
    return normalize(my_taste)


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

    with open('C:\\Users\\Ant\\Desktop\\news.txt', 'ab') as news_file:
        for n in news:
            news_file.write(n.encode())

    return news


def exclude_irrelevant_news(f_titles, key_words):
    relevant_news = []
    titles = [t.split(' - ')[0] for t in f_titles]
    print('t: ', titles)
    cou = 0
    for title in titles:
        t = normalize(title)
        rating = 0

        for i in t:
            if i in key_words:
                print(i, end='-')  # debug
                rating += 1
        print(rating)  # debug
        if rating > 0:
            relevant_news.append(f_titles[cou][:-1])
        cou += 1

    return relevant_news


def approve(noisy_news):
    good_news = []

    for n in noisy_news:
        print(n)
        if input() == 'y':
            good_news.append(n)

    return good_news


# w = learn_my_taste()

all_news = get_news()
print(all_news)
# chosen_news = exclude_irrelevant_news(all_news, w)
# print(chosen_news)
#
# s1 = approve(all_news)
# s2 = approve(chosen_news)
#
# tp = len(s2)
# fp = len(chosen_news) - tp
# precision = tp / (tp + fp)
# print('precision:', precision)

# fn = len(all_news) - len()
# recall = tp / (tp + fn)
