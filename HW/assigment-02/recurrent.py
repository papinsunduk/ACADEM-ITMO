from typing import Callable, Any
from common.debug.tracerec import visualize


def __recurrent(
        n: Any,
        stop_condition: Callable[[Any], bool],
        transform: Callable[[Any], Any],
        value: Callable[[Any], Any]
) -> Any:
    """Это вспомогательная функция, не надо ее менять"""
    if stop_condition(n):
        return n
    return __recurrent(transform(n), stop_condition, transform, value) + value(n)


def identity(n):
    """Вернуть число n, используя __recurrent"""
    return __recurrent(
        n,
        stop_condition=lambda x: x == 0,
        transform=lambda x: x-1,
        value=lambda x: 1
    )


def log2(n):
    """Вернуть округленный вниз двоичный логарифм n, используя __recurrent"""
    return __recurrent(
        n,
        stop_condition=lambda x: x == 0,
        transform=lambda x: x//2,
        value=lambda x: 0 if x == n else 1
    )


def push(n):
    """Вернуть массив, в котором единственное число 0 лежит на глубине n"""

    def __depth(item):
        """Вернуть глубину вложенного массива item"""
        depth = 1
        if isinstance(item[0], list):
            depth += __depth(item[0])
        return depth

    return __recurrent(
        n,
        stop_condition=lambda x: __depth([x]) == n+1,
        transform=lambda x: [0] if x == n else [x],
        value=lambda x: []
    )
