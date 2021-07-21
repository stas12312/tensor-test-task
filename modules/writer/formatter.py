from abc import ABC, abstractmethod


class Formatter(ABC):
    """Класс для форматирования строки"""

    @abstractmethod
    def format(self, text: str) -> str:
        """Форматирования текста"""
        raise NotImplementedError()


class BeatufulFormatter(Formatter):
    """Класс для форматированного текста не превышая заданный размер строки"""

    def __init__(self, row_lenght: int, row_sep: str = '\n\n'):
        super(BeatufulFormatter, self).__init__()
        self.row_lenght = row_lenght
        self.row_sep = row_sep

    def format(self, text: str) -> str:
        paragragn_text = text.split('\n')
        formated_parts = []

        for paragraph in paragragn_text:
            # Если параграф пустой, пропускаем его
            cleare_paragrah = paragraph.strip()
            if not cleare_paragrah:
                continue

            words = cleare_paragrah.split(' ')
            row_parts = []
            row_length = 0
            paragraph_parts = []
            for word in words:
                word_len = len(word)

                # Обработка ситуации, когда попалась длинное слово
                # как правило, такое происходит со ссылками
                if word_len > self.row_lenght:
                    paragraph_parts.append(' '.join(row_parts))
                    row_length = 0
                    row_parts = []

                    word_parts = self.split_word_by_length(word)
                    # Исключаем последнее слово, для продолжения дозаписи в строку
                    word = word_parts.pop()
                    word_len = len(word)

                    paragraph_parts.extend(word_parts)

                if row_length != 0 and row_length + word_len > self.row_lenght:
                    paragraph_parts.append(' '.join(row_parts))
                    row_length = 0
                    row_parts = []

                row_length += len(word) + 1
                row_parts.append(word)

            if row_parts:
                paragraph_parts.append(' '.join(row_parts))

            formated_parts.append('\n'.join(paragraph_parts))

        return self.row_sep.join(formated_parts)

    def split_word_by_length(self, word: str) -> list[str]:
        """Разделение слова на подслова"""
        return [word[i:i + self.row_lenght] for i in range(0, len(word), self.row_lenght)]
