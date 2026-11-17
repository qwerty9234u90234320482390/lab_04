"""Варіант 11: задача про сходинки (кроки 1, 2 або 3).

ways(n) — кількість способів піднятися на n сходинок.
Базові випадки: ways(0) = 1 (порожня послідовність кроків), ways(n < 0) = 0.
Рекурсивний крок: ways(n) = ways(n-1) + ways(n-2) + ways(n-3).
"""

from __future__ import annotations

from functools import lru_cache

STEPS: tuple[int, ...] = (1, 2, 3)


def _check(n: int) -> None:
    if n < 0:
        raise ValueError("кількість сходинок має бути невід'ємною")


def stairs_naive(n: int) -> int:
    """Наївна рекурсія: експоненційна складність, повторює підзадачі."""
    _check(n)
    return _naive(n)


def _naive(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return _naive(n - 1) + _naive(n - 2) + _naive(n - 3)


@lru_cache(maxsize=None)
def _memo(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return _memo(n - 1) + _memo(n - 2) + _memo(n - 3)


def stairs_memo(n: int) -> int:
    """Рекурсія з lru_cache: O(n) часу, глибина стека O(n)."""
    _check(n)
    return _memo(n)


def stairs_iter(n: int) -> int:
    """Ітеративна версія (динамічне програмування): O(n) часу, O(1) пам'яті.

    Безпечніша за рекурсію для великих n — не залежить від ліміту стека.
    """
    _check(n)
    a, b, c = 0, 0, 1  # ways(-2), ways(-1), ways(0)
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return c


def cache_stats() -> str:
    """Рядок зі статистикою кешу мемоізованої версії."""
    return str(_memo.cache_info())


def clear_cache() -> None:
    """Очищає кеш мемоізованої версії."""
    _memo.cache_clear()
