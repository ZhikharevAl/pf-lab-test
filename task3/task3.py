import json
import logging
import sys
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

TestData = dict[str, Any]


def load_json_file(filepath: str) -> dict[str, Any]:
    """Загружает данные JSON из файла."""
    try:
        with Path(filepath).open(encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.exception("Ошибка: Файл не найден по пути %s", filepath)
        sys.exit(1)
    except json.JSONDecodeError:
        logger.exception("Ошибка: Неверный формат JSON в файле %s", filepath)
        sys.exit(1)
    except Exception:
        logger.exception("Произошла непредвиденная ошибка при чтении файла %s", filepath)
        sys.exit(1)


def save_json_file(filepath: str, data: dict[str, Any]) -> None:
    """Сохраняет данные в файл JSON."""
    try:
        with Path(filepath).open(encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except OSError:
        logger.exception("Ошибка: He удалось записать в файл %s", filepath)
        sys.exit(1)
    except Exception:
        logger.exception("Произошла непредвиденная ошибка при записи в файл %s", filepath)
        sys.exit(1)


def fill_test_values(test_structure: list[TestData], values_map: dict[int, str]) -> None:
    """
    Рекурсивно заполняет поле 'value' в структуре тестов на основе словаря значений.

    Args:
        test_structure: Список словарей тестов (может быть вложенным).
        values_map: Словарь, сопоставляющий ID тестов c их результатами ('passed'/'failed').
    """
    for test_item in test_structure:
        test_id = test_item.get("id")
        if test_id is not None and test_id in values_map:
            test_item["value"] = values_map[test_id]
        if "values" in test_item and isinstance(test_item.get("values"), list):
            fill_test_values(test_item["values"], values_map)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        logger.error("Использование: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    values_data = load_json_file(values_file_path)
    tests_data = load_json_file(tests_file_path)

    if (
        not isinstance(values_data, dict)
        or "values" not in values_data
        or not isinstance(values_data.get("values"), list)
    ):
        logger.error(
            (
                "Ошибка: Неверный формат в файле %s. "
                "Ожидается словарь c ключом 'values', содержащим список."
            ),
            values_file_path,
        )
        sys.exit(1)

    if (
        not isinstance(tests_data, dict)
        or "tests" not in tests_data
        or not isinstance(tests_data.get("tests"), list)
    ):
        logger.error(
            (
                "Ошибка: Неверный формат в файле %s. "
                "Ожидается словарь c ключом 'tests', содержащим список."
            ),
            tests_file_path,
        )
        sys.exit(1)

    value_lookup: dict[int, str] = {}
    for item in values_data.get("values", []):
        if isinstance(item, dict) and "id" in item and "value" in item:
            value_lookup[item["id"]] = item["value"]
        else:
            logger.warning(
                "Предупреждение: Пропуск некорректного элемента в файле %s: %s",
                values_file_path,
                item,
            )
    report_data = tests_data

    if "tests" in report_data:
        fill_test_values(report_data["tests"], value_lookup)
    else:
        logger.error("Ошибка: Ключ 'tests' не найден в %s", tests_file_path)
        sys.exit(1)

    save_json_file(report_file_path, report_data)
