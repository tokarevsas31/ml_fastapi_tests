[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# Данный учебный проект представляет собой API для анализа тональности текста с использованием предварительно обученной модели sentiment-analysis c использованием библиотеки [Hugging Face](https://huggingface.co/). 

Автоматически загружает предварительно обученную модель и позволяет просто передавать текст на английском языке для анализа, возвращая соответствующую тональность (положительную, негативную и т. д.).

## Использование:
### Без venv
Устанавливаем зависимости
   ```
   pip install -r requirements.txt
   ```

### С venv
Создаем venv
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
Устанавливаем зависимости в venv
   ```
   pip install -r requirements.txt
   ```

### Запуск ML fastapi
Для запуска сервера выполняем следующую команду:
   ```
   uvicorn main:app --reload
   ```
После этого API будет доступен по адресу http://127.0.0.1:8000/

Tests GitHub Actions
