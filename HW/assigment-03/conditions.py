
'''Взять текст какой-нибудь детской сказки и положить его в файл. Написать программу, которая будет читать его из файла
и выводить статистику, а именно:
самые часто повторяющиеся слова (без учёта регистра, “носорог” и “Носорог” считать одним словом)
самое длинное предложение
среднее кол-во знаков препинания в предложении'''

signs = ['.', ',', '?', '!', ':', ';', '~', '-', '«', '»', '—']
EOS = ['.', '?', '!', '~', '-']

with open('./random_text.txt', encoding='utf-8') as f:

    text = f.read()
    lines = text.split('\n')
    text = ' '.join(lines)
    # text = text.replace('\n', ' ')  # избавляемся от переносов строк для удобства работы
    text = text.replace('...', '~')  # заменяем многоточия (3 символа) на 1 символ для удобства работы
    sentences = [text.split(i) for i in EOS][0]
    # print(text)

    i = 1
    beginning, end, length = 0, 0, 0
    maxSentence = ''
    signCount = []
    while i < len(text):
        if text[i].isupper() and text[i-2] in EOS:
            end = i - 2
            if end - beginning > length:
                maxSentence = text[beginning:end + 1]
                signCount.append(sum([text[beginning:end + 1].count(i) for i in signs]))
                beginning = end + 2
                i = end - 1
        i += 1

    print(f'Самое длинное предложение: {maxSentence}')
    print(f'Среднее количество знаков в предложении: {sum(signCount) / len(sentences)}')

    for i in signs:
        text = text.replace(i, ' ')  # убираем знаки препинания
    words = text.split()
    words = [i.lower() for i in words]  # преобразуем к одному регистру
    wCount = 0
    mostWord = ''
    for i in words:
        count = words.count(i)
        if count > wCount:
            wCount = count
            mostWord = i

    print(f'Самое часто встречающееся слово: {mostWord}')