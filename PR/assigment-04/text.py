def read_all(filename):
    """Вернуть содержимое текстового файла filename как строку."""
    return open(filename).read()


def sum_two(filename):
    """Прочитать первые два числа из текстового файла и вернуть их сумму."""
    return sum([int(i) for i in open(filename).read().split() if i.lstrip('-').isnumeric()][0:2])


def longest_line(filename):
    """Вернуть номер самой длинной строки текстового файла. Нумерация начинается с единицы."""
    with open(filename) as f:
        length, maxlen, ind = sum(1 for _ in f), 0, 1
        f.seek(0)
        for i in range(length):
            s = f.readline().rstrip('\n')
            if len(s) > maxlen:
                maxlen, ind = len(s), i + 1
    return ind


def random_access(filename, n):
    """Вернуть n-ый символ текстового файла. Нумерация с единицы"""
    return open(filename).read()[n-1] if 0 < n <= len(open(filename).read()) else ''


def alphabet(filename, n):
    """Вывести n первых заглавных букв латинского алфавита в текстовый файл."""
    with open(filename, 'w') as f:
        for i in range(65, 65 + min(26, n)):
            f.write(chr(i))
