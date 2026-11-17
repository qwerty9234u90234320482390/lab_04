# Лабораторна робота №4. Варіант 11: Задача про сходинки

## Опис
Рекурсія та мемоізація в Python. База: `quicksort`, обходи бінарного дерева
(рекурсивні та ітеративні), `fib` з `@lru_cache` та `fib_iter`.
Варіант 11: кількість способів піднятися на `n` сходинок кроками 1, 2 або 3 —
три версії (naive, memoized, iterative) і таблиця часу.

## Структура
- `algorithms.py` — quicksort, `Node` + обходи, `fib`, `fib_iter`, `fact`;
- `stairs.py` — варіант 11: `stairs_naive`, `stairs_memo`, `stairs_iter`;
- `benchmark.py` — таблиця часу, `cache_info()`/`cache_clear()`, демо `RecursionError`;
- `tests/` — pytest-тести (`test_quicksort.py`, `test_tree.py`, `test_fib.py`, `test_stairs.py`);
- `requirements.txt`, `mypy.ini`, `pyproject.toml`, `.gitignore`.

## Швидкий старт
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python benchmark.py
black --check . && ruff check . && mypy
```

## Базовий випадок і рекурсивний крок (варіант 11)
- база: `ways(0) = 1`, `ways(n < 0) = 0`;
- крок: `ways(n) = ways(n-1) + ways(n-2) + ways(n-3)`.

## Ліміт рекурсії CPython і відсутність TCO
- Глибина стека за замовчуванням ≈ 1000 кадрів (`sys.getrecursionlimit()`);
  при перевищенні виникає `RecursionError`. Підіймати ліміт
  (`sys.setrecursionlimit`) ризиковано — можливий segfault.
- CPython **не виконує tail-call optimization**: навіть хвостова рекурсія
  (`fact(n-1, acc*n)`) займає новий кадр стека на кожен виклик.
- Тому для великих `n` (наприклад, `stairs_memo(5000)`) використовуйте
  ітеративну версію `stairs_iter` — вона не залежить від глибини стека
  і використовує O(1) пам'яті.
- Наївна рекурсія має експоненційний час; `@lru_cache` зводить його до O(n).
