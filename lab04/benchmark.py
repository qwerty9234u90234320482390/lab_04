"""Порівняння часу: naive / memoized / iterative для задачі про сходинки."""

from __future__ import annotations

import sys
from time import perf_counter
from typing import Callable

from stairs import cache_stats, clear_cache, stairs_iter, stairs_memo, stairs_naive


def timeit(fn: Callable[[int], int], n: int, repeat: int = 1) -> float:
    """Повертає середній час виконання fn(n) у мілісекундах."""
    start = perf_counter()
    for _ in range(repeat):
        fn(n)
    return (perf_counter() - start) / repeat * 1000


def memo_cold(n: int) -> int:
    clear_cache()
    return stairs_memo(n)


def run(sizes: tuple[int, ...] = (10, 15, 20, 25, 30)) -> None:
    print(
        f"{'n':>4} | {'ways(n)':>14} | {'naive, мс':>12} | "
        f"{'memo, мс':>10} | {'iter, мс':>10}"
    )
    print("-" * 64)
    for n in sizes:
        t_naive = timeit(stairs_naive, n)
        t_memo = timeit(memo_cold, n, repeat=200)
        t_iter = timeit(stairs_iter, n, repeat=2000)
        print(
            f"{n:>4} | {stairs_iter(n):>14} | {t_naive:>12.3f} | "
            f"{t_memo:>10.4f} | {t_iter:>10.5f}"
        )


def demo_cache() -> None:
    clear_cache()
    stairs_memo(30)
    print("cache_info після stairs_memo(30):", cache_stats())
    clear_cache()
    print("cache_info після cache_clear():  ", cache_stats())


def demo_recursion_limit() -> None:
    print("sys.getrecursionlimit() =", sys.getrecursionlimit())
    clear_cache()
    try:
        stairs_memo(5000)
    except RecursionError:
        print("stairs_memo(5000) -> RecursionError (глибина рекурсії > ліміту)")
    clear_cache()
    print("stairs_iter(5000) має", len(str(stairs_iter(5000))), "цифр — без проблем")


if __name__ == "__main__":
    run()
    print()
    demo_cache()
    print()
    demo_recursion_limit()
