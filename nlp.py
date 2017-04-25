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
