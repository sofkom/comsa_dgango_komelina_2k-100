#Cайт с отзывами

##  Run
- Cоздание виртуального окружения:
```shell
  python3 -m venv .venv
```
- Вход в виртуальное окружение:
```shell
  source ./.venv/bin/activate
```
- Установка зависимостей:
```shell
  pip install -r requirements.txt
```
- Запуск сервера:
```shell
  python3 manage.py runserver
```

- Выполнение миграций:
```shell
  python3 manage.py makemigrations
```
```shell
  python3 manage.py migrate
```
