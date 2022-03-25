def increase_ints(s):
    """Увеличить на 1 только целые числа в множестве"""
    return {i+1 if type(i) == type(0) else i for i in s}


def weird_condition(a, b, x, y, z):
    """Довольно сомнительной адекватности условие (см. _legend.md)"""
    return all(i % x == 0 for i in a) and all(i % y == 0 for i in b) and (any(i % z == 0 for i in a) and all(i % z != 0 for i in b) or any(i % z == 0 for i in b) and all(i % z != 0 for i in a)) or all(len(i) == 0 for i in (a, b))


def index_of_median(a):
    """Индекс медианного значения массива"""
    return a.index(sorted(a)[len(a)//2])
