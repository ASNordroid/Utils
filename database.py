main_db = 'C:\\Users\\Ant\\PycharmProjects\\hackernews-reader\\base.txt'
save_db = 'C:\\Users\\Ant\\PycharmProjects\\hackernews-reader\\save.txt'
index_db = 'C:\\Users\\Ant\\PycharmProjects\\hackernews-reader\\index.txt'


def read_from_base(db_name):
    articles = []
    with open(db_name, 'rb') as file:
        for line in file:
            articles.append(line.decode())

    return articles


def write_to_base(db_name, items):
    if db_name == main_db:
        items.reverse()
    with open(db_name, 'ab') as file:
        for i in items:
            file.write(i.encode())


def get_headers():
    headers = []
    news = read_from_base(main_db)

    for line in news:
        headers.append((line.split(' ^ ')[0], line.split(' ^ ')[1]))

    return headers


def get_by_id(article_id):
    articles = read_from_base(main_db)
    for i in articles:
        if article_id == i.split(' ^ ')[0]:
            return i