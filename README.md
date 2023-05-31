# Electro online store

## Установка базы данных PostgreSQL
Вот прекрасный гайд

Ubuntu: [Тык](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)

Windows: [Тык](https://www.postgresql.org/download/windows/)

## Запуск проекта
Run in project directory:
```cpp
pip install -r requirements.txt
``` 
В "settings.py" Django нужно указать данные для подключения к БД PostgreSQL
```cpp
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'electro',
        'USER': 'login',
        'PASSWORD': 'password',
        'HOST': 'hostname/IP',
        'PORT': 'Пустое если порт стандартный',
    }
}
```
Для БД sqlite:
```cpp
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'BASE_DIR / electro',
    }
}
```
Миграция стандартных и пользовательских моделей Django
```cpp
python manage.py makemigrations 
```
```cpp
python manage.py migrate 
```
Создание пользователя "Администратора"
```cpp
python manage.py createsuperuser 
```
Запуск:
```cpp
python manage.py runserver 0.0.0.0:8000
```
Если нужно запустить localhost:
```cpp
python manage.py runserver
```
Остановка: 
```cpp
Ctrl + C
```
