def calculate(input_str):
    """Вычислить выражение, представленное в виде строки"""
    inp = input_str.split()
    for i in inp:
        if all(j.isnumeric() for j in i.split('.')):
            inp[inp.index(i)] = float(i)
    while any(i in inp for i in ['/', '*']):
        if '/' in inp:
            ind = inp.index('/')
            div = True
        else:
            ind = inp.index('*')
            div = False
        a, b = inp.pop(ind - 1), inp.pop(ind)
        if div:
            inp[ind - 1] = a / b
        else:
            inp[ind - 1] = a * b

    while any(i in inp for i in ['+', '-']):
        if '+' in inp:
            ind = inp.index('+')
            add = True
        else:
            ind = inp.index('-')
            add = False
        a, b = inp.pop(ind - 1), inp.pop(ind)
        if add:
            inp[ind - 1] = a + b
        else:
            inp[ind - 1] = a - b

    return round(inp[0], 2)

