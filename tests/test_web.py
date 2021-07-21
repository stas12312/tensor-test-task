import unittest

from modules.web import Web, WebException


class WebTest(unittest.TestCase):

    def test_parse_full_https_uri(self):
        """Проверка парсинга полной https ссылки"""
        link = 'https://sbis.ru/contacts/54-novosibirskaya-oblast?tab=clients'
        url = Web.get_uri_part(link)

        self.assertEqual('https', url.scheme)
        self.assertEqual('sbis.ru', url.host)
        self.assertEqual('contacts/54-novosibirskaya-oblast', url.path)

    def test_parse_full_http_uri(self):
        """Проверка парсинга полной http ссылки"""
        link = 'http://sbis.ru/contacts'
        url = Web.get_uri_part(link)

        self.assertEqual('http', url.scheme, )
        self.assertEqual('sbis.ru', url.host)
        self.assertEqual('contacts', url.path)

    def test_parse_not_full_uri(self):
        """Проверка парсинга неполной ссылки"""
        link = 'http://sbis.ru'
        url = Web.get_uri_part(link)

        self.assertEqual('http', url.scheme, )
        self.assertEqual('sbis.ru', url.host)
        self.assertEqual('', url.path)

    def test_sub_domain(self):
        """Проверка парсинга ссылки с поддоменами"""
        link = 'https://sub1.sub2.test.ru/check/'
        url = Web.get_uri_part(link)

        self.assertEqual('https', url.scheme)
        self.assertEqual('sub1.sub2.test.ru', url.host)
        self.assertEqual('check/', url.path)

    def test_url_with_symbols(self):
        link = 'https://test.ru/check_differents-symbols.html'
        url = Web.get_uri_part(link)

        self.assertEqual('https', url.scheme)
        self.assertEqual('test.ru', url.host)
        self.assertEqual('check_differents-symbols.html', url.path)

    def test_invalid_uri(self):
        """Проверка парсинга некорректных ссылок"""
        link1 = 'https://asfcasd'  # некорректный хост
        link2 = '://test.ru'  # отсутствует схема
        link3 = 'asdf://test.ru'  # некорректная схема

        self.assertRaises(WebException, Web.get_uri_part, link1)
        self.assertRaises(WebException, Web.get_uri_part, link2)
        self.assertRaises(WebException, Web.get_uri_part, link3)
