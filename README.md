# Проект YaCut
### Стек:
Flask



## Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.


Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:ragozindenis/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Обновить pip и установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать в корневой папке файл .env с данными:

```
FLASK_APP=yacut (названия)
FLASK_ENV=development (режим)
DATABASE_URI=sqlite:///db.sqlite3 (путь до бд)
SECRET_KEY=YOUR_SECRET_KEY (секретный ключ)
```

Запуск проекта:

```
flask run
```
