**Формулировка задачи**

Большинство веб-страниц сейчас перегружено всевозможной рекламой… Наша задача «вытащить»
из веб-страницы только полезную информацию, отбросив весь «мусор» (навигацию, рекламу и тд).

Полученный текст нужно отформатировать для максимально комфортного чтения в любом
текстовом редакторе. Правила форматирования: ширина строки не больше 80 символов (если
больше, переносим по словам), абзацы и заголовки отбиваются пустой строкой. Если в тексте
встречаются ссылки, то URL вставить в текст в квадратных скобках. Остальные правила на ваше
усмотрение.

Программа оформляется в виде утилиты командной строки, которой в качестве параметра
указывается произвольный URL. Она извлекает по этому URL страницу, обрабатывает ее и
формирует текстовый файл с текстом статьи, представленной на данной странице.
В качестве примера можно взять любую статью на lenta.ru, gazeta.ru и тд
Алгоритм должен быть максимально универсальным, то есть работать на большинстве сайтов.

**Усложнение задачи 1:** Имя выходного файла должно формироваться автоматически по URL.
Примерно так:
http://lenta.ru/news/2013/03/dtp/index.html => [CUR_DIR]/lenta.ru/news/2013/03/dtp/index.txt

**Усложнение задачи 2:** Программа должна поддаваться настройке – в отдельном файле/файлах
задаются шаблоны обработки страниц.

---
Язык разработки: *Python 3.9.3*

Описание используемых библоиотек:
* Beautiful Soup - извлечение со страницы нужных элементов.
* requests - получение содержимого страниц.
* cx_Freeze - формирование исполняемого файла.

---
Запускать указанные ниже команды следует из директории проекта.

Запуск программы (Windows x64):
* Запустить через командную строку исполняемый файл `build\app.exe [url]`.
* После завершения работы программы в директории появится вложенные папки,
  в которых размещается файл txt с полученной информацией.
* Пример: https://lenta.ru/news/2021/07/20/potential/ => [Текущая директория]/lenta.ru/news/2021/07/20/potential.txt

Запуск тестов (Требуется Python 3.9):
* `pip install -r requirements.txt`
* `python -m unittest discover`

Запуск программы из исходных файлов (Требуется Python 3.9):
* `pip install -r requirements.txt`
* `python app.py [url]`

Сборка исполняемого файла (Требуется Python 3.9):
* `pip install -r requirements.txt`
* `python setup.py build` - после выполнения команды появится директория `build` внутри которой
будет распологаться директория с исполняемым файлом.

---
**Алгоритм**

_Модуль parser:_

Для получения нужной информации со страниц используется наблюдение о том,
что на основных новостных сайтах вся полезная информация находится в html тэгах` <p>` и `<h1>`,
для извлечения данных тэгов исползуется библиотека Beautiful Soup.

После получения необходимых элементов страниц они обрабатываются и очищаются от html 
элементов, преобразуясь в набор текстовых параграфов.

_Модуль writer:_

Очищенный текст форматируется в соответствии с требованиями и записывается в файл, 
расположение и название которого формируется на основе URL.

*Дополнительные правила форматирования*:
* Если слово длиннее 80 символов, оно разбивается на подстроки длиной 80 символов
  и начинает записываться со следующей строки.
* Название ссылки помещается в круглые скобки (), через пробел следует ссылка в квадратных скобках []
Пример: (Ссылка) [https://link.ru]
  
---
Структура проекта:
* `modules/parser` - Модуль, отвечающий за получение с HTML-страницы нужной информации. 
  Для этого исползуется класс Parser из `modules/parser/parser.py` -
  данный класс принимает на вход два объекта классов, реализующих основную
  логику: Converter - преобразующий html-элементы в текст и Strategy - определяющий, 
  какие элементы будут получены со страницы. Данные классы являются абстрактными,
  для решения задачи реализованы DefaulStrategy и DefaulConverter, реализующие нужную логику.
  
* `modules/writer` - Модуль, отвечающий за форматирование текста и его запись в файл. 
  Для этого используется класс FormattedWriter, реализованный в `modules/writer/writer.py`. 
  Данный класс принимает два объекта классов Formatter - реализующий логику форматирования текста и 
  Output - реализующий логику записи текста на внешнее устройство. 
  Данные классы так же являются абстрактными, для решения поставленной задачи реализованы
  BeatufulFormatter и IOOutput.
  
* `modules/web.py` - Класс для получения страницы и разбора ссылки на составляющие.
* `modules/utils.py` - Набор вспомогательных функций для решения задачи.

* `tests` - Модуль с юнит-тестами, позволяющие проверять корректность работы модулей.

---
Результат работы размещены в директории `results`:

* lenta.ru - https://lenta.ru/news/2021/07/21/talibanerdogan/ - Извлечена
  вся полезная информация.
  
* vesti.ru - https://www.vesti.ru/article/2590822 - Извлечена вся полезная информация,
  часть полученной информации избыточна и не имеет отношения к статье (Контактные данные, юридические данные).
  
* gazeta.ru - https://www.gazeta.ru/social/2021/07/21/13784648.shtml - Была получена вся полезная информация,
так же имеется избыточная информация (Контактные данные, юридические данные).
  
* rbc.ru - https://www.rbc.ru/newspaper/2021/07/21/60f6a38a9a7947ec03f3181c - Была получена вся полезная информация.

___
Направления дальнейшего улучшения:

* Добавление возможности указывать несколько URL в параметрах.
* Добавление возможности указать главную страницу сайта и автоматически получить файлы статей, 
  ссылки на которые распологаются на указанной странице.
* Добавление конфигурационного файла с параметрами настройки извлечения информации (Названия классов и 
  тэгов, в которых содержится нужная информация или исключения, которые не нужно обрабатывать).
* Добавление черного списка словосочетаний, наличие которых откидывает ненужный блок (Например: Контакты).
* Оформление программы как веб-сервис или Telegram Бот для удобного использования.
* Добавление ссылок на картинки из статей.
* Использование сервиса по сокращению ссылок для улучшения комфортности прочтения.
