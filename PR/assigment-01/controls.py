import math


def transpose(a):
    """Транспозиция матрицы"""
    aT = []
    for i in range(len(a[0])):
        s = []
        for j in a:
            s.append(j[i])
        aT.append(s)
    return aT


def read_lines(input, print):
    """Количество непустых строк во вводе до первой пустой"""
    s = input()
    c = 0
    while s:
        c += 1
        s = input()
    print(c)


def min_prime(n):
    """Минимальный простой делитель числа"""
    for i in range(2, n//2+1):
        if n % i == 0:
            return i
    return n


def from_hexadecimal(s):
    """Перевод из шестнадцатеричной системы счисления"""
    return int(s, 16)
