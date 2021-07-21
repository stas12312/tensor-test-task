import os
import unittest
import uuid
from io import StringIO

from modules.writer import FormattedWriter
from modules.writer.formatter import BeatufulFormatter
from modules.writer.output import IOOutput


class WriterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.row_length = 80

    def test_write_in_file(self):
        """Проверка записи в файловый объект"""
        text = '333 1 4444 55555 333 1 22 666666 7777777 1 22 4444 333 1 22 333 99999999| 7777777'
        expected_test = '333 1 4444 55555 333 1 22 666666 7777777 1 22 4444 333 1 22 333 99999999|\n' \
                        '7777777'
        temp_filename = f'{uuid.uuid4()}.txt'
        with open(temp_filename, 'w+', encoding='UTF-8') as f:
            writer = FormattedWriter(BeatufulFormatter(self.row_length), IOOutput(f))
            writer.write(text)

        with open(temp_filename, 'r', encoding='UTF-8') as f:
            writed_text = f.read()

        os.remove(temp_filename)
        self.assertEqual(expected_test, writed_text)

    def test_write_in_string(self):
        """Проверка записи в StringIO объект"""
        text = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1| 1 1 1'
        expected_test = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1|\n' \
                        '1 1 1'

        string_io = StringIO()
        writer = FormattedWriter(BeatufulFormatter(self.row_length), IOOutput(string_io))
        writer.write(text)
        string_io.seek(0)
        self.assertEqual(expected_test, string_io.read())
