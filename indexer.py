from collections import defaultdict

import database as db
import nlp


def add_to_index(headers):
    index = get_index()
    if index == {}:
        index = defaultdict(list)

    for header in headers:
        header_words = nlp.normalize(header.split(' ^ ')[1])

        for word in header_words:
            index[word].append(header.split(' ^ ')[0])

    index_lst = []
    for x in index:
        if type(x) is not list:
            index_lst.append(x + ' ^ ' + ' '.join(index[x]) + '\n')

    db.write_to_base(db.index_db, index_lst)


def get_index():
    index = defaultdict(list)
    raw = db.read_from_base(db.index_db)

    for item in raw:
        header = item.split(' ^ ')
        index[header[0]] = header[1].split()

    return index
