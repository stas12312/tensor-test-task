import unittest

from modules.writer.formatter import BeatufulFormatter


class TestFormatter(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.row_length = 80
        cls.formatter = BeatufulFormatter(cls.row_length)

    def SetUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_row_length(self):
        """Проверка корректности разбивки строки, если следующее слово не помещается в строку"""
        text = '333 1 4444 55555 333 1 22 666666 7777777 1 22 4444 333 1 22 333 99999999| 7777777'
        expected_text = '333 1 4444 55555 333 1 22 666666 7777777 1 22 4444 333 1 22 333 99999999|\n' \
                        '7777777'

        formatter = BeatufulFormatter(self.row_length)
        formatted_text = formatter.format(text)
        rows = formatted_text.split('\n')

        self.assertEqual(expected_text, formatted_text)

    def test_short_words(self):
        """Проверка, что длинна строки достигает максимума"""
        text = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1| 1 1 1'
        expected_text = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1|\n' \
                        '1 1 1'

        formatter = BeatufulFormatter(self.row_length)
        formatted_text = formatter.format(text)
        self.assertEqual(expected_text, formatted_text)

    def test_rows(self):
        """Проверка на тексте с изначальными переносами"""
        text = '1 1 1 1\n' \
               '1 1 1 1\n' \
               '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1| 1 1 1\n' \
               '1 1 1 1\n'
        expected_text = '1 1 1 1\n\n' \
                        '1 1 1 1\n\n' \
                        '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1|\n' \
                        '1 1 1\n\n' \
                        '1 1 1 1'

        formatted_text = self.formatter.format(text)
        self.assertEqual(expected_text, formatted_text)

    def test_long_word(self):
        """Проверка переноса длинного слова по строкам"""
        text = '111 1111111111111111111111111111111111111111111111111111111111111111111111111111111|1111 1111'
        expected_text = '111\n' \
                        '1111111111111111111111111111111111111111111111111111111111111111111111111111111|\n' \
                        '1111 1111'

        formated_text = self.formatter.format(text)
        self.assertEqual(expected_text, formated_text)
