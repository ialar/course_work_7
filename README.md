# course_work_7

## 'Atomic habits' (tracker of useful habits)
Проект реализует бэкенд-часть SPA веб-приложения по трекингу полезных привычек пользователя с помощью планировщика асинхронных задач Celery.

## Стек
* Python
* DRF
* PostgreSQL
* Redis
* Celery

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