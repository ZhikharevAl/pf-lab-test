import logging
import math
import sys
from pathlib import Path

logger = logging.getLogger(__name__)


def get_point_position(
    circle_x: float, circle_y: float, radius: float, point_x: float, point_y: float
) -> int:
    """
    Определяет положение точки относительно окружности.

    Args:
        circle_x: Координата X центра окружности.
        circle_y: Координата Y центра окружности.
        radius: Радиус окружности.
        point_x: Координата X точки.
        point_y: Координата Y точки.

    Returns:
        0, если точка лежит на окружности.
        1, если точка внутри окружности.
        2, если точка снаружи окружности.
    """
    distance_sq = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    radius_sq = radius**2

    if math.isclose(distance_sq, radius_sq):
        return 0
    if distance_sq < radius_sq:
        return 1
    return 2


def read_circle_data(filepath: str) -> tuple[float, float, float]:
    """Считывает координаты центра и радиус окружности из файла."""
    try:
        with Path(filepath).open(encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) < 2:
                msg = "Файл окружности должен содержать как минимум 2 строки."
                raise ValueError(msg)
            center_coords = lines[0].strip().split()
            if len(center_coords) != 2:
                msg = "Первая строка файла окружности должна содержать координаты X и Y."
                raise ValueError(msg)
            radius_line = lines[1].strip()

            center_x = float(center_coords[0])
            center_y = float(center_coords[1])
            radius_val = float(radius_line)

            if radius_val < 0:
                msg = "Радиус не может быть отрицательным."
                raise ValueError(msg)

            return center_x, center_y, radius_val
    except FileNotFoundError:
        logger.info("Ошибка: Файл окружности не найден по пути %s", filepath)
        sys.exit(1)
    except ValueError as e:
        logger.info("Ошибка при чтении файла окружности %s: %s", filepath, e)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        logger.info("Произошла непредвиденная ошибка при чтении файла %s: %s", filepath, e)
        sys.exit(1)


def read_points_data(filepath: str) -> list[tuple[float, float]]:
    """Считывает координаты точек из файла."""
    points = []
    try:
        with Path(filepath).open(encoding="utf-8") as f:
            for i, line in enumerate(f):
                coords = line.strip().split()
                if len(coords) != 2:
                    msg = f"Строка {i + 1} в файле точек должна содержать координаты X и Y."
                    raise ValueError(msg)
                point_x = float(coords[0])
                point_y = float(coords[1])
                points.append((point_x, point_y))
        if not 1 <= len(points) <= 100:
            msg = "Количество точек должно быть от 1 до 100."
            raise ValueError(msg)
        return points  # noqa: TRY300
    except FileNotFoundError:
        logger.exception("Ошибка: Файл точек не найден по пути %s", filepath)
        sys.exit(1)
    except ValueError:
        logger.exception("Ошибка при чтении файла точек %s", filepath)
        sys.exit(1)
    except OSError:
        logger.exception("Ошибка ввода-вывода при чтении файла %s", filepath)
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 3:
        sys.stderr.write(
            "Использование: python task2.py <путь_к_файлу_окружности> <путь_к_файлу_точек>\n"
        )
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    c_x, c_y, r = read_circle_data(circle_file)
    points_list = read_points_data(points_file)

    results = []
    for p_x, p_y in points_list:
        position_code = get_point_position(c_x, c_y, r, p_x, p_y)
        results.append(str(position_code))

    logger.info("\n".join(results))
