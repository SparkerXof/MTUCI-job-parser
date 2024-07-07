Установка:

1. Клонировать репозиторий в локальную директорию.
2. Собрать Docker контейнер с помощью "docker build -t <имя_контейнера> .".
3. Запустить контейнер через "docker run -it -p 8000:8000 <имя_контейнера>".

Применение:

1. На страницу поиска вакансий можно попасть из корневого раздела хоста.
2. Для работы поиска необходимо выбрать хотя бы один сервис.
3. В пункте "Регион" необходимо использовать официальные названия субъектов РФ.
4. Для поиска по нескольким регионам названия пишутся через запятую.
5. Вакансии можно посмотреть через панель администрирования.
6. Для создания аккаунта администратора использовать "python3 manage.py makesuperuser".
