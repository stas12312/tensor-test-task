from typing import Union

from bs4 import BeautifulSoup, Tag, NavigableString, PageElement, Comment  # noqa

from .converter import Converter
from .strategy import Strategy


class Parser:
    """
    Класс для процесса поиска полезной информации
    на странице и его преобразование в текст
     """

    def __init__(self, body: bytes,
                 strategy: Strategy, converter: Converter):
        self.body = BeautifulSoup(body, 'html.parser')
        self.strategy = strategy
        self.converter = converter
        self.elements = self._get_useful_elemets()

    def _get_useful_elemets(self) -> list[Union[Tag, NavigableString]]:
        """Получение элементов с полезной информацией"""
        return self.strategy.get_elements(self.body)

    def get_elemets(self) -> list[Union[Tag, NavigableString]]:
        """Получение необходимых элементов"""
        return self.elements

    def get_text(self) -> str:
        """Получение текста"""
        text_parts = []
        for element in self.elements:
            element_text = self.converter.to_text(element)
            if element_text:
                text_parts.append(element_text)
        return '\n'.join(text_parts)
