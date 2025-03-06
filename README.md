# Tender Parser

[![Maintainability](https://api.codeclimate.com/v1/badges/e4e652a4a8a595ff546b/maintainability)](https://codeclimate.com/github/Gamabyta24/tender_parser/maintainability)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pytest](https://img.shields.io/badge/pytest-8.3.5-brightgreen.svg)](https://docs.pytest.org/)

Проект выполнен в рамках тестового задания от работодателя.

**Tender Parser** выполняет обход первых двух страниц сайта по тегу **44ФЗ** [zakupki.gov.ru](https://zakupki.gov.ru/epz/order/extendedsearch/results.html).

При обходе, у каждого элемента списка (тендера) собирает ссылку на его печатную форму, заменяет `view.html` на `viewXml.html`, получает ссылку на печатную **XML-форму**. Распарсив этот **XML**, для каждого тендера получает значение `publishDTInEIS`, или `None` в случае его отсутствия.

## Используемые технологии

- `black>=25.1.0`
- `bs4>=0.0.2`
- `isort>=6.0.1`
- `lxml>=5.3.1`
- `pytest>=8.3.5`
- `requests>=2.32.3`
- `ruff>=0.9.9`
- `celery>=5.4.0`
- `docker>=28.0.1`
- `redis`

## Установка (Unix-like системы)
Установить [Docker](https://docs.docker.com/desktop/setup/install/linux/)

```sh
pip install uv

git clone https://github.com/Gamabyta24/tender_parser.git

cd tender_parser

make install
```

## Запуск

```sh
make run
```



