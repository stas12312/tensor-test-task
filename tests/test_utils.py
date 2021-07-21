import os.path
import unittest

from modules.utils import get_filepath


class TestUtils(unittest.TestCase):

    def test_build_file_path(self):
        """Проверка построения пути файла по URL"""
        host = 'test.ru'
        url = '/test/path/article'
        ext = 'txt'

        expected_dirname = os.path.join('test.ru', 'test', 'path')
        expected_filename = 'article.txt'

        dirname, filename = get_filepath(host, url, ext)
        self.assertEqual(expected_dirname, dirname)
        self.assertEqual(expected_filename, filename)

    def test_build_file_path_with_closed_url(self):
        """Проверка построения пути с / в конце url"""
        host = 'sub.domain.ru'
        url = '/test/path/article/'
        ext = 'txt'

        expected_dirname = os.path.join('sub.domain.ru', 'test', 'path')
        expected_filename = 'article.txt'

        dirname, filename = get_filepath(host, url, ext)
        self.assertEqual(expected_dirname, dirname)
        self.assertEqual(expected_filename, filename)

    def test_build_file_path_with_ext(self):
        """Проверка построения пути с расширение в пути"""
        host = 'sub.domain.ru'
        url = '/test/path/article.html/'
        ext = 'txt'

        expected_dirname = os.path.join('sub.domain.ru', 'test', 'path')
        expected_filename = 'article.txt'

        dirname, filename = get_filepath(host, url, ext)
        self.assertEqual(expected_dirname, dirname)
        self.assertEqual(expected_filename, filename)
