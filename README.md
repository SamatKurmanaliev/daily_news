# Daily News
***
## Описание
> Это проект новостного веб-портала, разработанный с использованием языка программирования
> Python и фреймворка Django. 
> Веб-портал предоставляет пользователю возможность просматривать и читать новости.
> Можно добавлять авторов новостей так и пользователей. К постам новостей можно ставить 
> различные статусы такие как "like" и "dislike". Есть возможность редактировать свой пост, 
> а также полностью его удалить.
***
## Какие технологии использованы
- Linux
- PostgreSQL
- Python 3.10
- Django 4.2
- DjangoRestFramework
***
## Как поднять проект локально?
```
$ git clone https://github.com/SamatKurmanaliev/daily_news
$ cd daily_news
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
***
## Дальше нужно создать БД в PostgreSQL и запустить сервер
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
