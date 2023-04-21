Проект Instagram с API-Запросами

Реализован функционал CRUD для постов, входа и выхода, регистрации 
личный кабинет юзера а также API-запросы для проекта и лайки постов

Команды по миграции:

python manage.py makemigrations posts

python manage.py makemigrations accounts

python manage.py migrate

Команда для запуска приложения:

python manage.py runserver

Запросы в POSTMAN:

http://127.0.0.1:8000/api/posts/ - Вывод всех постов, метод GET

http://127.0.0.1:8000/api/posts/1/ - Вывод одного поста, метод GET

http://127.0.0.1:8000/api/posts/1/update/ - Редактирования поста при входе в профиль автора, метод PUT, данные: "author", "description"

http://127.0.0.1:8000/api/posts/3/delete/ - Удаление поста при входе в профиль автора, метод DELETE

http://127.0.0.1:8000/api/posts/create/ - Создание поста при авторизации, метод POST, данные: "description"

http://127.0.0.1:8000/api/posts/1/likes/ - Лайк для поста при авторизации, метод "POST"
