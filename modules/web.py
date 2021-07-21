import re
from dataclasses import dataclass

import requests

URI_REGEX = re.compile(r'^(https?)://(([\w]+\.)+[\w]+)/?([а-яА-ЯЁёa-zA-Z0-9-/_.]*)')


class WebException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


@dataclass
class URL:
    scheme: str
    host: str
    path: str


class Web:
    """Класс для получения и подготовки страницы"""

    @classmethod
    def get_page(cls, uri: str) -> bytes:
        """Получение страницы по указанному url"""
        try:
            r = requests.get(uri)
        except requests.RequestException as e:
            raise WebException(message=f'Ошибка при получении страницы <{e}>')

        return r.content

    @classmethod
    def get_uri_part(cls, uri: str) -> URL:
        """Получение частей url ссылки"""
        result = URI_REGEX.search(uri)
        if not result:
            raise WebException(message='Некорректная ссылка')
        return URL(scheme=result.group(1), host=result.group(2), path=result.group(4))
