
# api_quiz
Вопросы викторины (на английском)  

Запрашивает вопросы с https://jservice.io/api/random?count=1, сохраняет в бд.
Данные бд хранятся на docker volume

## Технологии
- Python 3.11
- Django 3.2
- DRF 3.12
- Postgres 15.3
- Docker


## Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```bash
$ git clone https://github.com/GitHub-NikName/quiz.git
$ cd quiz
```
- Скопировать и изменить настройки в .env
```bash
cp .env.exp .exp
````

```bash
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate --noinput
````
перезапустить.  

## Пример запроса

POST-запрос с праметром `questions_num` (количество вопросов) на эндпоинт `api/`

```json
{
  "questions_num": "integer"
}
```
Количество запрошенных вопросов сохраняются в бд, вопросы уникальны  
возвращает: предыдущий сохранённый вопрос для викторины:

```json
{
    "question_id": "integer",
    "question": "string",
    "answer": "string",
    "created_at": "date"
}
```


### Контакты:

Сергеев Михаил  
[email](server-15@yandex.ru)  
[telegram](https://t.me/sergeev_mikhail)  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
