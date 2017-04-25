import crawler
import database
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

            s1 = approve(all_news)
            s2 = approve(chosen_news)

            tp = len(s2)
            fp = len(chosen_news) - tp
            precision = tp / (tp + fp)
            print('precision:', precision)

            fn = len(all_news) - len()
            recall = tp / (tp + fn)

            database.write_to_base()
        # elif inp == 'search' or inp == 's':

__main__()