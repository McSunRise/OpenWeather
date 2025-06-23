import os
from celery import Celery
from django.conf import settings
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherproject.settings')

app = Celery("weather_celery")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# Просто таска для теста
@app.task
def divide(x, y):
    import time
    time.sleep(1)
    return x / y


@app.task
def get_weather(city_name: str):
    from weatherapp.requests import get_weather_data
    return asyncio.run(get_weather_data(city_name))
