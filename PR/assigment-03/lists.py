def sum_some(numbers, indices):
    """
    Вернуть сумму элементов из numbers, на позициях, записанных в indices
    sum_some([1, 2, 3], [0, 1, 1]) -> 5 = (1+2+2)
    """
    return sum([numbers[i] for i in indices])


def replace_range(a, b, x, y):
    """
    Заменить подмассив массива a с индексами от x до y на массив b
    replace_range([1, 2, 3, 4], [7, 8, 9], 0, 1) -> [7, 8, 9, 3, 4]
    """
    return a[:x] + b + a[y+1:]


def sum_list(a):
    """
    Рекурсивно просуммировать элементы массива a
    sum_list([1, 2, 3]) -> 6
    """
    if not a:
        return 0
    if len(a) == 1:
        return a[0]
    return a[0] + sum_list(a[1:])


def signs(a):
    """
    Расставьте между элементами массива a знаки отношений "меньше", "равно" или "больше"
    signs([2, 8, 4, 4]) -> [2, '<', 8, '>', 4, '=', 4]
    """
    m = []
    for i in range(len(a)-1):
        diff = a[i] - a[i+1]
        if diff > 0:
            m.append('>')
        elif diff < 0:
            m.append('<')
        else:
            m.append('=')
    return list(sum(zip(a, m), ())) + [a[-1]]
