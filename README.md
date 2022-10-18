api_yamdb
# Командный учебный проект api_yamdb

Сервис-обзор. 
Поддержаны: регистрация и аутентификация, произведения с категориями и жанрами, обзоры, комментирование

## Техстэк

**Client:** Все, что сможет распарсить JSON

**Server:** Python 3.7.13, Django 2.2.16, DRF 3.12.4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/jingleMyBells/api_final_yatube.git
```
```
cd api_yamdb
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python3 manage.py migrate
```
Заполнить демонстрационную базу данных:
```
python3 manage.py filldb
```
Запустить проект:

```
python3 manage.py runserver
```
## Регистрация и аутентификация:
- [POST: signup](http://127.0.0.1:8000/api/v1/auth/signup/)
- [POST: token](http://127.0.0.1:8000/api/v1/auth/token/)

## API Endpoints:
- [GET: titles](http://127.0.0.1:8000/api/v1/titles/)
- [GET: categories](http://127.0.0.1:8000/api/v1/categories/)
- [GET: genres](http://127.0.0.1:8000/api/v1/genres/)
- [GET: users](http://127.0.0.1:8000/api/v1/users/)
- [GET: auth](http://127.0.0.1:8000/api/v1/auth/)



## Authors

- Алия Бисенгалиева
- Никита Кривошеев
- Алексей Кудрявцев
