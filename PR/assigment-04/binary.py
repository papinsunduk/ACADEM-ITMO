def bin_sum_two(filename):
    """
    Из бинарного файла filename прочитать два первых числа и вернуть их сумму.
    Оба числа имеют тип int и закодированы строго четырьмя байтами.
    """
    with open(filename, 'rb') as f:
        return int.from_bytes(f.read(4), byteorder='big', signed=True) + int.from_bytes(f.read(4), byteorder='big', signed=True)


def find_person(filename, identifier):
    """Найти человека по id в базе указанной структуры (см. _legend.md)"""
    with open(filename, 'rb') as f:
        n = int.from_bytes(f.read(4), byteorder='big')
        for i in range(n):
            iD = int.from_bytes(f.read(4), byteorder='big')
            nI = int.from_bytes(f.read(4), byteorder='big')
            initials = f.read(nI).decode('utf-8')
            if iD == identifier:
                return initials
