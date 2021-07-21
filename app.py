import os
import sys

from modules import utils
from modules.parser import Parser
from modules.parser.converter import DefaultConverter
from modules.parser.strategy import DefaultStrategy
from modules.utils import check_console_args
from modules.web import Web, WebException
from modules.writer import FormattedWriter
from modules.writer.formatter import BeatufulFormatter
from modules.writer.output import IOOutput


def main(args: list[str]):
    if not check_console_args(args):
        print('Не передан параметр <URL адрес>')
        return

    link = sys.argv[1].strip()

    try:
        url = Web.get_uri_part(link)
    except WebException as e:
        print(e)
        return

    try:
        body = Web.get_page(link)
    except WebException as e:
        print('Не удалось получить страницу по указанному URL')
        return

    base_uri = f'{url.scheme}://{url.host}'
    converter = DefaultConverter
    parser = Parser(body, DefaultStrategy(), DefaultConverter(base_uri))
    text = parser.get_text()

    formatter = BeatufulFormatter(80)
    dirname, filename = utils.get_filepath(url.host, url.path)

    try:
        os.makedirs(dirname, exist_ok=True)
        filepath = os.path.join(dirname, filename)
        with open(filepath, 'w+', encoding='UTF-8') as f:
            output = IOOutput(f)
            writer = FormattedWriter(formatter, output)
            writer.write(text)
        print(f'Текст статьи сохранён в {filepath}')
    except OSError as e:
        print('Ошибка при записи результата')


if __name__ == '__main__':
    main(sys.argv)
