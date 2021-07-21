from abc import ABC, abstractmethod
from typing import Union

from bs4 import Tag, NavigableString  # noqa


class Strategy(ABC):
    """Класс для получения полезных элементов страницы"""

    @abstractmethod
    def get_elements(self, page: Union[Tag, NavigableString]) -> list[Union[Tag, NavigableString]]:
        raise NotImplementedError


class DefaultStrategy(Strategy):
    """
    Стандартная стратегия парсинга полезной информации

    Данный метод основывается на том, что полезная часть нагрузки страницы представляет собой <p> и <h1> тэги
    """

    def get_elements(self, page: Union[Tag, NavigableString]) -> list[Union[Tag, NavigableString]]:
        return page.findAll(['p', 'h1'])
