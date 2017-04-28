main_db = 'C:\\Users\\Ant\\PycharmProjects\\hackernews-reader\\base.txt'
best_db = 'C:\\Users\\Ant\\PycharmProjects\\hackernews-reader\\best.txt'


def read_from_base(db_name):
    articles = []
    with open(db_name, 'rb') as file:
        for line in file:
            articles.append(line.decode())

    return articles


def write_to_base(news):
    with open(main_db, 'ab') as file:
        for i in news:
            file.write(i.encode())


def get_headers():
    headers = []
    news = read_from_base(main_db)

    for line in news:
        headers.append((line.split(' ^ ')[0], line.split(' ^ ')[1]))

    return headers

# def is_in_base(header):