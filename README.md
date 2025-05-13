[![Python Code Quality Checks](https://github.com/ZhikharevAl/pf-lab-test/actions/workflows/code-quality.yaml/badge.svg)](https://github.com/ZhikharevAl/pf-lab-test/actions/workflows/code-quality.yaml) ![Ruff](https://img.shields.io/badge/linting-Ruff-323330?logo=ruff) ![uv](https://img.shields.io/badge/dependencies-uv-FFA500) ![Pyright](https://img.shields.io/badge/typing-Pyright-007ACC)

# README для проекта pf-lab-test

## Обзор

Этот проект содержит набор из четырех задач в рамках тестового задания для Performance Lab. Каждая задача представлена в виде отдельного модуля и решает определенную алгоритмическую проблему.

## Требования

- Python 3.13 или выше
- Зависимости для разработки (устанавливаются с помощью `uv`):
  - pyright
  - ruff
  - pytest
  - pre-commit

## Установка и настройка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # для Linux/MacOS
   # или
   .venv\Scripts\activate  # для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install uv
   uv pip install -e '.[dev]'
   ```

4. Установите pre-commit хуки:

   ```bash
   pre-commit install
   ```

## Описание задач

### Задача 1: Поиск циклической последовательности

Вычисляет путь обхода кругового массива с заданными параметрами.

**Использование:**

```bash
python task1/task1.py <n> <m>
```

где:

- `n` - размер кругового массива (элементы от 1 до n)
- `m` - длина интервала обхода

**Пример:**

```bash
python task1/task1.py 5 3
```

### Задача 2: Определение положения точек относительно окружности

Определяет положение набора точек относительно заданной окружности.

**Использование:**

```bash
python task2/task2.py <путь_к_файлу_окружности> <путь_к_файлу_точек>
```

где:

- `путь_к_файлу_окружности` - файл с координатами центра окружности и её радиусом
- `путь_к_файлу_точек` - файл с координатами точек

**Результаты:**

- 0 - точка лежит на окружности
- 1 - точка внутри окружности
- 2 - точка снаружи окружности

### Задача 3: Заполнение тестовых значений

Объединяет данные из двух JSON-файлов, заполняя структуру тестовых значений.

**Использование:**

```bash
python task3/task3.py <values.json> <tests.json> <report.json>
```

где:

- `values.json` - файл со значениями тестов
- `tests.json` - файл со структурой тестов
- `report.json` - файл для сохранения результирующего отчета

### Задача 4: Расчет минимального количества ходов

Вычисляет минимальное количество ходов для приведения всех элементов массива к одному значению.

**Использование:**

```bash
python task4/task4.py <путь_к_файлу_c_числами>
```

где:

- `путь_к_файлу_c_числами` - файл с целыми числами, по одному на строку

## Инструменты для разработки

Проект настроен для использования следующих инструментов:

- **Ruff**: линтер и форматтер кода
- **Pyright**: статический анализатор типов
- **pre-commit**: хуки для проверки кода перед коммитом
- **pytest**: библиотека для тестирования

## Структура проекта

```
pf-lab-test/
├── .github/
│   ├── actions/
│   │   ├── run-linters/
│   │   │   └── action.yaml
│   │   └── setup/
│   │       └── action.yaml
│   └── workflows/
│       └── code-quality.yaml
├── task1/
│   ├── __init__.py
│   └── task1.py
├── task2/
│   ├── __init__.py
│   └── task2.py
├── task3/
│   ├── __init__.py
│   └── task3.py
├── task4/
│   ├── __init__.py
│   └── task4.py
├── tests/
│   ├── __init__.py
│   └── test_task1.py
├── .gitignore
├── .pre-commit-config.yaml
├── author.txt
├── pyproject.toml
├── README.md
└── uv.lock

```

## Лицензия

Проект разработан для тестового задания Performance Lab.
