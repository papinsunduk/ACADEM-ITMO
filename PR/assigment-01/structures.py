def kth(a, k):
    """k-е по величине значение в массиве"""
    b = sorted(a)
    return a[a.index(b[k-1])]


def head_tail(a, k):
    """Первые и последние k элементов в массиве"""
    return a[:k]+a[::-1][:k][::-1]


def filter_sort(a, c):
    """Отсортировать копию массива, удалив строки с символом c"""
    b = [i for i in a if not(c in i)]
    return sorted(b)


def build_dict(keys, values):
    """Построить словарь по набору ключей и значений"""
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d


def compare_contents(a1, a2):
    """Проверка наборов элементов на совпадение"""
    flag = True
    for i in a1:
        if i not in a2:
            flag = False
    for i in a2:
        if i not in a1:
            flag = False
    return flag
