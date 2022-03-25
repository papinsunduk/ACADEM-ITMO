import math


def triangle(a, b, c):
    s = a + b + c
    b = s - max(a, b, c) > max(a, b, c)
    return b


def divide(n, k):
    """Разбиение на равные части"""
    return n // k * k


def add_float(x, y):
    """Сложение не более, чем десятичных, дробных чисел"""
    return round(x + y, 1)


def distance(x1, x2):
    """Расстояние между точками"""
    return abs(x2 - x1)


def compare_power(x1, d1, x2, d2):
    """Сравнение степеней"""
    if x1 ** d1 < x2 ** d2:
        return -1
    elif x1 ** d1 == x2 ** d2:
        return 0
    else:
        return 1
