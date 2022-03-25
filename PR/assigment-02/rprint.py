def flatten(a):
    """Вернуть все числа, содержащиеся в массиве на любом уровне вложенности"""
    arr = []
    for i in a:
        if isinstance(i, int):
            arr.append(i)
        else:
            arr += flatten(i)
    return arr


def rprint(a, depth, current_depth=0):
    """Вернуть строковое представление массива, обрезав его по глубине depth"""
    st = '['
    if current_depth == depth:
        st += '...'
    else:
        for i in range(len(a)):
            if isinstance(a[i], list):
                st += rprint(a[i], depth, current_depth + 1) + ', '*(len(a[i:]) > 1)
            else:
                st += str(a[i]) + ', '*(len(a[i:]) > 1)
    st += ']'
    return st


# noinspection PyShadowingBuiltins
def pretty_rprint(a, current_depth=0, print=print):
    """Вывести массив, делая отступы, соответствующие уровню вложенности"""
    if all(not isinstance(k, list) for k in a):         # массив не имеет вложений
        print('    ' * current_depth, end='')
        print('[', *a, ']', end='')
    else:
        print('    ' * current_depth, '[', sep='', end='')
        for i in a:
            if isinstance(i, list):                     # элемент - массив
                print('\n', end='')
                pretty_rprint(i, current_depth + 1, print)
            else:                                       # перед нами число
                print('\n', '    ' * (current_depth + 1), i, sep='', end='')
        print('\n', '    ' * current_depth, ']', sep='', end='')

