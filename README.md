
# Пример ML приложения с предварительно обученной моделью и тестом.

[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org)
[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)


Приложение определяет тональность текста на английском языке с помощью библиотеки Hugging Face.
Программный продукт реализует API, на базе библиотеки **Fastapi**, чтобы пользователь мог посылать посылать напрямую текст хосту, без разворачивания собстевенного приложения.

Чтобы отправить текст и узнать его окраску в адрессной строке пропишите: /predict/YOUR_TEXT
