Программная инженерия II. Практическое задание к модулю 2

Цель задания: научиться использовать Branches в Git.

Для задания выбрана модель определения эмоционального окраса текста

Для запуска в 1-м терминале запускаем команду для запуска сервера Uvicorn: uvicorn Api:app
Во 2-м терминале работаем с моделью посредством curl запроса:
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{ "text": "It was a wonderful journey. We have visited many beautiful places and seen many sightings! I am happy!" }'

Пример ответа: {"Исходный текст":"It was a wonderful journey. We have visited many beautiful places and seen many sightings! I am happy!","Результат:":"позитивный :)"}

Используемые модули: (см. requirements.txt)

Состав команды:
1. Воробьев Василий
2. Егоренкова Татьяна
3. Ильиных Виктория
4. Коньшина Ольга
5. Шабанов Дмитрий

