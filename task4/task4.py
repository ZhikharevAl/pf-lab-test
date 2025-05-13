import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)


def read_numbers_from_file(filepath: str) -> list[int]:
    """
    Считывает целые числа из файла, по одному на строку.

    Args:
        filepath: Путь к файлу.

    Returns:
        Список целых чисел.
    """
    numbers = []
    try:
        with Path(filepath).open(encoding="utf-8") as f:
            for i, line in enumerate(f):
                try:
                    num = int(line.strip())
                    numbers.append(num)
                except ValueError:
                    logger.warning(
                        "Предупреждение: Пропуск недопустимого числа на строке %d в файле %s: '%s'",
                        i + 1,
                        filepath,
                        line.strip(),
                    )
        return numbers  # noqa: TRY300
    except FileNotFoundError:
        logger.exception("Ошибка: Файл не найден по пути %s", filepath)
        sys.exit(1)
    except OSError:
        logger.exception("Произошла ошибка ввода-вывода при чтении файла %s", filepath)
        sys.exit(1)


def calculate_min_moves(nums: list[int]) -> int:
    """
    Вычисляет минимальное количество ходов для приведения всех элементов списка к одному числу.

    Оптимальная стратегия - привести все элементы к медиане списка.
    Общее количество ходов равно сумме абсолютных разностей между каждым
    элементом и медианой.

    Args:
        nums: Список целых чисел.

    Returns:
        Минимальное количество требуемых ходов.
    """
    if not nums:
        return 0

    nums.sort()
    median_index = len(nums) // 2
    median = nums[median_index]

    total_moves = 0
    for num in nums:
        total_moves += abs(num - median)

    return total_moves


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 2:
        logger.error("Использование: python task4.py <путь_к_файлу_c_числами>")
        sys.exit(1)

    numbers_file = sys.argv[1]

    numbers_list = read_numbers_from_file(numbers_file)

    if not numbers_list:
        logger.error("Ошибка: Входной файл не содержит допустимых чисел.")
        sys.exit(1)

    min_moves = calculate_min_moves(numbers_list)

    logger.info(min_moves)
