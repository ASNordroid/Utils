from collections import defaultdict

import database as db
import nlp


def get_index():
    index = defaultdict(list)
    headers = db.get_headers()
    print(headers)

    for header in headers:
        header_words = nlp.normalize(header[1])

        for word in header_words:
            index[word].append(header[0])

    return index
