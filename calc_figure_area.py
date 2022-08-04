from typing import List, Tuple


def calc_figure_area(points: List[Tuple[float]]) -> float:
    """Функция расчёта площади фигуры по координатам точек на плоскости."""
    total = 0
    for i in range(len(points)):
        if len(points[i]) != 2:
            raise ValueError(
                'Для расчёта площади необходимо '
                'два значения в одной координате'
            )
        if i == len(points) - 1:
            break
        if (not isinstance(points[i][0], (int, float))
                or not isinstance(points[i][1], (int, float))):
            raise TypeError(
                'Для расчёта площади необходимо передавать численные значения'
                'координат точек на плоскости'
            )
        side_a = abs(points[i][1])
        side_b = abs(points[i+1][1])
        high = points[i+1][0] - points[i][0]
        s = high * (side_a + side_b) / 2
        total += s
    return total
