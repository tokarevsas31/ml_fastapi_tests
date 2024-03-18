[![Tests](https://github.com/djvue/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/djvue/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.
# Данный учебный проект представляет собой API для анализа тональности текста с использованием предварительно обученной модели sentiment-analysis c использованием библиотеки [Hugging Face](https://huggingface.co/). 

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.
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

### Линтинг и форматирование кода

```
black *.py
flake8
```

### Запуск ML fastapi
Для запуска сервера выполняем следующую команду:
   ```
   uvicorn main:app --reload
   ```
После этого API будет доступен по адресу http://127.0.0.1:8000/

Tests GitHub Actions