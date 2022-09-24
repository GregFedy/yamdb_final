# Групповой проект «Yamdb»
## Описание
Проект YaMDb собирает отзывы (**Review**) пользователей на произведения (**Titles**). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (**Category**) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. 

Произведению может быть присвоен жанр (**Genre**) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (**Review**) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
### Функционал:
#### REVIEWS
- Получить список всех отзывов
- Создать новый отзыв
- Получить отзыв по id
- Частично обновить отзыв по id
- Удалить отзыв по id
#### COMMENTS
- Получить список всех комментариев к отзыву по id
- Создать новый комментарий для отзыва
- Получить комментарий для отзыва по id
- Частично обновить комментарий к отзыву по id
- Удалить комментарий к отзыву по id
#### AUTH
- Отправление ****confirmation_code**** на переданный **email**
- Получение **JWT-токена** в обмен на **email** и ****confirmation_code****
#### USERS
- Получить список всех пользователей
- Создание пользователя
- Получить пользователя по **username**
- Изменить данные пользователя по **username**
- Удалить пользователя по **username**
- Получить данные своей учетной записи
- Изменить данные своей учетной записи
#### CATEGORIES
- Получить список всех категорий
- Создать категорию
- Удалить категорию
#### GENRES
- Получить список всех жанров
- Создать жанр
- Удалить жанр
#### TITLES
- Получить список всех объектов
- Создать произведение для отзывов
- Информация об объекте
- Обновить информацию об объекте
- Удалить произведение

#### Для регистрации новых пользователей:
1. Необходимо отправить POST-запрос на добавление нового пользователя с параметрами email и **username** на эндпоинт `/api/v1/auth/signup/`.
2. YaMDB отправит письмо с кодом подтверждения (**confirmation_code**) на этот адрес email.
3. Дальше необходимо отправить POST-запрос с параметрами **username** и **confirmation_code** на эндпоинт `/api/v1/auth/token/`, в ответе на запрос придёт token (JWT-токен).
4. При желании можно отправить PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполнить поля в своём профайле (описание полей — в документации).

Документация к API доступна по адресу `http://127.0.0.1/redoc/`

## Установка
### Шаг 1. Установка Docker
Cкачать [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux следует убедиться, что установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Официальная [инструкция](https://docs.docker.com/engine/install/) по установке Docker.

### Шаг 2. Создать файл .env в директории /infra вутри приложения
Пример:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=127.0.0.1
```

### Шаг 3. Запуск docker-compose
Для запуска необходимо выполнить из директории /infra команду:
```bash
docker-compose up -d
```

### Шаг 4. Создание базы данных
Применяем миграции:
```bash
docker-compose exec web python manage.py migrate
```
### Шаг 5. Создание суперпользователя
Создание суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Шаг 6. Подгружаем статику
Выполните команду:
```bash
docker-compose exec web python manage.py collectstatic --no-input 
```

### Шаг 7. Заполнение базы тестовыми данными
Для заполнения базы тестовыми данными вы можете использовать файл fixtures.json, который находится в директории /infra. Выполните команду:
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

### Другие команды
Остановить работу всех контейнеров можно командой:
```bash
docker-compose down
```

Для пересборки и запуска контейнеров воспользуйтесь командой:
```bash
docker-compose up -d --build 
```

Мониторинг запущенных контейнеров:
```bash
docker stats
```

Останавливаем и удаляем контейнеры, сети, тома и образы:
```bash
docker-compose down -v
```

Команда покажет, сколько места на диске занимают образы, контейнеры, тома и билд-кеш. Будет и информация о том, сколько места можно освободить, удалив ненужное:
```bash
docker system df
```

Все неактивные (остановленные) контейнеры удаляются командой:
```bash
docker container prune
```

Можно удалить образы, какие использовались как промежуточные для сборки других образов, но на которые не ссылается ни один контейнер. Их называют dangling images (англ. «висячие образы»). Для выполнения такой задачи используется команда:
```bash
docker image prune
```
Удалить вообще всё, что не используется (неиспользуемые образы, остановленные контейнеры, тома, которые не использует ни один контейнер, билд-кеш), можно командой:
```bash
docker system prune
```

### Авторы проекта:

- [Bravo1109](https://github.com/Bravo1109)
- [GregFedy](https://github.com/GregFedy)
- [s-nikename](https://github.com/s-nikename)

[![Django-app workflow](https://github.com/GregFedy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/GregFedy/yamdb_final/actions/workflows/yamdb_workflow.yml)