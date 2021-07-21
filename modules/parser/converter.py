from abc import abstractmethod
from typing import Union

from bs4 import BeautifulSoup, Tag, NavigableString, PageElement, Comment  # noqa

NBSP_SPACE_CHAR = ' '
ZBSP_SPACE_CHAR = '​'


class Converter:
    """
    Абстрактный класс для преобразования BS4 элементов в текст
    """

    @abstractmethod
    def to_text(self, element) -> str:
        raise NotImplementedError()


class DefaultConverter(Converter):
    """
    Стандартый преобразователь BS4 элемента в строку

    Позволяет дополнять относительные ссылки для абсолютных
    """

    def __init__(self, base_url: str = ''):
        self.base_url = base_url

    def to_text(self, element: Union[Tag, NavigableString]) -> str:
        """Преобразование HTML элемента в текстовую строку"""
        element_text_parts: list[str] = []
        for part in element:
            text_part = self._get_text_from_part(part)
            if text_part:
                element_text_parts.append(text_part)
        return ''.join(element_text_parts)

    def _get_text_from_part(self, part: Union[Tag, NavigableString]) -> str:
        """Получение текстового представления для состовной части тэга <p>"""
        if self._is_link(part):
            link = part.get("href")
            suffix = ' ' if part.text[-1] == ' ' else ''
            abs_link = self._get_abs_link(link)
            link_name = part.text.strip()
            text = f'({link_name}) [{abs_link}]{suffix}'

        elif hasattr(part, 'text'):
            text = part.text
        elif isinstance(part, str):
            text = part
        else:
            return ''
        if text == '\n':
            return ''

        text = text.replace(NBSP_SPACE_CHAR, ' ')
        text = text.replace(ZBSP_SPACE_CHAR, ' ')
        return f'{text}'

    # noinspection PyMethodMayBeStatic
    def _is_link(self, element: Union[Tag, NavigableString]) -> bool:
        """Проверка, что элемент является ссылкой"""
        return isinstance(element, Tag) and element.name == 'a'

    # noinspection PyMethodMayBeStatic
    def _is_abs_link(self, link: str) -> bool:
        """Проверка, что ссылка абсолютная"""
        return link[0] != '/'

    def _get_abs_link(self, link: str) -> str:
        return f'{self.base_url}{link}' if not self._is_abs_link(link) else link
