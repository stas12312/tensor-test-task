import unittest

from bs4 import BeautifulSoup

from modules.parser.converter import DefaultConverter


class ConverterTest(unittest.TestCase):

    def test_convert_html(self):
        """Проверка конвертирования елемента htmk в текст"""
        test_html = '<p>Тестовая строка со ссылкой ' \
                    '<a href="https://test.ru"><b>Ссылка </b></a>' \
                    'в которой есть пробел, а также ' \
                    '<strong>разные</strong><em> тэги</em><b>для</b> <i>форматирования</i> ' \
                    'текста</p>'

        expected_text = 'Тестовая строка со ссылкой (Ссылка) [https://test.ru] в которой есть пробел,' \
                        ' а также разные тэгидля форматирования текста'

        soup = BeautifulSoup(test_html, 'lxml')
        element = soup.find('p')
        converter = DefaultConverter()
        converted_text = converter.to_text(element)

        self.assertEqual(expected_text, converted_text)

    def test_add_base_uri(self):
        """Проверка дополнения ссылок до абсолютного пути"""
        test_html = '<p>Тестовая <a href="https://test.ru/content">ссылка с абсолютным путём</a> ' \
                    'Тестовая <a href="/content">ссылка с относительным путём</a><\p>'

        expected_text = 'Тестовая (ссылка с абсолютным путём) [https://test.ru/content] ' \
                        'Тестовая (ссылка с относительным путём) [https://test.ru/content]'

        soup = BeautifulSoup(test_html, 'lxml')
        element = soup.find('p')
        converter = DefaultConverter("https://test.ru")
        converter_text = converter.to_text(element)

        self.assertEqual(expected_text, converter_text)
