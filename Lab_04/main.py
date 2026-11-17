"""Точка входу лабораторної роботи №4, варіант 11 (рекурсія та мемоізація)."""

from __future__ import annotations

from algorithms import (
    Node,
    bfs_level_order,
    dfs_preorder_iter,
    fib,
    fib_iter,
    inorder,
    postorder,
    preorder,
    quicksort,
)
from benchmark import demo_cache, demo_recursion_limit
from benchmark import run as run_benchmark
from stairs import stairs_iter, stairs_memo, stairs_naive


def demo_base() -> None:
    """Демонстрація базової частини: quicksort, обходи дерева, Фібоначчі."""
    print("quicksort([5, 2, 9, 2, 1]) =", quicksort([5, 2, 9, 2, 1]))
    tree = Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))
    print("preorder  :", list(preorder(tree)))
    print("inorder   :", list(inorder(tree)))
    print("postorder :", list(postorder(tree)))
    print("bfs       :", bfs_level_order(tree))
    print("dfs iter  :", dfs_preorder_iter(tree))
    print("fib(30) =", fib(30), "| fib_iter(30) =", fib_iter(30))


def demo_stairs() -> None:
    """Варіант 11: кількість способів піднятися на n сходинок."""
    for n in (1, 2, 3, 4, 10):
        print(
            f"n={n}: naive={stairs_naive(n)}, "
            f"memo={stairs_memo(n)}, iter={stairs_iter(n)}"
        )


def main() -> None:
    """Запуск усіх демонстрацій лабораторної роботи."""
    print("=== Базова частина ===")
    demo_base()
    print("\n=== Варіант 11: задача про сходинки ===")
    demo_stairs()
    print("\n=== Порівняння часу ===")
    run_benchmark((10, 15, 20, 25))
    print("\n=== Кеш ===")
    demo_cache()
    print("\n=== Ліміт рекурсії ===")
    demo_recursion_limit()


if __name__ == "__main__":
    main()
