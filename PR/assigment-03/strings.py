def reverse(s):
    """
    Вернуть исходную строку, записанную наоборот
    reverse('abc') -> 'cba'
    """
    return s[::-1]


def swap_case(s):
    """
    Заменить регистр каждого символа, входящего в строку, на противоположный
    swap_case('Hello world') -> 'hELLO WORLD'
    """
    return s.swapcase()


def censor_words(s, blacklist):
    """
    Вернуть исходную строку, в которой слова из blacklist заменены на звездочки
    censor_words('hello world', ['hello']) -> '***** world')
    """
    m = s
    for i in blacklist:
        if i in m:
            m = m.replace(i, '*' * len(i))
    return m


def remove_duplicates(s):
    """
    Удалить идущие подряд повторы слов в строке
    remove_duplicates('hello nice nice world hello') -> 'hello nice world hello'
    """
    words = s.split()
    out = [words[0]]
    for i in range(1, len(words)):
        if words[i] != words[i-1]:
            out.append(words[i])
    return ' '.join(out)


def parentheses(s):
    """
    Проверить, закрыты ли все пары круглых скобок в строке
    parentheses( '(abc(1+2))' )    -> True
    parentheses( '(lalala' )       -> False - скобка не закрыта
    parentheses( '(hello)world)' ) -> False - слишком много закрывающих скобок
    """
    summ = 0
    for i in s:
        if i == '(':
            summ += 1
        elif i == ')':
            summ -= 1
        if summ < 0:
            return False
    return summ == 0

