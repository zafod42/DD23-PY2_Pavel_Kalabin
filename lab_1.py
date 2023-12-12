# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Vertex:
    def __init__(self, x: float, y: float, z: float):
        """
        Создание и подготовка к работе объекта "Вершина"

        :param x: координата Х
        :param y: координата Y
        :param z: координата Z

        Примеры:
        >>> vertex = Vertex(-1, -0.3, 3)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Координата X должна быть типа int или float")
        if not isinstance(y, (int, float)):
            raise TypeError("Координата Y должна быть типа int или float")
        if not isinstance(z, (int, float)):
            raise TypeError("Координата Z должна быть типа int или float")

    def get_position_vector(self) -> tuple[float]:
        """
        Метод, который возвращает радиус-вектор точки

        :return: Список, координат точки, который представляет собой её радиус-вектор

        Примеры:
        >>> vertex = Vertex(0, -1, 3)
        >>> vertex.get_position_vector()
        """
        ...

    def move_by_vector(self, vector: tuple[float]) -> None:
        """
        Метод, который сдвигает точку по осям X, Y, Z на заданный вектор

        :param vector: Вектор, на который сдвигается точка

        Примеры:
        >>> vertex = Vertex(-0.1, 0.2, 2.1)
        >>> vector = (-1.2, 2, 3)
        >>> vertex.move_by_vector(vector)
        """
        ...
    ...


class Polygon:
    def __init__(self, a: Vertex, b: Vertex, c: Vertex):
        """
        Создание и подготовка к работе объекта "Полигон"

        :param a: Вершина A - треугольника ABC
        :param b: Вершина B - треугольника ABC
        :param c: Вершина C - треугольника ABC

        Примеры:
        >>> vertex1 = Vertex(-1, 2, 3)
        >>> vertex2 = Vertex(-2.3, -1, 0.2)
        >>> vertex3 = Vertex(-2.1, -4, 2)
        >>> polygon = Polygon(vertex1, vertex2, vertex3)
        """
        if not isinstance(a, Vertex):
            raise TypeError("Вершина A должна иметь тип Vertex")
        if not isinstance(b, Vertex):
            raise TypeError("Вершина B должна иметь тип Vertex")
        if not isinstance(c, Vertex):
            raise TypeError("Вершина C должна иметь тип Vertex")
        if self.is_correct_polygon():
            raise ValueError("Вершины должны составлять корректный треугольник")
        ...

    def is_correct_polygon(self) -> bool:
        """
        Метод, который проверяет является ли полигон корректным

        :return: Является ли полигон корректным

        Примеры:
        >>> a = Vertex(0, 0, 0)
        >>> b = Vertex(1, 0, 0)
        >>> c = Vertex(-1, -1, 0)
        >>> polygon = Polygon(a, b, c)
        >>> polygon.is_correct_polygon()
        """
        ...

    def get_area(self) -> float:
        """
        Метод, который возвращает площадь полигона

        :return: Вычисленная площадь

        Примеры:
        >>> a = Vertex(0, 3, 0)
        >>> b = Vertex(1, 0, 0)
        >>> c = Vertex(-1, -1, 0)
        >>> polygon = Polygon(a, b, c)
        >>> polygon.get_area()
        """
        ...

    def move_by_vector(self, vector: tuple[float]) -> None:
        """
        Метод, который перемещает полигон на вектор

        :param vector: Вектор, на который происходит перемещение

        Примеры:
        >>> a = Vertex(0, 3, 0)
        >>> b = Vertex(1, 0, 0)
        >>> c = Vertex(-1, -1, 0)
        >>> polygon = Polygon(a, b, c)
        >>> vector = (-1, -1, -1)
        >>> polygon.move_by_vector(vector)
        """
    ...

class Surface:
    def __init__(self, polygon_array: list[Polygon], facing: float, position: tuple[float]):
        """
        Создание и подготовка к работе объекта класса Surface

        :param polygon_array: Массив полигонов, из которых состоит поверхность
        :param facing: Направление куда "смотрит" поверхность (в радианах)
        :param position: Радиус-вектор центра поверхности

        Примеры:
        >>> a = Vertex(0, 3, 0)
        >>> b = Vertex(1, 0, 0)
        >>> c = Vertex(-1, -1, 0)
        >>> polygon = Polygon(a, b, c)
        >>> polygon_array = list()
        >>> polygon_array.append(polygon)
        >>> surface = Surface(polygon_array, 0, (0, 0, 0))
        """
        if not isinstance(polygon_array, list) and not isinstance(polygon_array[0], Polygon):
            raise TypeError("Массив должен содержать полигоны")
        if not isinstance(facing, (int, float)):
            raise TypeError("facing должен быть типа int или float")
        if not isinstance(position, tuple) and not isinstance(position[0], float):
            raise TypeError("Вектор position должен содержать float координаты")
        if len(position) != 3:
            raise ValueError("Векто position должен содержать три координаты в пространстве")
        if len(polygon_array) == 0:
            raise ValueError("Поверхность должна состоять хотя бы из одного полигона")
        ...

    def get_area(self) -> float:
        """
        Метод, который возвращет площадь поверхности

        :return: Площадь поверхности

        Примеры:
        >>> a = Vertex(0, 3, 0)
        >>> b = Vertex(1, 0, 0)
        >>> c = Vertex(-1, -1, 0)
        >>> polygon = Polygon(a, b, c)
        >>> polygon_array = list()
        >>> polygon_array.append(polygon)
        >>> surface = Surface(polygon_array, 0, (0, 0, 0))
        >>> surface.get_area()
        """

    def get_distance_from_center(self) -> float:
        """
        Метод, который возвращает длинну отрезка между координатами (0,0,0) и центром поверхности

        :return: Длинна отрезка

        Примеры:
        >>> a = Vertex(0, 3, 0)
        >>> b = Vertex(1, 0, 0)
        >>> c = Vertex(-1, -1, 0)
        >>> polygon = Polygon(a, b, c)
        >>> polygon_array = list()
        >>> polygon_array.append(polygon)
        >>> surface = Surface(polygon_array, 0, (0, 0, 0))
        >>> surface.get_distance_from_center()
        """
    ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
