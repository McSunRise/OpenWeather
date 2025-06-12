# OpenWeather Django App

Это Django-приложение для работы с погодными данными, построенное с использованием PostgreSQL, Redis и Docker.

## Стек технологий

- Python 3.13
- Django 5.2
- PostgreSQL 17
- Redis (с ACL)
- Docker / Docker Compose
- GitHub Actions (CI)

---

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/McSunRise/openweather.git
cd openweather
```
### 2. Создание `.env` файла
Создать файл на основе `.env.example`, вписать свои данные

### 3. Генерация секретного ключа

```bash
openssl genrsa -out private.pem 2048
```
Файл `private.pem` поместить в корень проекта

### 4. Запуск Docker-контейнера

```bash
docker compose up --build -d
```
По умолчанию приложение доступно по адресу: http://localhost:8000

### 5. Запуск тестов

```bash
docker compose run --rm django-web python manage.py test
```
