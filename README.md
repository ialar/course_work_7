# course_work_7

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/doc/)
[![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/pycharm/documentation/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white&color=092E20&labelColor=gray)](https://www.djangoproject.com/start/)
[![Django REST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://docs.github.com/en/actions)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.readthedocs.io/en/latest/)
[![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)](https://docs.celeryproject.org/en/stable/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&color=2496ED&labelColor=gray)](https://docs.docker.com/)

## 'Atomic habits' (tracker of useful habits)

### Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.

### Описание
Проект реализует бэкенд-часть SPA веб-приложения по трекингу полезных привычек пользователя с помощью планировщика асинхронных задач Celery.
Рассылка напоминаний для привычек настроена через интеграцию с Telegram (при наступлении указанного времени телеграм-бот автоматически отправляет сообщение пользователю).

### Требования
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск
1. Клонируйте репозиторий с помощью команды и перейдите в папку проекта:
```shell
git clone https://github.com/ialar/course_work_7.git
cd course_work_7
```
2. Создайте файл .env на основе .env.sample и заполните его своими данными:
```bash
cp .env.example .env
```
3. Соберите образы и запустите контейнеры командой:
```bash
docker-compose up -d --build
```

### Создание суперпользователя
Чтобы создать суперпользователя, выполните команду:
```bash
docker-compose exec <container_name_or_id> python manage.py csu
```

### Наполнение БД
При необходимости наполните базу данных с помощью фикстур:
```bash
python manage.py loaddata fixtures/<name>.json
```

### Доступ и работа с приложением
- Документация: http://localhost:8000/redoc/ (либо /swagger/)
- Админка: http://localhost:8000/admin/