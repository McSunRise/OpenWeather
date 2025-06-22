from django.core.cache import cache
from django.test import TestCase
from django.core.cache.backends.base import InvalidCacheBackendError
from weatherproject.celery import divide
import os
import time
import logging


class RedisCacheTest(TestCase):
    def test_redis_cache_connection(self):
        try:
            cache.set('redis_test_key', 'connected', timeout=5)
            value = cache.get('redis_test_key')
            self.assertEqual(value, 'connected', "Redis не возвращает ожидаемое значение")
        except (ConnectionError, InvalidCacheBackendError) as e:
            self.fail(f"Redis не подключён или произошла ошибка при доступе к кэшу: {e}")


class LogTest(TestCase):
    def test_log_existence(self):
        log_file_path = 'logs/django.log'
        logger = logging.getLogger('django')
        logger.info('Log existence test message')
        self.assertTrue(os.path.exists(log_file_path), 'Log file was not created.')
        with open(log_file_path, 'r') as f:
            content = f.read()
            self.assertIn('Log existence test message', content)


class CeleryTest(TestCase):
    def test_celery_worker(self):
        result = divide.delay(5, 1)
        self.assertFalse(result.ready(), f'Task result is ready, despite 1s sleep >> {result.ready()}')
        time.sleep(2)
        self.assertTrue(result.ready(), f'Task result not ready 2s later >> {result.ready()}')
        try:
            self.assertEqual(result.get(), 5.0, 'Error')
        except AssertionError as exc:
            self.fail(exc)



