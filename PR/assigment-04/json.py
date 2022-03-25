import json


def save_color(color, filename):
    """Сохранить цвет в файл в формате JSON (см. _legend.md)"""
    with open(filename, 'w') as f:
        f.write('{"r": %d, "g": %d, "b": %d, "a": %.1f}' % (color["r"], color["g"], color["b"], color["a"]))


def load_color(filename):
    """Вернуть цвет, записанный в JSON-файле"""
    with open(filename) as f:
        return json.load(f)


def links(filename):
    """Вывести все страницы из JSON-структуры и подсчитать количество ссылок на каждую. (см. legend)"""
    with open(filename) as f:
        content = json.load(f)['websites']
        sites, lnks = [], []
        for i in content:
            sites += [i['url']]
            lnks += i['links']
        return [(i, lnks.count(i)) for i in set(sites + lnks)]
