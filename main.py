import crawler
import database
import indexer


def __main__():
    while True:
        inp = input('> ')

        if inp == 'news':
            news = crawler.get_news()
            print(news)

__main__()