from .formatter import Formatter
from .output import Ouptut


class FormattedWriter:
    """Класс для вывода результата"""

    def __init__(self, formatter: Formatter, output: Ouptut):
        self.formatter = formatter
        self.output = output

    def write(self, text: str) -> None:
        text = self.formatter.format(text)
        self.output.write(text)
