import unittest

from calc_figure_area import calc_figure_area


class TestCalcArea(unittest.TestCase):
    """Тестируем calc_figure_area."""

    def test_calc_int(self):
        """Тест на правильность ответа при передаче интов."""
        data = [(0, 0), (1, 1), (2, 2), (3, 1), (4, 2), (5, 3), (6, 4), (7, 2)]
        self.assertEqual(
            calc_figure_area(data),
            14,
            'Функция возвращает некорректное значение'
        )

    def test_calc_float(self):
        """Тест на правильность ответа при передаче флотов."""
        data = [(0.0, 0.0), (1.5, 1.5), (2.5, 2.5)]
        self.assertEqual(
            calc_figure_area(data),
            3.125,
            'Функция возвращает некорректное значение'
        )

    def test_calc_int_and_float(self):
        """Тест на правильность ответа при передаче флотов и интов."""
        data = [(0.0, 0), (1.5, 1.5), (3, 3)]
        self.assertEqual(
            calc_figure_area(data),
            4.5,
            'Функция возвращает некорректное значение'
        )

    def test_one_point(self):
        """Тест на передачу одной точки."""
        data = [(1, 0)]
        self.assertEqual(
            calc_figure_area(data),
            0,
            'Функция возвращает некорректное значение при передаче одной точки'
        )

    def test_empty_data(self):
        """Тест пустого массива."""
        data = []
        self.assertEqual(
            calc_figure_area(data),
            0,
            'Функция возвращает некорректное значение при '
            'передаче пустого списка'
        )

    def test_tuple_isnt_couple_values(self):
        """Тест передачи лишнего значения в координате точки."""
        data = [(1, 0), (2, 3), (3, 2, 5)]
        self.assertRaises(ValueError, calc_figure_area, data)

    def test_values_is_digits(self):
        """Тест передачи некорректного типа данных в кортеже."""
        data = [(1, 0), ('qwe', 'as'), (3, 2)]
        self.assertRaises(TypeError, calc_figure_area, data)


if __name__ == '__main__':
    unittest.main()
