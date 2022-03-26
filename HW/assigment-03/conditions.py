def median(a, b, c):
    """
    Вернуть медиану из трех элементов
    median(2, 5, 3) -> 3
    """
    if a + b + c - min(a, b, c) - max(a, b, c) == a:
        return a
    elif b != max(a, b, c) and b != min(a, b, c):
        return b
    else:
        return c


def get_or_none(a, index):
    """
    Вернуть a[index], если он существует, иначе None
    get_or_none([1, 2, 3], 2) -> 2
    get_or_none([1, 2], 2)    -> None
    """
    if -len(a) <= index < len(a):
        return a[index]
    return None


def is_power_of_two(x):
    """
    Вернуть, является ли x степенью двойки
    is_power_of_two(8) -> True
    is_power_of_two(0) -> False
    """
    s = bin(x)
    return s.count('1') == 1 and x > 0


def is_monotonic(a, b, c):
    """
    Проверить, является ли [a, b, c] строго монотонной последовательностью
    is_monotonic(1, 2, 3) -> True
    is_monotonic(9, 5, 4) -> True
    is_monotonic(6, 7, 6) -> False
    """
    return a > b > c or a < b < c


def inline_if(a, b, condition):
    """
    Вернуть a, если condition == True, и b иначе.
    inline_if(1, 2, False) -> 2
    """
    return a if condition else b
