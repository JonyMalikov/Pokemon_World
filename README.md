# Pokemon World
Pokemon_World

## Описание
Этот проект - покемонах
## Установка

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com/JonyMalikov/Pokemon_World.git

cd Pokemon_World
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

- Выполнить миграции:

```
python manage.py migrate
```

- Запустить проект:

```
python manage.py runserver
```

## Стек технологий

Python 3, Django 2.2.16, SQLite3.
