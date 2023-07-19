# FOODGRAM

FOODGRAM это сайт для размещения и поиска рецептов.

### Технологии:

Python, Django, Docker, Gunicorn, NGINX, PostgreSQL.

### Для запуска проекта необходимо:

- Клонировать репозиторий:
```
https://github.com/SergeyKataev1/foodgram-project-react.git
```
- На удаленном сервере необходимо произвести установку необходимых пакетов для docker и docker-compose:

```
sudo apt install docker.io 
```
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
- Локально отредактируйте файл infra/nginx.conf и в строке server_name впишите свой IP.
- Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
- Cоздайте .env файл и впишите:
```
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>
```
- Теперь проект можно запустить на сервере:
```
sudo docker-compose up -d --build 
```
### Настройка бекенда:
Для корректной работы бекенда необходимо выполнить следующие операции:
- Выполнить миграции для приложений users и recipes:
```
sudo docker-compose exec backend python manage.py makemigrations users
sudo docker-compose exec backend python manage.py makemigrations recipes
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py makemigrations recipes
```
- Собрать необходимые статические файлы:
```
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
- Добавить данные об ингредиентах и тегах из заранее заготовленных файлов (по желанию):
```
sudo docker-compose exec backend python manage.py load_data
```
- Создать суперпользователя Django:
```
sudo docker-compose exec backend python manage.py createsuperuser
```
Проект будет доступен по открытому IP вашего сервера.
158.160.72.66

- Данные админки:
```
Логин: SergeyKataev1
Email: admin@admin.com
Пароль: SergeyKataev1
```