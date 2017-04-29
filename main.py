import crawler
import database as db
import indexer
import nlp


while True:
    inp = input('> ')

    if inp == 'news':
        w = nlp.learn_my_taste()
        all_news = crawler.get_news()

        chosen_news = nlp.exclude_irrelevant_news(all_news, w)
        for item in chosen_news:
            print(item)

        indexer.add_to_index(chosen_news)
        db.write_to_base(db.main_db, chosen_news)
    elif inp == 'search' or inp == 'src':
        found = []
        words_to_find = input('Enter key words: ').split()
        index = indexer.get_index()
        for i in index:
            if i in words_to_find:
                found.append(index[i])

        found_f = set(found[0])
        for key in range(1, len(found)):
            found_f = found_f & set(found[key])

        print(found_f)
        for i in list(found_f):
            print(db.get_by_id(i))

    elif inp == 'quit' or inp == 'q':
        break
    else:
        print('news - get news\nsearch - search for key words in saved news\nquit\n')
