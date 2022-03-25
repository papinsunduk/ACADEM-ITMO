def twice(fun, arg):
    """Вернуть результат применения функции fun дважды к аргументу arg"""
    return fun(fun(arg))


def foreach(funs, items):
    """Применить функции из массива funs к соответствующим элементам массива items"""
    return [funs[i](items[i]) for i in range(len(items))]


def apply(fun, args, kwargs):
    """Вернуть результат вызова функции fun с переданными позиционными и именными аргументами"""
    return fun(*args, **kwargs)


def all_ternary(n):
    """Вернуть все троичные числа длины n в алфавитном порядке"""
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1', '2']
    return [i + j for i in ['0', '1', '2'] for j in all_ternary(n-1)]


def swap_arguments(fun):
    """Вернуть функцию, принимающую аргументы в противоположном от fun порядке"""
    return lambda x, y: fun(y, x)
