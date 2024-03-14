__Описание:__

* Выбрана обученная модель для определения объектов в катринке `google/owlvit-base-patch32`
  с сайта [huggingface.co](https://huggingface.co/google/owlvit-base-patch32)
* Модель определения объектов принимает на вход ссылку на изображение и название объекта(объектов) которое необходимо найти - внизу есть примеры curl запросов
* На выходе модель определения объектов отдаёт массив найденных объектов, каждый объект содержит:
    * `score` - вероятность определения объекта
    * `label` - название объекта
    * `box` - координаты квадрата в котором найден объект на изображении
* Для определения тональности текста используется pipline (`sentiment-analysis`) с моделью по
  умолчанию `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
* На вход принимает текст, на выходе тональность и вес определения

__Варианты использования определения объектов в катринке:__

* Определение количества машин на парковке
* Определение животных в кадре
* Поиск предметов на конвейере
* Поиск запрещенных объектов

__Варианты использования определения тональности текста:__

* Определение тональности отзывов маркетплейсов
* Определение тональности новостей

__Реализация:__

* Реализовано API с помощью библиотеки FastAPI
* Для первоначального определения объектов на изображении интегрирована обученная модель `EfficientNetB0`
* Для определения объектов по названию в изображении, интегрирована обученная модель `google/owlvit-base-patch32`
* Для определения тональности текста, используется pipline (`sentiment-analysis`) с моделью по
  умолчанию `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
* Разработаны тесты

__Локальный запуск:__

* Стянуть проект `git clone git@github.com:DMax-w/ml_fastapi_tests.git`
* Перейти в проект `cd ml_fastapi_tests`
* Подготовить окружение (_виртуальная среда, установка пакетов_) командой `make deps`
* Запуск тестов `make test`
* Запустить командой `make run`

Дополнительные команды описаны в `Makefile`

Для систем в которых отсутствует утилита `make`, запуск можно выполнить путём выполнения содержимого соответствующих
команд описанных в `Makefile`

__Результат:__

* Разработано API с интегрированными обученными моделями ML:
* Локальный:
    * `http://localhost:8000/` [healthcheck](http://localhost:8000/) - расположено приветствие, можно проверить, что сервер запущен
    * `http://localhost:8000/docs/` [docs](http://localhost:8000/docs/) - расположена документация, можно выполнить запросы из интерфейса
    * `http://localhost:8000/find-object/` - метод с моделями определения объектов в картинке
    * `http://localhost:8000/classify-text/` - метод с моделями определения тональности текста

__Примеры запросов для curl локально:__

`curl -X 'POST'
'http://localhost:8000/find-object/'
-H 'Content-Type: application/json'
-d '{
"url": "https://parkingcars.ru/wp-content/uploads/2021/02/stoyanka-1024x683.jpg",
"targets": "car"
}'`

`curl -X 'POST'
'http://localhost:8000/find-object/'
-H 'Content-Type: application/json'
-d '{
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2_q3Ph31cc_MgsovOHJOKqIyTxaWnWmckLw&usqp=CAU",
"targets": "hog"
}'`

`curl -X 'POST'
'http://localhost:8000/find-object/'
-H 'Content-Type: application/json'
-d '{
"url": "https://storage.yandexcloud.net/mfi/1242/products/main/3474.jpg",
"targets": "pineapple"
}'`

`curl -X 'POST'
'http://localhost:8000/classify-text/'
-H 'Content-Type: application/json'
-d '{
"text": "I like machine learning!"
}'`

`curl -X 'POST'
'http://localhost:8000/classify-text/'
-H 'Content-Type: application/json'
-d '{
"text": "I hate machine learning!"
}'`
