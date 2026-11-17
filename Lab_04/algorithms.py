"""Лабораторна робота 4: базова частина (quicksort, обходи дерев, Фібоначчі)."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from random import choice
from typing import Generator, Optional


def quicksort(xs: list[int]) -> list[int]:
    """Рекурсивний чистий quicksort (3-шляхове розбиття, випадковий pivot)."""
    # база рекурсії: 0 або 1 елемент вже відсортовано
    if len(xs) <= 1:
        return xs[:]
    p = choice(xs)
    left = [x for x in xs if x < p]
    mid = [x for x in xs if x == p]
    right = [x for x in xs if x > p]
    # крок рекурсії: сортуємо лише підмасиви
    return quicksort(left) + mid + quicksort(right)


@dataclass(slots=True)
class Node:
    """Вузол бінарного дерева."""

    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def preorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return
    yield t.key
    yield from preorder(t.left)
    yield from preorder(t.right)


def inorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return
    yield from inorder(t.left)
    yield t.key
    yield from inorder(t.right)


def postorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return
    yield from postorder(t.left)
    yield from postorder(t.right)
    yield t.key


def bfs_level_order(t: Optional[Node]) -> list[int]:
    """Ітеративний обхід у ширину (черга)."""
    if not t:
        return []
    q, out = deque([t]), []
    while q:
        n = q.popleft()
        out.append(n.key)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return out


def dfs_preorder_iter(t: Optional[Node]) -> list[int]:
    """Ітеративний DFS preorder із власним стеком."""
    if not t:
        return []
    stack, out = [t], []
    while stack:
        n = stack.pop()
        out.append(n.key)
        # спершу правий, щоб лівий був оброблений першим
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
    return out


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Фібоначчі з мемоізацією (O(n))."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iter(n: int) -> int:
    """Ітеративний Фібоначчі без рекурсії."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fact(n: int, acc: int = 1) -> int:
    """Псевдо-tail-рекурсія: у CPython TCO немає, стек все одно росте."""
    if n <= 1:
        return acc
    return fact(n - 1, acc * n)
