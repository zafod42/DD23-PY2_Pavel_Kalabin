class Property:
    """
    Класс Property описывает имущество. Имущество имеет некоторую стоимость и владельца.
    """

    def __init__(self, cost: float, owner: str):
        """
        Конструктор класса Property

        :param cost: Стоимость имущества в рублях. Дробная часть представляет собой копейки
        :param owner: ФИО владельца имущества в именительном падеже

        """
        self.cost = cost
        self.owner = owner

    def __str__(self):
        """
        Возвращает строковое представление объекта в виде форматированной строки.

        :returns: Строковое представление объекта
        :rtype: str
        """
        return f"Имущество. Cтоимость:{self.cost} рублей. Владелец: {self.owner}."

    def __repr__(self):
        """
        Возвращает представление объекта в виде валидного выражения Python.

        :returns: Валидное выражение Python
        :rtype: str
        """
        return f"{self.__class__.__name__}(cost={self.cost}, owner='{self.owner}')"

    def sell(self, new_owner: str) -> None:
        """
        Продажа имущества по нынешней стоимости

        :param new_owner: Новый владелец, которому было продано имуещство

        """
        pass

    def use(self) -> bool:
        """
        Метод позволяет использовать имущество

        :returns: Информацию об успешном использовании
        :rtype: bool
        """
        pass

    pass


class Apartment(Property):
    """ Класс Apartment описывает подкласс имущества. """

    def __init__(self, cost: float, owner: str, area: float, address: str):
        """
        Конструктор класса Apartment

        :param cost: Стоимость имущества в рублях. Дробная часть представляет собой копейки
        :param owner: ФИО владельца имущества в именительном падеже
        :param area: Площадь квартиры.
        :param address: Адрес квартиры.

        """
        super().__init__(cost, owner)
        self.area = area
        self.address = address

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта в виде форматированной строки.

        :returns: Строковое представление объекта
        :rtype: str
        """

        return f"Квартира. Стоимость: {self.cost} рублей. Владелец: {self.owner}. Площадь: {self.area}. Адрес: {self.address}"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта в виде валидного выражения Python.

        :returns: Валидное выражение Python
        :rtype: str
        """
        return f"{self.__class__.__name__}(cost={self.cost}, owner='{self.owner}', area={self.area}, address='{self.address}')"

    def use(self) -> bool:
        """
        Метод позволяющий выпоолнить проживание в квартире.

        Метод был перегружен так как характер "использования" квартиры отличается
        от того как используется имущество в общем смысле. В квартире необходимо
        проживать

        :returns: Успешность вашего проживания в квартире
        :rtype: bool
        """
        pass
    pass


if __name__ == "__main__":
    # Write your solution here
    property = Property(192.2, "Пупкин Василий Васильевич")
    print(property)
    print(property.__repr__())
    apartment = Apartment(20_000_000, "Пупкин Василий Васильевич", 123, "Саратов")
    print(apartment)
    print(apartment.__repr__())
    pass
