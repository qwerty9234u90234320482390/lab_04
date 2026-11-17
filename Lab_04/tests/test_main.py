import pytest

from main import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    out = capsys.readouterr().out
    assert "Варіант 11" in out
    assert "RecursionError" in out
