import pytest

from stairs import (
    _memo,
    clear_cache,
    stairs_iter,
    stairs_memo,
    stairs_naive,
)

KNOWN = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]  # ways(0..10)


def test_known_values_all_versions() -> None:
    for n, expected in enumerate(KNOWN):
        assert stairs_naive(n) == expected
        assert stairs_memo(n) == expected
        assert stairs_iter(n) == expected


def test_base_cases() -> None:
    assert stairs_naive(0) == 1
    assert stairs_memo(0) == 1
    assert stairs_iter(0) == 1


def test_negative_raises() -> None:
    for fn in (stairs_naive, stairs_memo, stairs_iter):
        with pytest.raises(ValueError):
            fn(-1)


def test_versions_agree_up_to_20() -> None:
    for n in range(21):
        assert stairs_naive(n) == stairs_memo(n) == stairs_iter(n)


def test_recurrence_property() -> None:
    for n in range(3, 60):
        assert stairs_iter(n) == (
            stairs_iter(n - 1) + stairs_iter(n - 2) + stairs_iter(n - 3)
        )


def test_cache_info_and_clear() -> None:
    clear_cache()
    assert _memo.cache_info().currsize == 0
    stairs_memo(10)
    info = _memo.cache_info()
    assert info.currsize > 0
    assert info.hits > 0
    clear_cache()
    assert _memo.cache_info().currsize == 0


def test_large_n_iterative_is_safe() -> None:
    assert stairs_iter(5000) > 0
    clear_cache()
    with pytest.raises(RecursionError):
        stairs_memo(5000)
    clear_cache()
