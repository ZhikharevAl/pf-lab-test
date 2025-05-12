import logging
import sys

logger = logging.getLogger(__name__)


def find_cyclic_sequence(n: int, m: int) -> str:
    """
    Вычисляет путь обхода кругового массива.

    Args:
        n: Размер кругового массива (элементы от 1 до n).
        m: Длина интервала обхода.

    Returns:
        Строка, представляющая путь.
    """
    if n <= 0 or m <= 0:
        logger.error("Ошибка: n и m должны быть положительными целыми числами.")
        sys.exit(1)

    path = []
    current_pos = 1

    while True:
        path.append(current_pos)
        end_pos = ((current_pos - 1) + (m - 1)) % n + 1
        current_pos = end_pos
        if current_pos == 1:
            break
    return "".join(map(str, path))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 3:
        logger.error("Использование: python task1.py <n> <m>")
        sys.exit(1)

    try:
        n_arg = int(sys.argv[1])
        m_arg = int(sys.argv[2])
        RESULT_PATH = find_cyclic_sequence(n_arg, m_arg)
        logger.info("Результат: %s", RESULT_PATH)

    except ValueError:
        logger.exception("Ошибка: n и m должны быть целыми числами.")
        sys.exit(1)
    except ArithmeticError:
        logger.exception("Произошла ошибка арифметики.")
        sys.exit(1)
    except RuntimeError:
        logger.exception("Произошла ошибка выполнения.")
        sys.exit(1)
