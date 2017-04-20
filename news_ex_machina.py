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

    # print(normalize(my_taste))
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
            news_file.write(i.encode())

    return news_str


def exclude_irrelevant_news(f_titles, key_words):
    relevant_news = []
    titles = [i.split(' - ')[0] for i in f_titles]
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

    # print(noisy_news)
    # print(good_news)
    return good_news


w = learn_my_taste()

all_news = get_news()
chosen_news = exclude_irrelevant_news(get_news(), w)

s1 = approve(all_news)
s2 = approve(chosen_news)

# precision = tp / (tp + fp)
tp = 0
for i in all_news:
    for j in chosen_news:
        if i == j:
            tp += 1
print()

# recall = tp / (tp + fn)
