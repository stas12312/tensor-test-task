from abc import abstractmethod, ABC
from io import BytesIO
from typing import TextIO


class Ouptut(ABC):

    @abstractmethod
    def write(self, text: str) -> None:
        """Метод для записи текста на внешнее устройтсов"""


class ConsoleOuptut(Ouptut):
    def write(self, text: str) -> None:
        """Вывод текста на консоль"""
        print(text)


class FileOuptut(Ouptut):
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, text: str) -> None:
        """Вывод текста в файл"""
        with open(self.filename, 'w+', encoding='UTF-8') as f:
            f.write(text)


class IOOutput(Ouptut):
    def __init__(self, __io: TextIO):
        self.io = __io

    def write(self, text: str) -> None:
        """Вывод текста в IO объект"""
        self.io.write(text)
