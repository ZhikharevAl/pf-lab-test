import pytest

from task1.task1 import find_cyclic_sequence


@pytest.mark.parametrize(
    ("n", "m", "expected_path"),
    [
        (4, 3, "13"),
        (5, 4, "14253"),
    ],
)
def test_task_examples(n: int, m: int, expected_path: str) -> None:
    """Тестирует функцию find_cyclic_sequence на примерах из задания."""
    assert find_cyclic_sequence(n, m) == expected_path, f"Ошибка для n={n}, m={m}"


@pytest.mark.parametrize(
    ("n", "m", "expected_path"),
    [
        (1, 1, "1"),
        (2, 1, "1"),
        (2, 2, "12"),
        (3, 2, "123"),
        (10, 1, "1"),
        (5, 5, "15432"),
        (5, 6, "1"),
        (5, 10, "15432"),
        (6, 4, "14"),
        (7, 3, "1357246"),
    ],
)
def test_valid_inputs(n: int, m: int, expected_path: str) -> None:
    """Тестирует различные валидные комбинации n и m, включая граничные случаи."""
    assert find_cyclic_sequence(n, m) == expected_path, f"Ошибка для валидных n={n}, m={m}"


@pytest.mark.parametrize("invalid_n", [0, -1, -10])
def test_invalid_n(invalid_n: int) -> None:
    """Тестирует невалидные значения n (граничные и типичные)."""
    m_valid = 3
    with pytest.raises(SystemExit) as excinfo:
        find_cyclic_sequence(invalid_n, m_valid)
    assert excinfo.value.code == 1, f"Ожидался SystemExit(1) для n={invalid_n}"


@pytest.mark.parametrize("invalid_m", [0, -1, -5])
def test_invalid_m(invalid_m: int) -> None:
    """Тестирует невалидные значения m (граничные и типичные)."""
    n_valid = 5
    with pytest.raises(SystemExit) as excinfo:
        find_cyclic_sequence(n_valid, invalid_m)
    assert excinfo.value.code == 1, f"Ожидался SystemExit(1) для m={invalid_m}"


def test_both_invalid() -> None:
    """Тестирует случай, когда и n, и m невалидны."""
    with pytest.raises(SystemExit) as excinfo:
        find_cyclic_sequence(0, 0)
    assert excinfo.value.code == 1


def test_large_values() -> None:
    """Тестирует относительно большие значения n и m (проверка производительности/границ)."""
    try:
        result = find_cyclic_sequence(50, 17)
        assert isinstance(result, str)
        assert len(result) > 0
    except (ValueError, TypeError) as e:
        pytest.fail(f"Тест c большими значениями вызвал ошибку: {e}")
