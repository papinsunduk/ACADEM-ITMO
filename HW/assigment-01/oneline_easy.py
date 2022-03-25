def square_sum(a):
    """Сумма квадратов элементов"""
    return sum([i**2 for i in a])


def print_dividing(a, b, t, print):
    """Все числа от a до b, делящиеся на t, через пробел"""
    print(*[i for i in range(a, b+1) if i % t == 0], end='')


def shuffle_lists(a, b):
    """Перемешать массивы в порядке чередования"""
    return list(sum(zip(a, b), ()))
