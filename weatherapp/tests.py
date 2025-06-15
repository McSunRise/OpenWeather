from django.core.cache import cache
from django.test import TestCase
from django.core.cache.backends.base import InvalidCacheBackendError
import os
import logging


class RedisCacheConnectionTest(TestCase):
    def test_redis_cache_connection(self):
        try:
            cache.set('redis_test_key', 'connected', timeout=5)
            value = cache.get('redis_test_key')
            self.assertEqual(value, 'connected', "Redis не возвращает ожидаемое значение")
        except (ConnectionError, InvalidCacheBackendError) as e:
            self.fail(f"Redis не подключён или произошла ошибка при доступе к кэшу: {e}")


class LogExistenceTest(TestCase):
    def test_log_existence(self):
        log_file_path = 'logs/django.log'
        logger = logging.getLogger('django')
        logger.info('Log existence test message')
        self.assertTrue(os.path.exists(log_file_path), 'Log file was not created.')
        with open(log_file_path, 'r') as f:
            content = f.read()
            self.assertIn('Log existence test message', content)

