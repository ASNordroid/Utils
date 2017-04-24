import crawler

base = r'C:\Users\Ant\PycharmProjects\Utils\base.txt'


def read_from_base(file_name):
    with open(file_name) as file:
        for line in file.readlines():
            articles = {}

            header = line.split(' - ')[0]
            properties = line.split(' - ')[1].split()

            articles[header] = properties
    return articles


def write_to_base(header, properties):
    with open(base, 'a') as file:
        file.write(header + ' - ' + properties)

# def is_in_base(header):