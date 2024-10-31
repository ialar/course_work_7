# course_work_7

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

## 'Atomic habits' (tracker of useful habits)
<h3>Контекст</h3>
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
<h3>Описание</h3>
Проект реализует бэкенд-часть SPA веб-приложения по трекингу полезных привычек пользователя с помощью планировщика асинхронных задач Celery.
Рассылка напоминаний для привычек настроена через интеграцию с Telegram (при наступлении указанного времени телеграм-бот автоматически отправляет сообщение пользователю).

## Установка и запуск
1. Клонируйте репозиторий с помощью команды:
```shell
git clone https://github.com/ialar/course_work_7.git
```
2. Перейдите в папку проекта:
```shell
cd course_work_7
```
3. Установите необходимые зависимости, выполнив команду:
```shell
pip install -r requirements.txt
```

Воспользуйтесь шаблоном .env.sample для создания файла `.env`.
Создайте БД, примените миграции и загрузите необходимые данные с помощью фикстур (.\fixtures\):
```commandline
psql -U postgres  
create darabase <db_name>;
\q
```

Запустите Redis:
```commandline
redis-server
```
Запустите сервер:
```commandline
python manage.py runserver
```
Запустите Celery:
```commandline
celery -A config worker -l INFO -P eventlet
celery -A config beat -l info -S django
```