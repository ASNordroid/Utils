import database as db
import nlp

# TODO: get all words
# TODO: for every word find


def get_all_words():
    headers = db.get_headers()

    for header in headers:
        header_words = nlp.normalize(header)