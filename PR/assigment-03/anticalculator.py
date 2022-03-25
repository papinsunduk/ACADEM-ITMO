def anti_calculate(x, n):
    """Разложить число на выражение из знаков 'плюс', 'минус', 'умножить'"""
    if n == 0:
        return str(x)
    from random import randint
    signs = [randint(0, 2)] * (n > 1) + [randint(0, 1) for i in range(n-2)]
    prom = randint(0, 100)
    out = str(prom)
    for i in signs:
        a = randint(0, 100)
        if i == 2:  # повезло-повезло
            out += ' * ' + str(a)
            prom *= a
        elif i == 1:
            prom -= a
            out += ' - ' + str(a)
        else:
            prom += a
            out += ' + ' + str(a)
    if prom > x:
        out += ' - ' + str(prom - x)
    else:
        out += ' + ' + str(-prom + x)
    return out
