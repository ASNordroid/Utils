import crawler

main_db = 'C:\\Users\\Ant\\PycharmProjects\\Utils\\base.txt'
best_db = 'C:\\Users\\Ant\\PycharmProjects\\Utils\\best.txt'


def read_from_base(file_name):
    with open(file_name) as file:
        for line in file.readlines():
            articles = {}

            header = line.split()[0]
            properties = line.split()[1].split()

            articles[header] = properties

    return articles


def write_to_base(news):
    with open(main_db, 'a') as file:
        for i in news:
            file.write(i.encode())

# def is_in_base(header):