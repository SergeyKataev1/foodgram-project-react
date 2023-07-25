# FOODGRAM

FOODGRAM это сайт для размещения и поиска рецептов и дипломный проект ЯП.

### Технологии:

Python, Django, Docker, Gunicorn, NGINX, PostgreSQL.

### Для запуска проекта необходимо:

- Клонировать репозиторий:
```
https://github.com/SergeyKataev1/foodgram-project-react.git
```
- На удаленном сервере необходимо произвести установку необходимых пакетов для docker и docker-compose:
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```
- Проверим Docker:
```
sudo systemctl status docker 
```
- Локально отредактируйте файл infra/nginx.conf и в строке server_name впишите свой IP.
- Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```
scp -i c:/vm_access/<SSH_key_file> docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp -i c:/vm_access/<SSH_key_file> nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
- Cоздайте .env файл c переменными:
```
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>
```
- Теперь проект можно запустить на сервере:
```
sudo docker compose up -d --build 
```
### Настройка бекенда:
Для корректной работы бекенда необходимо выполнить следующие операции:
- Выполнить миграции для приложений users и recipes:
```
sudo docker compose exec backend python manage.py makemigrations users
sudo docker compose exec backend python manage.py makemigrations recipes
sudo docker compose exec backend python manage.py migrate
```
- Собрать статические файлы:
```
sudo docker compose exec backend python manage.py collectstatic --no-input
```
- Добавить данные об ингредиентах и тегах из заранее заготовленных файлов (для тестов):
```
sudo docker compose exec backend python manage.py load_data_json
```
- Создать суперпользователя Django:
```
sudo docker compose exec backend python manage.py createsuperuser
```
- Проект будет доступен по открытому IP сервера:
```
158.160.72.66:80
```

- Данные админки:
```
Логин: SergeyKataev1
Email: admin@admin.com
Пароль: SergeyKataev1
```
- P.S. Если на сервере больше одного проекта, настройте внешний NGINX.