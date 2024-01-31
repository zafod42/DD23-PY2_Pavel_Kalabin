class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        print("Название книги неизменяемо")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        print("Имя автора неизменяемо")


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if self.pages_check(pages):
            self._pages = pages

    def __str__(self):
        return super().__str__() + f" Страницы {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @staticmethod
    def pages_check(value) -> bool:
        """Метод валидации значения кол-ва страниц книги"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц книги должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц книги должно быть положителным числом.")
        return True

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Число страниц должно быть целочисленным.")
        if pages <= 0:
            raise ValueError("Количество страниц книги должно быть положителным числом.")
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if self.duration_check(duration):
            self._duration = duration

    def __str__(self):
        return super().__str__() + f" Длительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @staticmethod
    def duration_check(value) -> bool:
        """Метод валидации значения продолжительности аудиокниги"""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность аудиокниги должна быть целым или дробным числом.")
        if value <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом.")
        return True

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise ValueError("Длительность аудио книги должна быть в формате с плавающей запятой.")
        if duration < 0:
            raise ValueError("Длительность аудио книги должна быть положительной")
        self._duration = duration


if __name__ == '__main__':
    paper = PaperBook("Paper", "Author1", 812)
    audio = AudioBook("Audio", "Author2", 52.7)

    print(paper)
    print(paper.__repr__())
    paper.author = "Author3"
    paper.pages = 200
    print(paper)
    print()
    print(audio)
    print(audio.__repr__())
    audio.duration = 12.1
    print(audio)
