import os


def check_console_args(argv: list[str]) -> bool:
    """Проверка наличия нужных аргументов"""
    args_count = len(argv)
    if args_count < 2:
        return False
    return True


def get_filepath(host: str, url: str, ext='txt') -> tuple[str, str]:
    """Получение данных расположения файла по path адресу"""
    # Преобразования пути по формату ОС
    url_parts = url.rstrip('/').split('/')
    full_path = os.path.join(host, *url_parts)
    dirname, filename = full_path.rsplit(os.path.sep, maxsplit=1)
    filename = f'{filename.split(".")[0]}.{ext}'

    return dirname, filename
