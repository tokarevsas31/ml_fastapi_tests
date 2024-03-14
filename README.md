[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

## Дополнительные улучшения были внесены командой (история авторских коммитов по ссылкам):
- [Кирилл Хитрин - khit-mle ](https://github.com/mlteamurfu2325/ml_fastapi_tests/commits?author=khit-mle):
    - добавлен `.gitignore`
    - исправлен ожидаемый ответ в тесте запроса `GET /`
    - реализован функционал сохранения запроса и оценки тональности в локальной БД `SQLite`
    - добавлены тесты по запросу `GET /predict/`
- [Алексей Горбачев - ANGorbachev](https://github.com/mlteamurfu2325/ml_fastapi_tests/commits?author=ANGorbachev):
    - имплементирован функционал по запросу запросу `GET /predict/`
    - добавлена обработка кейсов по кодам ошибок `400` и `404` при `GET /predict/`
- [Данил Хардин - DanilKhardi](https://github.com/mlteamurfu2325/ml_fastapi_tests/commits?author=DanilKhardi):
    - добавлен файл настроек логирования `log.ini`
    - реализовано дублирование вывода логов `uvicorn` в файл в текущей директории
- [Елена Икрина - LenaIkra](https://github.com/mlteamurfu2325/ml_fastapi_tests/commits?author=LenaIkra):
    - добавлена новая модель `PredictionResponse`, унаследованная от `BaseModel` и расширенная; упорядочено обращение к моделям в кодовой базе
    - расширена обработка исключений в коде
- [Александра Антонова - alexa313](https://github.com/mlteamurfu2325/ml_fastapi_tests/commits?author=alexa313):
    - добавлен файл конфигурации `.pre-commit-config.yaml` для унификация локальных проверок кода у разработчиков из команды
    - добавлена возможность через передачу аргумента при входе в программу через `main.py` определять, будет ли `uvicorn` принимать соединения через localhost или по внешнему IP
