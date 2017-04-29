import crawler
import database as db
import indexer
import nlp


def approve(noisy_news):
    good_news = []

    for n in noisy_news:
        print(n)
        if input() == 'y':
            good_news.append(n)

    return good_news


def __main__():
    while True:
        inp = input('> ')

        if inp == 'news':
            w = nlp.learn_my_taste()
            all_news = crawler.get_news()
            print(all_news)

            chosen_news = nlp.exclude_irrelevant_news(all_news, w)
            print(chosen_news)

            indexer.add_to_index(chosen_news)
            db.write_to_base(db.main_db, chosen_news)
        elif inp == 'search' or inp == 'src':
            found = {}
            words_to_find = input('Enter key words: ').split()
            index = indexer.get_index()
            for i in index:
                if i in words_to_find:
                    found[i] = index[i]

            for f in found:
                print(f)

        elif inp == 'quit' or inp == 'q':
            return
        else:
            print('news - get news\nsearch - search for key words in saved news\nquit\n')

__main__()