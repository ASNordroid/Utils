import database as db


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
    taste = []

    headers = db.get_headers()
    for header in headers:
        taste += normalize(header[1])

    return taste


def exclude_irrelevant_news(f_titles, key_words):
    relevant_news = []
    titles = [_.split(' ^ ')[1] for _ in f_titles]
    cou = 0

    for title in titles:
        t = normalize(title)
        rating = 0

        for i in t:
            if i in key_words:
                rating += 1
        if rating > 0:
            relevant_news.append(f_titles[cou])
        cou += 1

    return relevant_news
